from os import read
import requests
response = requests.get("https://api.humorapi.com/jokes/random?api-key=b1b245f440084a3bba61f5b82aa0923b")
print("Wanna hear a joke? (Y/N)")
responseJoke = input()
if "Y" in responseJoke or "y" in responseJoke:
    joke = response.json()['joke']
    print(joke)
else:
    print("Ok fine, no jokes :(")