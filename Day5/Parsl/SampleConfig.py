#!/usr/bin/python3
import parsl
from parsl.app.app import python_app
from parsl.configs.local_threads import config

parsl.load(config)


@python_app
def myFun():
    return "Hello World"


if __name__ == "__main__":
    print(f"res: {myFun().result()}")

# chmod +x SampleConfig.py 
# [srtejaa@srtejaa-pc] ➜ Parsl (U! main) ./SampleConfig.py       
# res: Hello World


'''
import parsl: This imports the Parsl library itself. Parsl is a parallel scripting library in Python that simplifies the process of parallelizing applications across various execution environments, such as local machines, clusters, or cloud resources.
from parsl.app.app import python_app: This imports the python_app decorator from the app module within Parsl. The python_app decorator is used to define Python functions as Parsl apps, which can then be executed asynchronously in parallel.
from parsl.configs.local_threads import config: This imports the config object from the local_threads module within Parsl's configuration options. This specific configuration (local_threads) is tailored for running Parsl apps locally using multiple threads. It defines settings such as the number of threads to use for parallel execution.

'''