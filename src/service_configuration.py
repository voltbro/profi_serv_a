#!/usr/bin/env python3


import string
import time
import os

configuration_number = 0x00015
version = "0.0.2"

print(os.system("ls -la"))


print("Service package 1: ver. {}".format(version))
time.sleep(0.5)
print("Service package 1: start configuration ")
time.sleep(0.5)

print(os.system("ifconfig | grep -w inet"))

print("Service package 1: successfully configured!")
time.sleep(0.5)
print("Service package 1: configuration checksum : {}".format(configuration_number))
print("Service package 1: please push Ctrl+C to finish")
