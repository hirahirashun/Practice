import pandas as pd
import numpy as np

p = np.array(pd.read_csv('data2.csv'))

N = len(p)
s_x = sum(p[:, 0]) #x座標の和
s_y = sum(p[:, 1]) #y座標の和
s_xy = sum(p[:, 0]*p[:, 1]) #x, y座標の積の和
s_x2 = sum(np.power(p[:, 0], 2)) #x座標の二乗の和

#連立方程式の求解
#前進消去
def foward_erase(a): 
	for i in range(len(a)):
		swap_max(a, i) #絶対値が大きい係数の式と交換
		f1 = a[i][i]
		for j in range(len(a[i])):
			a[i][j] = a[i][j]/f1 #i番目の式のi番目の係数を1にする
		for k in range(i + 1, len(a)):
			f2 = a[k][i]
			for l in range(len(a[k])):
				#k番目の式のi番目の変数を消去
				a[k][l] = a[k][l] - f2*a[i][l] 

def swap_max(a, i):
	m = i
	for j in range(i + 1, len(a)):
		#絶対値の最大値を求める
		if abs(a[m][i]) < abs(a[j][i]):
			m = j
	#交換
	temp = a[i]
	a[i] = a[m]
	a[m] = temp


#後退代入				
def back_substitution(a):
	n = len(a[0]) - 1 
	r = np.empty(n) #結果格納用
	r[n - 1] = a[n - 1][n] #n番目の変数の解
	if (n >  1):
		for i in range(n - 1):
			#n - 1番目から順に代入
			r[n - i - 2] = a[n - i - 2][n] 
			for j in range(n - i - 1, n):
				r[n -i - 2] -= r[j]*a[n -i - 2][j]
	return r
	
def solve_linear(a):
	foward_erase(a)
	return back_substitution(a)

#係数代入
F = np.array([[s_x2, s_x, s_xy], [s_x, N, s_y]])
w, b = solve_linear(F) #求めたw, b
w0, b0 = 0.5, 0.4 #真のw, b

print('w = ', w, '相対誤差:', abs(w-w0)/w0)
print('b = ', b, '相対誤差:', abs(b-b0)/b0)







