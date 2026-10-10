"""
Sticky session example using B2Proxy.
Maintains the same exit IP for a period of time (sticky session).
Useful for tasks that need session continuity, such as pagination or login.
"""

import requests

PROXY_URL = "http://username:password@your-proxy-gateway.com:8080"

def fetch_with_sticky_session(url):
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
    for i in range(3):
        result = fetch_with_sticky_session("https://httpbin.org/ip")
        if result:
            print(f"Request {i+1} - Exit IP: {result.get('origin')}")
