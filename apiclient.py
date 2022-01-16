import requests as req

class iClient:
    def __init__(self) -> None:
        pass

    def get_price(self) -> float: pass
    
    def get_mcap(self) -> list:pass

class coingecko(iClient):
    def __init__(self) -> None:
        self.coins = req.get("https://api.coingecko.com/api/")