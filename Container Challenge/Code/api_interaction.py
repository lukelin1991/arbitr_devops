import requests
from faker import Faker
from pprint import pprint

LOCAL_URL = "http://localhost:8000"

ENDPOINTS = [
    "/hello",
    "/user/add",
    "/user/retrieve/"
]

def generate_random_data():
    fake = Faker()
    return {
        "username": fake.user_name(),
        "email": fake.email(),
        "full_name": fake.name()
    }

USERLIST = [] # creating a "userlist" to hold the usernames that are created.

#basic interaction for each endpoint in all TestAPIs
def api_interaction():
    for endpoint in ENDPOINTS:
        if endpoint == "/user/add":
            user_data = generate_random_data()
            USERLIST.append(user_data["username"])
            response = requests.post(LOCAL_URL + endpoint, json=user_data)

        elif endpoint == "/user/retrieve/":
            for username in USERLIST:
                response = requests.get(LOCAL_URL + endpoint + username)
                
        else:
            response = requests.get(LOCAL_URL + endpoint)
        
        if response.status_code == 200:
            print(f"Request to {endpoint} successful:")
            pprint(response.json())
        else:
            print(f"Failed to make request to {endpoint}.  Status code: {response.status_code}")

if __name__ == "__main__":
    api_interaction()