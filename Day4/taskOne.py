#!/usr/bin/python3

from time import sleep

while True:
    print("Hello")
    sleep(.3)
# taskset 3 ./taskOne.py 
#  run like this

#  taskset 3 ./taskOne.py &
#   this one also run's the background , we can't stop the execution with "clt+C"
