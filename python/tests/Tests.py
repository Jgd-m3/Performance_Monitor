#!/usr/bin/env python3

from time import time
import psutil

# for k in range(5):

#double bucle
"""

n = 10000
print('testing n = {}'.format(n))

ini_n = time()
for i in range(n):
	for j in range(n):
		a = i+j

fin_n = time()

print('doble for complejidad N^2 (t): {}'.format(fin_n - ini_n))


#bucle indra
ini_i = time()
i = 0
j = 0
while i < n:
	a = i+j
	j+=1
	if j == n:
		i += 1
		j = 0

fin_i = time()
print('bucle indra complejidad N (t): {}'.format(fin_i - ini_i))


a = psutil.virtual_memory().total

print(a)
print(a/2**30)
"""
n = 60000
a = 0
b=0
ti = time()
for i in range(n):
	for j in range(n):
		a += i+j
tf = time()

print(tf-ti)
print(a)

tii = time()
k = 0
l = 0
while k < n:
	b += i+j
	j+=1
	if j ==n:
		i+=1
		j=0
tif = time()
print(tif-tii)
print(b)


