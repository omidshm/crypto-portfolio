from apiclient import coingecko
from prettytable import PrettyTable

class Portfolio:
    def __init__(self) -> None:
        self.items = []
    
    def help():
        help_lines_list = [
            'Welcome to Crypto Portfolio Manager App',
            'here is methods you can call:',
            '...'
        ]
        return '\n'.join(help_lines_list)
    
    def __repr__(self):
        return 'portfolio object'
    
    def add_item(self, itemName:str, amount:float, buyPrice:float):
        self.items.append(Item(itemName, amount, buyPrice))

    @property
    def items_list(self):
        if self.items == []:
            return 'Portfolio its clean. Lets add an item'
        else:
            result_no_price = []
            item_names = []
            for item in self.items:
                item_name = item.item_statics['symbol']
                item_names.append(item_name)
                result_no_price.append(item.item_statics)
            
            prices = coingecko().get_batch_price_dict(item_names)

            result = []
            for item in result_no_price:
                item['current_price'] = prices[item['symbol']]
                result.append(item)
            
            return result

    
    def portfo_table(self):pass



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
        item_dict = {
            'symbol':self.itemName,
            'amount':self.amount,
            'buy_price':self.buyPrice,
            'volume':self.Volume
        }
        return item_dict