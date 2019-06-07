from pymongo import MongoClient
import datetime
import pprint


two_hour_time = datetime.datetime.now() - datetime.timedelta(hours = 2)
three_hour_time = datetime.datetime.now() - datetime.timedelta(hours = 3)
four_hour_time = datetime.datetime.now() - datetime.timedelta(hours = 4)

client = MongoClient('localhost', 27017)
db = client.WEATHER
# filter_condition = {"$lte": three_hour_time, "$gte": two_hour_time}
filter_condition = {"$lte": two_hour_time, "$gte": three_hour_time}

# for data in db.meteorology.find({"time": filter_condition, "stationName": "福山"}):
#     print("兩小時前資料")
#     pprint.pprint(data)
# for data in db.meteorology.find({"stationName": "福山"}):
#     pprint.pprint(data)
two_hour_data = db.meteorology.find_one({"time": {"$lte": two_hour_time, "$gte": three_hour_time}, "stationId": "C0A560"})
three_hour_data = db.meteorology.find_one({"time": {"$lte": three_hour_time, "$gte": four_hour_time}, "stationId": "C0A560"})
print("兩小時前資料")
print(two_hour_data['time'])
print("三小時前資料")
print(three_hour_data)

# print(datetime.datetime.now())
# print(one_hour_time)
# print(two_hour_time)
# print(three_hour_time)