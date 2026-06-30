import requests

# URL of the Wisecow application
URL = "http://192.168.49.2:30449"

def check_application():
    try:
        response = requests.get(URL, timeout=5)

        if response.status_code == 200:
            print("Application Status : UP")
            print(f"HTTP Status Code  : {response.status_code}")
        else:
            print("Application Status : DOWN")
            print(f"HTTP Status Code  : {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Application Status : DOWN")
        print("Reason:", e)

if __name__ == "__main__":
    check_application()
