"""
SOCKS5 proxy example using B2Proxy.
Requires the 'requests[socks]' package: pip install requests[socks]
"""

import requests

SOCKS5_PROXY = "socks5://username:password@your-proxy-gateway.com:1080"

def fetch_with_socks5(url):
    proxies = {
        "http": SOCKS5_PROXY,
        "https": SOCKS5_PROXY,
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

if __name__ == "__main__":
    result = fetch_with_socks5("https://httpbin.org/ip")
    if result:
        print(f"Exit IP: {result.get('origin')}")
