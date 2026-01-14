import requests
import random
import time

url = "http://localhost:5000/predict"

def testcase_generation(num_features=6):
    return [random.randint(0, 3) for _ in range(num_features)]

# wait for flask to start
time.sleep(2)

for i in range(5):
    testcase = testcase_generation()
    payload = {"features": testcase}

    response = requests.post(url, json=payload)

    print("Testcase:", testcase)
    print("Status:", response.status_code)

    assert response.status_code == 200
    assert "prediction" in response.json()

print("All API tests passed")