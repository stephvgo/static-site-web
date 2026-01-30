import requests

API_URL = "https://g8vhsi4yyf.execute-api.us-east-1.amazonaws.com/dev/count"

def smoke_test():
    try:
        response = requests.post(API_URL, timeout=5)

        print("Status code:", response.status_code)

        if response.status_code != 200:
            print("API did not return status code 200")
            return

        data = response.json()

        if "count" not in data:
            print("Response missing 'count'")
            print(data)
            return

        print("Smoke test passed.")
        print("Visitor count is now:", data["count"])

    except Exception as e:
        print("Smoke test failed:", e)

if __name__ == "__main__":
    smoke_test()
