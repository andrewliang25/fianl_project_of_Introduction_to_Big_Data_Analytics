import PreprocessData
import VisualizingDecisionTree
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import metrics
from sklearn.cross_validation import train_test_split

def CreateClassifier(train_X, train_Y):
    classifier = tree.DecisionTreeClassifier()
    trained_classifier = classifier.fit(train_X, train_Y)
    return trained_classifier

def main():
    place_weather = PreprocessData.PreprocessData()
    feature_columns = ['ObsTime', 'StnPres', 'SeaPres', 'Temperature', 'Td dew point', 'RH', 'Precp',
                       'PrecpHour', 'SunShine', 'SunShineRate', 'VisbMean', 'EvapA', 'Cloud Amount']
    weather_X = place_weather[feature_columns]
    weather_Y = place_weather['NextDayPrecp']
    train_X, test_X, train_Y, test_Y = train_test_split(weather_X, weather_Y.astype('int'), test_size = 0.3)

    rainfall_classifier = CreateClassifier(train_X, train_Y)

    test_Y_predicted = rainfall_classifier.predict(test_X)
    accuracy = metrics.accuracy_score(test_Y, test_Y_predicted)
    VisualizingDecisionTree.Visualize(rainfall_classifier, feature_columns, weather_Y.to_string())
    print(accuracy)

if __name__ == "__main__":
    main()
