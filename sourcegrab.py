import requests
import sys

r = str(sys.argv[1])
n = str(sys.argv[2])

r = requests.get(r)
r = r.text

file = open(n,"w")

file.write(r + "\n")
file.close()