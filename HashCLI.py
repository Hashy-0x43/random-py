# Python v3.9.0

from hashlib import md5, sha1, sha256, sha512
from sys import argv
from datetime import date
today = date.today()
from datetime import datetime
now = datetime.now()

if argv[1] == "--md5":
    algorithm = "MD5"
    result = (md5(argv[2].encode()).hexdigest())

if argv[1] == "--sha1":
    algorithm = "SHA1"
    result = (sha1(argv[2].encode()).hexdigest())

if argv[1] == "--sha256":
    algorithm = "SHA256"
    result = (sha256(argv[2].encode()).hexdigest())

if argv[1] == "--sha512":
    algorithm = "SHA512"
    result = (sha512(argv[2].encode()).hexdigest())

else:
    print("pythonX HashCLI.py --<algorithm> <text> <Y/N>\nLast parameter is for whether you want to save the output or not.")
    exit()

output = f"[{argv[2]}] in [{algorithm}] is [{result}]."

print(output)

if argv[3] == 'Y' or argv[3] == 'y':
    file = open("hash_data.txt","a")
    file.write((today.strftime("%m/%d/%Y")) + " " + (now.strftime("%H:%M:%S")) + "\n")
    file.write(output + "\n")
    file.close()

if argv[3] == 'N' or argv[3] == 'n':
    exit()
