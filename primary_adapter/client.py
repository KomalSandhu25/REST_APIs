
import requests
import domain.HomeState as homeState
class HomeStateApiClient:

    def __init__(self, api_url):
        self.home_states = {}
        self.api_url = api_url

    def retrieve_home_state(self, home_id):
        url = self.api_url + home_id
        response = requests.get(url)
        try:
            if response.status_code == 200:
                data = response.json()
                home_state = homeState(data['ID'], data['State'], data['Occupied'])
                self.home_states[data['ID']] = home_state
                return home_state
            else:
                raise Exception("Failed to retrieve home state. Response code:", response.status_code)
        except Exception as e:
            print(e)
            return None


    def update_home_state(self, home_id, occupied):
        url = self.api_url + home_id
        payload = {"Occupied": occupied}
        response = requests.put(url, json=payload)
        try:
            if response.status_code == 200:
                self.home_states[home_id].occupied = occupied
                print("Home state updated successfully")
            else:
                raise Exception("Failed to update home state. Response code:", response.status_code)
        except Exception as e:
            print(e)
            return None

def main():
    api_url = "https://example.com/api/home/"
    client = HomeStateApiClient(api_url)

    # Retrieve home state
    home_id = "ID1"
    home_state = client.retrieve_home_state(home_id)
    print("Home state:", home_state)

    # Update home state
    client.update_home_state(home_id, "Y", "N")

