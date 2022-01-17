from apiclient import coingecko

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

    @property
    def price(self):
        price = coingecko().get_price(self.itemName)
        return price

    @property
    def item_statics(self):
        return [self.itemName,self.amount,self.buyPrice,self.Volume]