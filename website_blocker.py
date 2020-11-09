# You have to run this code in administrator mode
# open your py IDE in administrator mode and the run the code
import time
from datetime import datetime as dt

# Windows host file path
hostpath = r"c:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1" # local host/server

websites = ["www.facebook.com"]# Add the website you want to block ,you can add more website

while True:
    # Give the time duration ,Example 7pm(19) to 8pm(20)
    if dt(dt.now().year,dt.now().month,dt.now().day,19) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("Website is Blocked")
        with open(hostpath,'r+') as file:
            data=file.read()
            for website in websites:
                if website in data:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(hostpath,'r+') as file:
            data=file.readlines()
            file.seek(0)
            for line in data:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()   # truncate the file size
        print("Website is Unblocked")
    time.sleep(120)  # The loop will stop for 2 minutes

     
