#!/usr/bin/env python3
import sys

data = sys.stdin.read()
data = data.split('\n')

num_state = (data[0].split(' '))[0]
num_state = int(num_state)

delta = []
for i in range(num_state):
    delta.append(data[2+i].split(' '))

sigma = []
for i in data[1]:
    sigma.append(i)

word = data[-2]
current_state = data[-5]
final_state = (data[-4]).split(' ')

for symbol in word:
    i = current_state
    j = sigma.index(symbol)
    current_state = delta[int(i)-1][int(j)]

if current_state in final_state:
    print('Yes')
else:
    print('No')