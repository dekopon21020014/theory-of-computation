#!/usr/bin/env python3
import sys #パイプでcatから受け取るため

white_space = ' '

data = sys.stdin.read() # catの結果をパイプで受け取る
data = data.split('\n') # 行ごとに区切って配列にする

num_state = (data[0].split(white_space))[0] #状態数
num_state = int(num_state)

delta = [] #状態遷移関数を定義と同じく２次元配列で表現する
for i in range(num_state):
    delta.append(data[2+i].split(white_space))

sigma = list(data[1]) #入力の２行目を1文字ずつ配列の要素にする

word = data[-2] #入力文字列
current_state = data[-5] #現在の状態
final_state = (data[-4]).split(white_space) #受理状態の配列

for symbol in word: #入力文字列の文字数回繰り返す
    i = current_state
    j = sigma.index(symbol)
    current_state = delta[int(i)-1][int(j)]

if current_state in final_state: #現在状態が受理状態か
    print('Yes')
else:
    print('No')