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

def processURL(url, index, log):

    # put all responses in dedicated folder and inside of that folder index numbers match the urls.txt line numbers
    path = "responses/" + str(index)

    # skip url if folder of index exists, delete/move folder to refresh data
    if not os.path.exists(path):

        response = requests.get(url)
        os.makedirs(path)

        print("Processing: " + str(index) + " " + str(response.status_code) + " " + response.headers.get('Content-Type', 'Unknown') + " " + url, end="")
        log.write(str(index) + "\t" + str(response.status_code) + "\t" + response.headers.get('Content-Type', 'Unknown') + "\t" + url)

        with open(path + "/content-type.txt", "w") as file:
            file.write(response.headers.get('Content-Type', 'Unknown'))

        with open(path + "/response.txt", "w") as file:
            file.write(response.text)

        with open(path + "/headers.txt", "w") as file:
            file.write(str(response.headers))

        with open(path + "/status.txt", "w") as file:
            file.write(str(response.status_code))
    else:
        print("Skipping:   " + str(index) + " " + url, end="")



url_file = open("urls.txt", "r")
log = open("log.tsv", "a")
index = 1

# index matches line number in urls.txt
for line in url_file:
    processURL(line, index, log)
    index += 1

log.write("\n")



