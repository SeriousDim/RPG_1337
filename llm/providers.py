from dataclasses import dataclass

from dotenv import load_dotenv
load_dotenv()

import os

@dataclass
class Provider:
    base_url: str
    api_key: str


PROVIDERS = {
    "proxy_api": Provider(
        "https://api.proxyapi.ru",
        os.environ["PROXY_API_KEY"]
    ),
    "routerai": Provider(
        None,
        None
    )
}
