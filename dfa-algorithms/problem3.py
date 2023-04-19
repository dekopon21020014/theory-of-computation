#!/usr/bin/env python3

# this is probrem3
# cd test/runner
# sh P2.sh ../../problem3.py

import sys

def read_input():
    # パイプでcatから受け取るため
    data = sys.stdin.read()
    # 行ごとに区切って配列にする
    data = data.split('\n')
    # 状態数
    num_state = int(data[0].split()[0])
    # 状態遷移関数を2次元配列で表現する
    delta = [data[2+i].split() for i in range(num_state)]
    # 入力の2行目を1文字ずつ配列の要素にする
    sigma = list(data[1])
    # 現在の状態(初期状態)
    current_state = data[-3]
    # 受理状態の配列
    final_states = data[-2].split()
    not_accept_states = []
    for i in range(1, num_state+1):
        if str(i) in final_states:
            continue
        else:
            not_accept_states.append(str(i))

    return num_state, delta, sigma, current_state, final_states, not_accept_states

def get_reachable_states(num_state, delta, current_state):
    marked_states = [current_state]
    index = 0
    while True:
        for state in delta[int(current_state)-1]:
            if state not in marked_states:
                marked_states.append(state)
        if index+1 < len(marked_states):
            index += 1
            current_state = marked_states[index]
        else:
            break
    return marked_states

#if __name__ != 'main':
num_state, delta, sigma, current_state, final_states, not_accept_states = read_input()
reachable_states = get_reachable_states(num_state, delta, current_state)
if any(x in reachable_states for x in not_accept_states):
    print('No')
else:
    print('Yes')