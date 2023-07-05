#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import string
import time
import os
import random
import tqdm

configuration_number = "1xM18650"
version = "1.0.0"

print(os.system("ls -la"))

def print_random_str(l):
    for i in range(l):
        char = chr(random.randint(32, 126))
        print(char, end='', flush=True)
        time.sleep(0.03)
    
    return (' ')

#print(print_random_str(40))
#print(print_random_str(40))
#print(print_random_str(40))
#print(print_random_str(40))
#print(print_random_str(40))

print("Service package 1: ver. {}".format(version))
time.sleep(0.5)
print("Service package 1: start configuration ")
time.sleep(0.5)

for i in tqdm.tqdm(range(3000), ascii=True, desc="System check"):
    time.sleep(0.001)

print("")
print(os.system("ifconfig | grep -w inet"))

print("Service package 1: successfully configured!")
time.sleep(0.5)
print("Service package 1: configuration checksum : {}".format(configuration_number))
print("Service package 1: please push Ctrl+C to finish")
