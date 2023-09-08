import requests
import random
#Requests - libraries that lets you query websites
#Random - generate random numbers

r = requests.get("http://172.25.0.20/")
#Response is the variable that gets the webpage

randomnumber = random.randint(1,1000)
#Randomnumber is a variable that finds a random number between 1-1000

while True:
    response = requests.get("http://172.25.0.20?guess=" + str(randomnumber))
    pagetext = response.text
    if "wrong!" not in pagetext:
        print(pagetext)
        print(pagetext)("http://172.25.0.20?guess=" + str(randomnumber))
