import requests 
from requests.adapters import HTTPAdapter
import time
import json

session = requests.Session()
adapter = HTTPAdapter(max_retries=100)

class RequestSender:
    def __init__(self):
        self.getHeader = {
            'User-Agent': 'ATOMClient/1/0',
            'Host': 'localhost:4567',
            'Accept': 'application/json',
            'Connection': 'close',
            'Content-Type': 'application/json',
        }

        self.putHeader = {
            'Host': 'localhost:4567',
            'User-Agent': 'ATOMClient/1/0',
            'Content-Type': 'application/json',
            'Content-Length': 'unknown'
        }

    def getRequest(self, getPath):
        startTime = time.time()
        x = requests.get(f"http://www.localhost:4567{getPath}", headers=self.getHeader, timeout=20)
        endTime = time.time()
        return (x, endTime)
    
    def putRequest(self, data):
        startTime = time.time()
        self.putHeader['Content-Length'] = str(len(data))
        x = requests.put(f"http://www.localhost:4567/weather.json", headers=self.putHeader, data=data, timeout=20)
        endTime = time.time()
        return (x, endTime-startTime)





