import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import csv

p = np.array(pd.read_csv('data.csv'))

w, b = 1.0, 1.0 #初期値
a = 10**-7 #学習率	
n = 0 

s_x2 = sum(np.power(p[:, 0], 2))
s_y2 = sum(np.power(p[:, 1], 2))
s_xy = sum(p[:, 0]*p[:, 1])
s_x = sum(p[:, 0])
s_y = sum(p[:, 1])
N = len(p)

def E(w, b):
	E = s_y2 + w**2 * s_x2 + N*b**2 -2*w*s_xy +2*w*b*s_x -2*b*s_y
	return E

def Ew(w, b): #dE/dw
	
	return 2*w*s_x2 -2*s_xy + 2*b*s_x 

def Eb(w, b): #dE/db
	
	return -2*s_y + 2*w*s_x +2*b*N


res = np.array([[n, E(w, b)]]) #結果格納用
while (abs(Ew(w, b)) > 0.01 or abs(Eb(w, b)) > 0.005):#終了条件)
	w = w -a* Ew(w, b) #wを更新
	b = b - a* Eb(w, b) #bを更新
	n += 1
	if n%1000 == 0: #nを1000ごとにEを記録
		res = np.append(res, np.array([[n, E(w, b)]]), axis = 0)

w0, b0 = 0.5, 0.4 #真のw, b
print('n = ', n)
print('w = ', w, '相対誤差:', abs(w-w0)/w0)
print('b = ', b, '相対誤差:', abs(b-b0)/b0)

with open('E-n.csv', 'w') as file:
	w = csv.writer(file, lineterminator = '\n')
	w.writerow(['n', 'E'])
	w.writerows(res)







