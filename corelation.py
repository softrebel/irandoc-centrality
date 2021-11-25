import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from igraph import *

g = Graph.Read_GraphML('teimourpour_tags.graphml')
betweenness = g.betweenness()
closeness = g.closeness()
degree = g.degree()
eigenvector = g.eigenvector_centrality()
centrality = {
    'Degree': degree,
    'EigenVector': eigenvector,
    'Closeness': closeness,
    'Betweenness': betweenness
}

keys = list(centrality.keys())
for i in keys:
    index = keys.index(i)
    for j in range(index+1, len(keys)):
        jindex=keys[j]
        x = centrality[i]
        y = centrality[jindex]
        plt.scatter(x, y, color='blue')
        plt.xlabel(i)
        plt.ylabel(jindex)

        from sklearn import linear_model
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import r2_score
        regr = linear_model.LinearRegression()
        x = np.asanyarray(x).reshape(-1, 1)
        y = np.asanyarray(y)
        train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2)
        regr.fit (train_x, train_y)
        print(f"{i}_{jindex}")
        print ('Coefficients: ', regr.coef_)
        print ('Intercept: ',regr.intercept_)
        plt.plot(train_x, regr.coef_[0]*train_x + regr.intercept_, '-r')
        test_y_ = regr.predict(test_x)
        print("R2-score: %.2f" % r2_score(test_y , test_y_) )
        plt.savefig(f"{i}_{jindex}.svg")
        plt.show()

#
#
# plt.scatter(closeness, eigenvector,  color='blue')
# plt.xlabel("Closeness")
# plt.ylabel("Eigenvector")
# # plt.savefig("1.svg")
# plt.show()
# plt.scatter(degree, eigenvector,  color='blue')
# plt.xlabel("Degree")
# plt.ylabel("Eigenvector")
# # plt.savefig("1.svg")
# plt.show()
# plt.scatter(betweenness, eigenvector,  color='blue')
# plt.xlabel("Betweenness")
# plt.ylabel("Eigenvector")
# # plt.savefig("1.svg")
# plt.show()
# plt.scatter(betweenness, degree,  color='blue')
# plt.xlabel("Betweenness")
# plt.ylabel("Degree")
# # plt.savefig("1.svg")
# plt.show()
# plt.scatter(betweenness, closeness,  color='blue')
# plt.xlabel("Betweenness")
# plt.ylabel("Closeness")
# # plt.savefig("2.svg")
# plt.show()
# plt.scatter(degree, closeness,  color='blue')
# plt.xlabel("Degree")
# plt.ylabel("Closeness")
# plt.show()
# # plt.savefig("3.svg")
# plt.show()
#
#
# from sklearn import linear_model
# from sklearn.metrics import r2_score
# regr = linear_model.LinearRegression()
# regr.fit (train_x, train_y)
# # The coefficients
# print ('Coefficients: ', regr.coef_)
# print ('Intercept: ',regr.intercept_)
# plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
# plt.xlabel("Engine size")
# plt.ylabel("Emission")
