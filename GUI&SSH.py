"""
Christian and Evan
Web File Exploit Test Tool
1)Have a list of URLS to run through. in a file with 1 url per line
2)Use the GET response to see the data and type.Save data to another file.
3)Be able to pull the output of the GET response and edit it, then submit it back to the server.
4)Check to see if it worked. Via the terminal for python

"""

import os
import requests

def processURL(url, index):

    path = "responses/" + str(index)

    if not os.path.exists(path):

        response = requests.get(url)
        os.makedirs(path)

        print("Processing: " + str(index) + " " + url + " " + str(response.status_code) + " " + response.headers['Content-Type'])

        with open(path + "/response.txt", "w") as file:
            file.write(response.text)

        with open(path + "/headers.txt", "w") as file:
            file.write(str(response.headers))

        with open(path + "/status.txt", "w") as file:
            file.write(str(response.status_code))
    else:
        print("Skipping: " + str(index) + " " + url)



url_file = open("urls.txt", "r")
index = 1

for line in url_file:
    processURL(line, index)
    index += 1



