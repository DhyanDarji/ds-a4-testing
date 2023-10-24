import requests
import time

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
        x = requests.get(f"http://www.localhost:4567{getPath}", headers=self.getHeader)
        endTime = time.time()
        return (x, endTime)
    
    def putRequest(self, data):
        startTime = time.time()
        self.putHeader['Content-Length'] = len(data)
        x = requests.put(f"http://www.localhost:4567/weather.json", headers=self.putHeader, data=data)
        endTime = time.time()
        return (x, endTime)





