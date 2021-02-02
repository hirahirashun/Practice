import random 
import numpy as np
import csv

N = 100 #データ数100
w = 0.5 #真のw
b = 0.4 #真のb
p = np.empty((0, 2)) #データ格納用
for i in range(N):
	x = random.uniform(0, 10) 
	y = w*x + b + random.uniform(-0.8, 0.8) #δ < |0.2|の乱数付与
	p = np.append(p, np.array([[x, y]]), axis = 0) 

p = p[np.argsort(p[:, 0])] #座標の並び替え

with open('data2.csv', 'w') as file:
	w = csv.writer(file, lineterminator = '\n')
	w.writerow(['x', 'y'])
	w.writerows(p)




