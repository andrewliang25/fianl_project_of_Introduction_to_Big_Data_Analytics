from pymongo import MongoClient
import datetime
import pickle
import sklearn
import pprint

def normalize(data_list):
    result = []
    AVG_2_HOUR_TEMP = 23.886516
    AVG_3_HOUR_TEMP = 23.886232
    AVG_3_HOUR_PRES = 1010.499932
    SD_2_HOUR_TEMP = 5.917852
    SD_3_HOUR_TEMP = 5.918066
    SD_3_HOUR_PRES = 6.441873
    result.append((data_list[0]-AVG_2_HOUR_TEMP)/SD_2_HOUR_TEMP)
    result.append((data_list[1]-AVG_3_HOUR_TEMP)/SD_3_HOUR_TEMP)
    result.append((data_list[2]-AVG_3_HOUR_PRES)/SD_3_HOUR_PRES)
    return result

def get_need_data(stationId):
    data = []
    two_hour_time = datetime.datetime.now() - datetime.timedelta(hours = 2)
    three_hour_time = datetime.datetime.now() - datetime.timedelta(hours = 3)
    four_hour_time = datetime.datetime.now() - datetime.timedelta(hours = 4)
    client = MongoClient('localhost', 27017)
    col = client.WEATHER.meteorology
    two_hour_data = col.find_one({"time": {"$lte": two_hour_time, "$gte": three_hour_time}, "stationId": stationId})
    three_hour_data = col.find_one({"time": {"$lte": three_hour_time, "$gte": four_hour_time}, "stationId": stationId})
    # pprint.pprint(two_hour_data)
    # pprint.pprint(three_hour_data)
    data.append(two_hour_data['TEMP'])
    data.append(three_hour_data['TEMP'])
    data.append(three_hour_data['PRES'])
    result = []
    result.append(data)
    return result

def predict_rain(stationId):
    datas = get_need_data(stationId)
    pickle_in = open('first_outcome.pickle', 'rb')
    regressor = pickle.load(pickle_in)
    print(regressor.predict(datas)[0])
    return float((regressor.predict(datas)[0]))
    # print(type(regressor))

def temp(stationId, hour):
    result = []
    client = MongoClient('localhost', 27017)
    col = client.WEATHER.meteorology
    condition = {"$gte": datetime.datetime.now() - datetime.timedelta(hours = hour)}
    for data in col.find({"time": condition, "stationId": stationId}):
        result.append(data["TEMP"])
    return result

def pres(stationId, hour):
    result = []
    client = MongoClient('localhost', 27017)
    col = client.WEATHER.meteorology
    condition = {"$gte": datetime.datetime.now() - datetime.timedelta(hours = hour)}
    for data in col.find({"time": condition, "stationId": stationId}):
        result.append(data["PRES"])
    return result

def main():
    predict_rain("C0A560") 

if __name__ == '__main__':
    main()
# data[[2小時前溫度, 3小時前溫度, 3小時前氣壓],[2小時前溫度, 3小時前溫度, 3小時前氣壓]]