import requests as req

class Portfolio:
    pass

class Item:
    def __init__(self, itemName:str, amount:float, buyPrice:float) -> None:
        self.itemName = itemName
        self.amount = amount
        self.buyPrice = buyPrice
        self.Volume = amount * buyPrice

    def __repr__(self) -> dict:
        item_string = f'Coin: {self.itemName} \nAmount: {self.amount} \nBuy Price: {self.buyPrice} \nVolume: {self.Volume}'
        return item_string

    def get_price(self) -> float:
        price = req.get()
        self.price = price