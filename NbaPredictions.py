import recommendations as rec
import requests

def recommend():
    rownames1, colnames1, data1, trainingGameExamples = rec.readfile('TrainingGameExamples.csv')
    rownames2, colnames2, data2, todaysGameExamples = rec.readfile('TodaysGameExamples.csv')

    trainingGameExamples.update(todaysGameExamples)

    print("ClearGameRecommendations")
    requests.get("http://localhost/guerillalogisticsapi/MachineLearning/ClearGameRecommendations")

    for key, dict in todaysGameExamples.items():
        predictions = rec.getRecommendations(trainingGameExamples, key)

        payload = {}
        payload["key"] = key

        for pair in predictions:
            payload[pair[1]] = pair[0]

        r = requests.get("http://localhost/guerillalogisticsapi/MachineLearning/SaveGameRecommendation", params=payload)
        print(key)

    print("AdjustGameRecommendations")
    requests.get("http://localhost/guerillalogisticsapi/MachineLearning/AdjustGameRecommendations")
    # [print("%20s %s" % (key, dict)) for key, dict in results.items()]