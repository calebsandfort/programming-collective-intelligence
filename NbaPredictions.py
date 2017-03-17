import recommendations as rec
import requests

def recommend():
    rownames1, colnames1, data1, trainingGameExamples = rec.readfile('TrainingGameExamples.csv')
    rownames2, colnames2, data2, todaysGameExamples = rec.readfile('TodaysGameExamples.csv')

    trainingGameExamples.update(todaysGameExamples)

    delete = True

    for key, dict in todaysGameExamples.items():
        predictions = rec.getRecommendations(trainingGameExamples, key)

        payload = {}
        payload["key"] = key
        payload["delete"] = delete

        for pair in predictions:
            payload[pair[1]] = pair[0]

        r = requests.get("http://dev-csandfort.gwi.com/guerillalogisticsapi/MachineLearning/SaveGameRecommendation", params=payload)
        print(r.url)
        delete = False

    # [print("%20s %s" % (key, dict)) for key, dict in results.items()]