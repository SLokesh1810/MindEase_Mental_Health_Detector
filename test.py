import requests
import random
import time
import sys

url = "http://localhost:5000/predict"

def testcase_generation(num_features=6):
    return [random.randint(0, 3) for _ in range(num_features)]

# wait for flask to start
time.sleep(2)

# First, check if the app is up
try:
    health_check = requests.get("http://localhost:5000", timeout=5)
    print(f"Health check status: {health_check.status_code}")
except requests.exceptions.ConnectionError as e:
    print(f"ERROR: Cannot connect to app at http://localhost:5000")
    print(f"Connection error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: Health check failed: {e}")
    sys.exit(1)

for i in range(5):
    testcase = testcase_generation()
    payload = {"features": testcase}

    try:
        response = requests.post(url, json=payload, timeout=5)
    except requests.exceptions.ConnectionError as e:
        print(f"ERROR: Cannot connect to app: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Request failed: {e}")
        sys.exit(1)

    print("Testcase:", testcase)
    print("Status:", response.status_code)

    assert response.status_code == 200
    assert "prediction" in response.json()

print("All API tests passed")