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

marked_state = []
current_state = data[-3] #現在の状態(初期状態)
final_state = (data[-2]).split(white_space) #受理状態の配列

marked_state.append(current_state)
index = 0
while True:
    #for dist_from_cur_state in delta[int(current_state)-1]:
    for state in delta[int(current_state)-1]:
        if state not in marked_state:
            marked_state.append(state)

    if index+1 < len(marked_state):
        index += 1
        current_state = marked_state[index]
    else:
        break

if any(x in marked_state for x in final_state):
    print('Yes')
else:
    print('No')
