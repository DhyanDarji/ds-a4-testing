import requestSender as rs
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

class Experiment_2: 
    def __init__(self):
        self.requestToDelay = {}
        self.rs = rs.RequestSender()
        self.data = open(f"test_files/data_1.txt").read()
    def run(self, none):
        response = self.rs.putRequest(self.data)
        return response[1]


def main(requests):
    test = Experiment_2()
    res = []
    with ThreadPoolExecutor(requests) as pool:
        res.append(list(pool.map(test.run, [None]*requests))) 
    return np.mean(res)
        
print(main(1))
print(main(100))
print(main(1000))
print(main(10000))
print(main(100000))
print(main(1000000))

