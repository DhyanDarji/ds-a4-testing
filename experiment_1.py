
import requestSender as rs
import time
import json

class Experiment_1:
    def __init__(self):
        self.count = 1
        self.rs = rs.RequestSender()
    def readDataJson(self, folder, filePath):
        f = open(f"{folder}/{filePath}")
        return f.read()
    def test_get(self, test_type, path, expected_output):
        rs = self.rs.getRequest(path)
        response = rs[0].text
        if expected_output not in response:
            print(f"{test_type} {self.count}: Failed")
            print(response)
        else:
            print(f"{test_type} {self.count}: Passed")
        self.count +=1
    def run_Test(self, data, test_type, getPath, expected_output):
        d = self.readDataJson("test_files_2",data)
        s = self.rs.putRequest(d)
        time.sleep(1)


        response = self.rs.getRequest(getPath)[0].text


        if expected_output not in response:
            print(f"{test_type} {self.count}: Failed")
        else:
            print(f"{test_type} {self.count}: Passed")
        self.count +=1

if __name__ == "__main__":
    test = Experiment_1()
    test.test_get("No Data", "/weather.json", "Not Found!")
    test.run_Test("data_1.txt", "PUT/GET No ID", "/weather.json", "IDS60901")
    test.run_Test("data_9.txt", "PUT/GET ID", "/weather.json?stationid=IDS61111", "Wagga")
    test.run_Test("data_5.txt", "PUT/GET Invalid Metadata", "/weather.json?stationid=IDS23441", "The data you have requested does not exist on server")
