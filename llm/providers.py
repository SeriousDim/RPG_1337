from dataclasses import dataclass

from dotenv import load_dotenv
load_dotenv()

import os

@dataclass
class Provider:
    name: str
    base_url: str
    api_key: str


PROVIDERS = {
    "proxy_api": Provider(
        "proxy_api",
        "https://api.proxyapi.ru",
        os.environ["PROXY_API_KEY"]
    ),
    "router_ai": Provider(
        "router_ai",
        "https://routerai.ru/api/v1",
        os.environ['ROUTER_AI_API_KEY']
    )
}
