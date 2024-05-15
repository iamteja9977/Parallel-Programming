#!/usr/bin/python3
import parsl
from parsl.app.app import bash_app
from parsl.configs.local_threads import config

parsl.load(config)
# parsl.load(config): Loads the Parsl configuration specified by the config object.
#  In this case, it configures Parsl to use the local execution environment with multiple threads.

@bash_app
# @bash_app: Decorator used to define a bash command as a Parsl app.
def myFun(stdout="fileOne.txt", stderr="fileTwo.txt"):
    return 'echo "Hello World!..."'

# Specifies the paths for the standard output and standard error streams of the bash command.
#  The output of the command will be redirected to fileOne.txt, and any error messages will be redirected to fileTwo.txt.

if __name__ == "__main__":
    print(f"res: {myFun().result()}")


'''
In Parsl, when a Bash app executes successfully, it returns 0,
 which typically signifies successful completion without any errors.
'''
# when you run the code
# ./myBash.py      
# res: 0

# with 2 files are created
# fileOne.txt and fileTwo.txt



'''

The folder /home/srtejaa/Desktop/2024/Parallel-Programming/Day5/Parsl/runinfo/000 is created because Parsl automatically generates a runinfo directory to store metadata related to the execution of Parsl apps.
 This directory is used to manage and track information about task execution, such as logs, task status, and other diagnostic information.
'''