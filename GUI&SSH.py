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
from datetime import datetime
import re

def sanitize_filename(url):
    return re.sub(r'[<>:"/\\|?*\n]', '_', url)  # Replace illegal filename characters

def write_size_limited(file, data):
    max_size = 1024 ** 3  # 1GB in bytes
    if len(data.encode('utf-8')) < max_size:
        file.write(data)
    else:
        file.write("Data exceeds 1GB and will not be written.\n")

def processURL(url, index, log):
    url = url.strip()  # Remove leading/trailing spaces or newlines
    filename = sanitize_filename(url) + ".txt"  

    if os.path.exists(filename):  # Skip if file already exists
        print(f"{'Skipping:':20} {index} {url}")
        return

    try:
        response = requests.get(url, timeout=4)
    except Exception as e:
        print(f"{(type(e).__name__+':'):20} {index} {url}")
        log.write(f"{datetime.now()}\t{index}\t0\t{type(e).__name__}\t{url}\n")
        return

    print(f"{'Processing:':20} {index} {response.status_code} {response.headers.get('Content-Type', 'Unknown')} {url}")
    log.write(f"{datetime.now()}\t{index}\t{response.status_code}\t{response.headers.get('Content-Type', 'Unknown')}\t{url}\n")

    with open(filename, "w") as file:
        file.write(f"URL: {url}\n")
        file.write(f"Status Code: {response.status_code}\n")
        file.write(f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}\n\n")
        file.write("Headers:\n")
        write_size_limited(file, str(response.headers) + "\n\n")
        file.write("Response Body:\n")
        write_size_limited(file, response.text)

with open("urls.txt", "r") as url_file, open("log.tsv", "a") as log:
    for index, line in enumerate(url_file, start=1):
        processURL(line, index, log)
    log.write("\n")  # Fix: Writing newline before log file closes


    """
    	•	Before making a request, the script checks if a file with the URL’s sanitized name already exists:
        
    if os.path.exists(filename):  # Skip if file already exists
    print(f"{'Skipping:':20} {index} {url}")
    return
    """
