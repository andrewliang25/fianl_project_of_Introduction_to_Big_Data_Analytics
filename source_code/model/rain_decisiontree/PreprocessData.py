import pandas as pd
import numpy as np
import os

###folder_path = 'c:/users/user/desktop/bigdataproject/SUAO/'
folder_path = os.getcwd() + '/SUAO/'
print(folder_path)
save_file_name = 'SUAO_ALL.csv'

def Merge(folder_path, save_file_name):
    if not os.path.isfile(folder_path + save_file_name):
        os.chdir(folder_path)
        file_list = os.listdir()

        combined_file = pd.concat(
            [pd.read_csv(folder_path + file_name) for file_name in file_list])

        combined_file.to_csv(folder_path + save_file_name,
                             encoding='utf_8_sig', index=False)


def Normalize(input_series):
    mu = input_series.mean()
    std = input_series.std()
    z_score_normalized = (input_series - mu) / std
    return z_score_normalized

def PreprocessData():
    Merge(folder_path, save_file_name)
    place_weather = pd.read_csv(folder_path + save_file_name)
    next_day_precp = pd.Series(place_weather['Precp']).shift(periods=-1, fill_value=0)
    #next_two_day_precp = pd.Series(place_weather['Precp']).shift(periods=-2, fill_value=0)
    place_weather = place_weather[['ObsTime', 'StnPres', 'SeaPres', 'Temperature', 'Td dew point', 'RH', 'Precp',
                                   'PrecpHour', 'SunShine', 'SunShineRate', 'VisbMean', 'EvapA', 'Cloud Amount']]
    place_weather = pd.DataFrame(place_weather, columns=['ObsTime', 'StnPres', 'SeaPres', 'Temperature', 'Td dew point', 'RH', 'Precp',
                                         'PrecpHour', 'SunShine', 'SunShineRate', 'VisbMean', 'EvapA', 'Cloud Amount', 'NextDayPrecp'])
    place_weather['NextDayPrecp'] = next_day_precp
    #place_weather["NextTwoDayPrecp"] = next_two_day_precp
    place_weather = place_weather.replace('/', 0.0)
    place_weather = place_weather.replace('T', -1)
    place_weather = place_weather[place_weather['Precp'] != -1]
    place_weather = place_weather.dropna()
    
    for column in place_weather:
        #print(column)
        place_weather[column] = pd.to_numeric(place_weather[column], downcast='float')
        place_weather[column] = Normalize(place_weather[column])
        #print(place_weather.head(20))
    return place_weather   
