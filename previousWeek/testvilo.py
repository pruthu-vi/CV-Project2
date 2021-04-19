from datetime import datetime
import pytz

if __name__ == "__main__":
  test = datetime.datetime.now(pytz.timezone('Australia/Sydney'))
  print(test.timestamp())
  # print(test.utcfromtimestamp(test.timestamp()))
  print(test.tzinfo)
  print(test.hour)
  print(test.astimezone(pytz.utc).hour)