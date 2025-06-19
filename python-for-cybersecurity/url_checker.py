# URL Inspection Tool to check for suspicious elements

from urllib.parse import unquote

def check_url(url):
    decoded = unquote(url)
    suspicious = ["@", "bit.ly", "tinyurl", "%20", "javascript:", "//"]

    print("Decoded URL:", decoded)
    for item in suspicious:
        if item in decoded:
            print(f"⚠️ Suspicious pattern found: {item}")

# User input
url = input("Enter a URL to check: ")
check_url(url)
