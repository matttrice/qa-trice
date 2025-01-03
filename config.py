import os

# Setup to potentially use different environments
ENV = os.getenv("TEST_APP_ENV", "consumer")

header = {
    "buy_crypto": "Buy crypto",
}

url_paths = {
    "consumer": {
        "home": "/c",
        "portfolio": "/c/portfolio",
        "explore": "c/explore",
        "transactions": "/c/transactions/history"
    }
}

def get_header(name:str):
    return header[name]

def get_url(name:str):
    return url_paths[ENV][name]