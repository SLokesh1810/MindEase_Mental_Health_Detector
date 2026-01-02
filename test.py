import requests
import random

# Flask API URL
url = "https://vf6z1px8-5000.inc1.devtunnels.ms/predict"

def testcase_generation(num_features=6):
    """Generate random test data with correct feature length"""
    return [random.randint(0, 3) for _ in range(num_features)]

for i in range(6):
    testcase = testcase_generation()

    payload = {"features": testcase}

    try:
        response = requests.post(url, json=payload, timeout=10)
        print("\nTestcase:", testcase)
        print("Status Code:", response.status_code)

        # Try parsing JSON safely
        try:
            print("Response:", response.json())
        except requests.exceptions.JSONDecodeError:
            print("Response is not JSON:", response.text)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
