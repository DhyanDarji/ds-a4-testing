
import requestSender as rs
import time
import json

class Experiment_3:
    def __init__(self):
        self.count = 1
        self.rs = rs.RequestSender()
    def readDataJson(self, filePath):
        f = open(f"test_files/{filePath}")
        return f.read()

    def run_Test(self, data_1, data_2, test_type, getPath, expected_output):
        d_1 = self.readDataJson(data_1)
        d_2 = self.readDataJson(data_2)
        self.rs.putRequest(d_1)
        time.sleep(1)
        self.rs.putRequest(d_2)
        time.sleep(1)

        response = self.rs.getRequest(getPath)[0].text

        if expected_output not in response:
            print(f"{test_type} {self.count}: Failed")
        else:
            print(f"{test_type} {self.count}: Passed")
        self.count +=1

if __name__ == "__main__":
    test = Experiment_3()
    # data_1, data_2, test_type, getPath, expected_output
    test.run_Test("data_7.txt","data_6.txt", "PUT/GET New Data -> Old Data (ID)", "/weather?id=IDS60921", "Brisbane")

    test.run_Test("data_8.txt","data_9.txt", "PUT/GET Old Data -> New Data (No ID)", "/weather?id=", "Adelaide")

    test.run_Test("data_10.txt","data_11.txt", "PUT/GET Old Data -> New Data (ID)", "/weather?id=IDS61546", "Daz")


