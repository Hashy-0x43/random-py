import requests

n = input("Pick Filename: ")
file = open(n,"w")

r = input("URL: ")
r = requests.get(r)
r = r.text

file.write(r + "\n")
file.close()
