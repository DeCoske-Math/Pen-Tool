import requests
import json
from bs4 import BeautifulSoup
import os.path

url_list = []


def simple_crawler(url):
    if url.endswith("/"):
        url = url[:-1]

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error if the request fails
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return

    content_type = response.headers.get("Content-Type", "").lower()

    if "html" in content_type or "xml" in content_type:
        # Parse HTML/XML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")  # or "lxml" for XML
        data = soup.prettify()

        print(f"\nURLs found on {url}:\n")

        for link in soup.find_all("a", href=True):
            sub_url = link["href"]
            if sub_url.startswith("/"):
                sub_url = f"{url}{sub_url}"
            print(f"{sub_url}\n")
            url_list.append(f"{sub_url}\n")

    elif "json" in content_type:
        # Parse JSON response
        try:
            data = response.json()  # If the response is valid JSON
        except json.JSONDecodeError:
            data = json.loads(response.text)  # Fallback method

    elif "text" in content_type:
        # Handle plain text
        data = response.text.strip()

    elif "octet-stream" in content_type or "binary" in content_type:
        # Handle binary data
        data = response.content  # Binary content (e.g., files, images, etc.)

    elif "http" in content_type:
        # Handle HTTP response body separately if needed
        data = response.text  # Assuming text format, modify as needed

    else:
        # Default case: Unknown content type
        data = response.content  # Fallback to raw content

    return data  # Return data instead of just printing it


# Get user input for multiple URLs
urls = input("Enter URLs separated by commas: ").split(",")
# urls = ["https://crypto.com/"]

# Strip spaces and crawl each URL
for url in [u.strip() for u in urls]:
    simple_crawler(url)

if os.path.isfile("urls.txt"):
    with open("urls.txt", "r") as url_file:
        for line in url_file:
            url_list.append(line.strip())

# remove duplicates
url_list = list(set(url_list))

with open("urls.txt", "w") as url_file:
    url_file.writelines(url_list)
