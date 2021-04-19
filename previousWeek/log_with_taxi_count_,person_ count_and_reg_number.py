import boto3
import re
import logging
from log_with_meraki_and_rekognition import  meraki_output
# TTR - Needs further improvements and possible changes!

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(message)s")
file_handler = logging.FileHandler("vehicle_reg_plates.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def detect_labels(file):
    """Use AWS Rekognition to label/categorise key elements in the image

    Parameters
    ----------
    file : str
        The file location of the image

    Returns
    -------
    [type]
        [description]
    """
    client = boto3.client("rekognition", region_name="ap-southeast-2")

    with open(file, "rb") as image:
        result = client.detect_labels(Image={"Bytes": image.read()})  ## Changed 

    return result["Labels"]


def detect_text(file, roi=False):
    """Use AWS Rekognition to read text in the image

    Parameters
    ----------
    file : str
        The file location of the image

    Returns
    -------
    [type]
        [description]
    """

    client = boto3.client("rekognition", region_name="ap-southeast-2")

    with open(file, "rb") as image:
        # Bounding boxes are passed in to detect_text to narrow search regions for text 
        if roi is not False:
            result = client.detect_text(
                Image={"Bytes": image.read()},
                Filters={"RegionsOfInterest": [{"BoundingBox": roi}]},
            )
        else:
            result = client.detect_text(Image={"Bytes": image.read()})

    return result["TextDetections"]


def correct_taxi_plate(plate: str) -> str:
    numberPlate = re.sub(r"[\s\.:-]", "", plate)
    numberPlate = re.sub(r"^[1l7]", "T", numberPlate, 1)

    return numberPlate


def is_taxi_plate(plate: str) -> bool:
    matched = re.match(r"^TC?\d{3,4}$", plate)

    return bool(matched)

# TODO: Non Taxi identification needs to be improved
def is_non_taxi_plate(plate: str) -> bool:
    matched = re.compile(r"^[A-Z0-9]{5,7}").search(plate)
    if bool(matched):
        matched = re.compile(r"\d").search(plate)

    return bool(matched)

# Vehicle count by rekognition

def  extract_taxi_count(taxi_instances) -> int:

                        
    
    if taxi_instances!=None:
        len_of_objects = len(taxi_instances)                  ## If labels of response is not null

       
    return(len_of_objects)           


def extract_person_count(person_instances):

    if person_instances !=None:
        len_of_objects= len(person_instances)
    return(person_instances)

# Logging filtered labels/no plates that resides within the bounding boxes of each instance of any vehicle detected

def extract_taxi_status(vehicle_instances,person_instances):
 
     for key in vehicle_instances:
        if not vehicle_instances[key]:
            continue
        for instance in vehicle_instances[key]:
            match_found = detect_text(filename, instance["BoundingBox"])
            for match in match_found:
                if match["Type"] == "LINE":
                    numberPlate = correct_taxi_plate(match["DetectedText"])
                    taxiCount = extract_taxi_count     
                    if is_taxi_plate(numberPlate):
                        logger.info(f'Taxi Registration Plate: {match["DetectedText"]}')
                        logger.info(f'By Rekognition - Vehicle Count :'+str(len(vehicle_instances)))
                        logger.info(f'By rekognition - Person Count :'+str(len(person_instances)))
                        


                        print(
                            match["DetectedText"]
                            + ":"
                            + str(("Taxi", instance["BoundingBox"]))
                        )
                    elif is_non_taxi_plate(numberPlate):
                        logger.info(
                            f'Vehicle (Non-Taxi) Registration Plate: {match["DetectedText"]}'
                        )
                        print(
                            match["DetectedText"]
                            + ":"
                            + str(("Not A Taxi", instance["BoundingBox"]))
                        )

def extract_meraki_status():
    output = meraki_output()
    for out_temp in output:
        meraki_zone_zoneid = out_temp['zone']['zoneId']
        meraki_zone_label = out_temp['zone']['label']

        meraki_analytics_zoneid = out_temp['analytics']['zoneId']
        meraki_analytics_entrances = out_temp['analytics']['entrances']
        meraki_analytics_averageCount = out_temp['analytics']['averageCount']
        

        logger.info(f'By Meraki -ZoneId :' + str(meraki_zone_zoneid))
        logger.info(f'By Meraki -Zone Label :' + str(meraki_zone_label))
        logger.info(f'By Meraki -Analytics ZoneID :' + str(meraki_analytics_zoneid))
        logger.info(f'By Meraki -Analytics Entrance :' + str(meraki_analytics_entrances))
        logger.info(f'By Meraki -Analytics Average count :' + str(meraki_analytics_averageCount))

if __name__ == "__main__":
    filename = "airport-2.jpg"
    labels = detect_labels(filename)
    carDetected: bool = False
    carInstances: dict = {}
    personInstances:dict = {}
    for label in labels:
        for element in ["Car", "Automobile", "Vehicle"]:
            if label["Name"] == element:
                carDetected = True
                carInstances[f"{element}_Instances"] = label["Instances"]
                continue

    for label in labels:
        for element in ["Person"]:
            if label["Name"]==element:
                personDetected = True
                personInstances[f"{element}_Instances"]=label["Instances"]
                continue
                
    print(carInstances)
    print(personInstances)
    logger.info(f"instances: {carInstances}")

    if carDetected:
        extract_taxi_status(carInstances,personInstances)
        extract_meraki_status()
