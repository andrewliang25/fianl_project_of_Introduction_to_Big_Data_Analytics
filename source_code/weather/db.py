from pymongo import MongoClient
from meteorology_data import get_data
import schedule
import time

def insert_data():
    client = MongoClient('localhost', 27017)
    datas = get_data()
    db = client.WEATHER
    for data in datas:
        db.meteorology.insert_one(data)
    print("新增資料完成!")
    

def main():
    schedule.every().hour.do(insert_data)
    schedule.run_all()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()