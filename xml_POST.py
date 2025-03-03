import requests

# URL where you want to send the XML
url = "https://crypto.com/cdn-cgi/trace"

# XML data
xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<trace>
  <fl>719f66</fl>
  <h>crypto.com</h>
  <ip>2600:1004:a02c:41ef:8c0c:78ae:ba2e:b66b</ip>
  <ts>1740093358.309</ts>
  <visit_scheme>https</visit_scheme>
  <uag>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15</uag>
  <colo>ATL</colo>
  <sliver>none</sliver>
  <http>http/3</http>
  <loc>US</loc>
  <tls>TLSv1.3</tls>
  <sni>plaintext</sni>
  <warp>off</warp>
  <gateway>off</gateway>
  <rbi>-1</rbi>
  <kex>X25519</kex>
</trace>"""

# Headers to indicate XML content
headers = {
    "Content-Type": "application/xml"
}

# Send POST request
response = requests.post(url, data=xml_data, headers=headers)

# Print response
print("Response Code:", response.status_code)
print("Response Body:", response.text)