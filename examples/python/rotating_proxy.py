"""
Rotating proxy example using B2Proxy.
Each request uses a different exit IP (rotating session).
Replace the placeholder with your actual proxy credentials.
"""

import requests

# Replace with your proxy gateway, username, and password
PROXY_URL = "http://username:password@your-proxy-gateway.com:8080"

def fetch_with_rotating_proxy(url):
    proxies = {
        "http": PROXY_URL,
        "https": PROXY_URL,
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

if __name__ == "__main__":
    # Test the proxy by checking the exit IP
    result = fetch_with_rotating_proxy("https://httpbin.org/ip")
    if result:
        print(f"Exit IP: {result.get('origin')}")
