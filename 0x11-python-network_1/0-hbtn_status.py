import urllib.request

# URL to fetch
url = "https://alx-intranet.hbtn.io/status"

# Fetch the URL using urllib
with urllib.request.urlopen(url) as response:
    # Read the response content
    content = response.read()

    # Display information about the response
    print("Body response:")
    print(f"    - type: {type(content)}")
    print(f"    - content: {content}")
    print(f"    - utf8 content: {content.decode('utf-8')}")
