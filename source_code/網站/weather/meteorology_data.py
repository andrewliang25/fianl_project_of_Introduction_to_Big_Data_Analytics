import math
import requests
import json
import datetime
from pprint import pprint

# API document : https://opendata.cwb.gov.tw/dist/opendata-swagger.html#/%E8%A7%80%E6%B8%AC/get_v1_rest_datastore_O_A0001_001

def process_data(rawdata):
    result_data = {
        'stationName': None,
        'stationId': None,
        'time': None,
        'WDIR': None,
        'WDSD': None,
        'TEMP': None,
        'HUMD': None,
        'PRES': None,
        'SUN': None
    }
    result_data['stationName'] = rawdata['locationName']
    result_data['stationId'] = rawdata['stationId']
    result_data['time'] = datetime.datetime.strptime(rawdata['time']['obsTime'], "%Y-%m-%d %H:%M:%S")
    result_data['WDIR'] = check_data(rawdata['weatherElement'][1]['elementValue'])
    result_data['WDSD'] = check_data(rawdata['weatherElement'][2]['elementValue'])
    result_data['TEMP'] = check_data(rawdata['weatherElement'][3]['elementValue'])
    result_data['HUMD'] = check_data(rawdata['weatherElement'][4]['elementValue'])
    result_data['PRES'] = check_data(rawdata['weatherElement'][5]['elementValue'])
    result_data['SUN'] = check_data(rawdata['weatherElement'][6]['elementValue'])
    return result_data

def check_data(data):
    if data == "null":
        return "null"
    elif math.isclose(float(data),-99.0, abs_tol=0.1):
        return "null"
    else:
        try:
            result = float(data)
        except:
            print("資料來源有誤，加入失敗!")
            result = "null"
        finally:
            return result

# empty_data = {
#         'stationName': None,
#         'stationId': None,
#         'time': None,
#         'WDIR': None,
#         'WDSD': None,
#         'TEMP': None,
#         'HUMD': None,
#         'PRES': None,
#         'SUN': None
#     }

def get_data(): 
    # "limit": 1
    param = {"Authorization":"CWB-531E4E35-FFF3-4740-BD4D-7543DCC9BFCE"}
    URL = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001"
    r = requests.get(URL, params=param)
    # pprint(r.text)
    json_data = json.loads(r.text)
    all_raw_data = json_data['records']['location']
    finish_data = []
    for i in all_raw_data:
        finish_data.append(process_data(i))
    # pprint(finish_data)
    return finish_data