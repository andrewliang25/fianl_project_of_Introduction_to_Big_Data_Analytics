from flask import Flask, render_template, jsonify, request, make_response, session, current_app
from flask_cors import CORS
from pymongo import MongoClient
import model

app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.route('/GET/predictrain/<stationId>', methods=['GET','OPTION'])
def get_predict_rain(stationId):
    rsp = {
        'success': 'OK',
        'rain': model.predict_rain(stationId),
    }
    return jsonify(rsp)

@app.route('/GET/temp/<stationId>/<hour>', methods=['GET','OPTION'])
def get_temp(stationId, hour):
    rsp = {
        'success': 'OK',
        'rain': model.temp(stationId, hour),
    }
    return jsonify(rsp)

@app.route('/GET/pres/<stationId>/<hour>', methods=['GET','OPTION'])
def get_pres(stationId, hour):
    rsp = {
        'success': 'OK',
        'rain': model.pres(stationId, hour),
    }
    return jsonify(rsp)

if __name__ == '__main__':
    app.run()