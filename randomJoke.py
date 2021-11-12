from os import read
import requests
response = requests.get("https://api.kanye.rest")
print("Wanna hear a random Kanye quote? (Y/N)")
responseJoke = input()
if "Y" in responseJoke or "y" in responseJoke:
    print(response.json()['quote'])
else:
    print("Ok fine, maybe next time")