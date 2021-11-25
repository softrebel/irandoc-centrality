from igraph import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

g = Graph.Read_GraphML('teimourpour_tags_without_zero_degrees.graphml')

centralities = {
    'Degree': g.degree(),
    'Closeness': g.closeness(),
    'Betweenness': g.betweenness(),
    'EigenVector': g.eigenvector_centrality(),
}
centality_names = list(centralities.keys())
for centrality in centality_names:
    i_index = centality_names.index(centrality)
    for j in range(i_index + 1, len(centality_names)):
        regr = linear_model.LinearRegression()
        other_centrality = centality_names[j]
        x = centralities[centrality]
        y = centralities[other_centrality]
        x_set = np.asanyarray(x).reshape(-1, 1)
        y_set = np.asanyarray(y)
        train_x, test_x, train_y, test_y = train_test_split(x_set, y_set, test_size=0.2)
        regr.fit(train_x, train_y)
        print(f"{centrality}_{other_centrality}")
        # Pearson correlation
        r = np.corrcoef(x, y)
        print('Pearson Correlation')
        print(r[0, 1])
        # The coefficients

        print('Coefficients: ', regr.coef_)
        print('Intercept: ', regr.intercept_)
        # plt.scatter(train_x, train_y, color='blue')
        # plt.plot(train_x, regr.coef_[0] * train_x + regr.intercept_, '-r')
        # plt.xlabel(centrality)
        # plt.ylabel(other_centrality)
        # plt.savefig(f"{centrality}_{other_centrality}.png")
        # plt.show()
        predicted_y = regr.predict(test_x)

        # mean absolute error (MAE)
        print('MAE', np.mean(np.absolute(test_y - predicted_y)))
        # MSE
        print('MSE', np.mean((test_y - predicted_y) ** 2))
        # R2
        print('R2', r2_score(test_y, predicted_y))
