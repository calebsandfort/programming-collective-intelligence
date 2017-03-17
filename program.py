import recommendations

rownames, colnames, data = recommendations.readfile('TrainingGameExamplesSmall.csv')

print("{0}\n\n{1}\n\n{2}".format(rownames, colnames, data))