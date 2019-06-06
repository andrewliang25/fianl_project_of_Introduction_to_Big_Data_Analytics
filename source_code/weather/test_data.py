import datetime
from pymongo import MongoClient



now = datetime.datetime.now()
one_hour_time = datetime.datetime.now() - datetime.timedelta(hours = 1)
two_hour_time = datetime.datetime.now() - datetime.timedelta(hours = 2)
three_hour_time = datetime.datetime.now() - datetime.timedelta(hours = 3)

test_data = [{
        'stationName': "福山",
        'stationId': "C0A560",
        'time': now,
        'WDIR': 999,
        'WDSD': 0.0,
        'TEMP': 24.0,
        'HUMD': "null",
        'PRES': 960.1,
        'SUN': "null"
    },{
        'stationName': "福山",
        'stationId': "C0A560",
        'time': one_hour_time,
        'WDIR': 999,
        'WDSD': 0.0,
        'TEMP': 23.4,
        'HUMD': "null",
        'PRES': 960.5,
        'SUN': "null"
    },
    {
        'stationName': "福山",
        'stationId': "C0A560",
        'time': two_hour_time,
        'WDIR': 999,
        'WDSD': 0.0,
        'TEMP': 22.2,
        'HUMD': "null",
        'PRES': 960.9,
        'SUN': "null"
    },{
        'stationName': "福山",
        'stationId': "C0A560",
        'time': three_hour_time,
        'WDIR': 999,
        'WDSD': 0.0,
        'TEMP': 21.3,
        'HUMD': "null",
        'PRES': 963.7,
        'SUN': "null"
    },]

client = MongoClient('localhost', 27017)
db = client.WEATHER
for data in test_data:
    db.meteorology.insert_one(data)
print("Finish!")