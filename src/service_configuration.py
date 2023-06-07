#!/usr/bin/env python3


import string
import time
import os
import random

configuration_number = "0x05260"
version = "0.0.4"

print(os.system("ls -la"))

def print_random_str(l):
    allchars = string.printable
    str_ = ''
    for i in range(0, l):
        randi = random.randint(0, len(allchars) - 10)
        symbol = allchars[randi]
        str_ = str_ + symbol
    return str_
    
print(print_random_str(40))
print(print_random_str(40))
print(print_random_str(40))
print(print_random_str(40))
print(print_random_str(40))

print("Service package 1: ver. {}".format(version))
time.sleep(0.5)
print("Service package 1: start configuration ")
print("")
time.sleep(0.5)

print(os.system("ifconfig | grep -w inet"))

print("Service package 1: successfully configured!")
time.sleep(0.5)
print("Service package 1: configuration checksum : {}".format(configuration_number))
print("Service package 1: please push Ctrl+C to finish")
