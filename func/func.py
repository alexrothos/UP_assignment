from config import Config
import requests

def reach_for_data():
    url = Config.data_url

    headers = {
        "Authorization": "Basic dXNlcjI6Z1JkMnZQVXR6M2ZqYnJ2WQ=="
    }

    data = requests.get(url, headers=headers)

    if data.status_code == 200:
        return data.json()
    else:
        return None