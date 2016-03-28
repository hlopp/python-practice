#!/usr/bin/python
import operator

list_ip = []
result = dict()
with open('access.log') as f:
    lines = f.readlines()
    for line in lines:
        ind = line.find(' ')
        if ind == -1: continue
        ip = line[:ind]
        if ip in result: 
            result[ip]+=1
        else:
            result[ip]=1

sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
for i in range(0,9):
    if i < len(sorted_result) :
        print(sorted_result[i][0])
    else:
        break
    

print(sorted_result)



