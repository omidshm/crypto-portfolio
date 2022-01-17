import requests as req

class iClient:
    def __init__(self) -> None:
        pass

    def get_price(self) -> float: pass
    
    def get_mcap(self) -> list:pass

    def get_1d_volume(self) -> list:pass

    def get_7d_volume(self) -> list:pass


class coingecko(iClient):

    _base_api = "https://api.coingecko.com/api/v3"

    def __init__(self) -> None:
        self.coins_list_response = req.get(self._base_api+"/coins/list").json()
        self._coins_id_dict = coingecko.organize_coins(self.coins_list_response)

    @staticmethod
    def organize_coins(coins_response:list) -> dict:
        coins = {}
        for item in coins_response:
            coin_id = item['id']
            symbol = item['symbol']

            coins[symbol] = coin_id

        return coins

    @staticmethod
    def validate_symbol(coin_dict, symbol) -> bool:
        try:
            coin_dict[symbol]
            return True
        except:
            return False

    @staticmethod
    def validate_batch_symbols(coin_dict, symbol_list) -> list:
        validation_result = []
        for symbol in symbol_list:
            try:
                id = coin_dict[symbol]
                validation_result.append(id)
            except:
                validation_result.append('')
        
        return validation_result

    @staticmethod
    def create_price_list(validated_symbols):
        pass

    def get_price(self, coin_symbol):
        if coingecko.validate_symbol(self._coins_id_dict,coin_symbol):
            coin_id = self._coins_id_dict[coin_symbol]

            coin_obj = req.get(self._base_api+"/coins/markets?vs_currency=usd&ids="+coin_id+"&sparkline=true").json()
            current_price = coin_obj[0]['current_price']

            return current_price

        else: return f'Coin {coin_symbol} not exist'

    def get_batch_price_dict(self, coin_symbols_list:list) -> dict:
        validated_symbols = coingecko.validate_batch_symbols(self._coins_id_dict, coin_symbols_list)
        validated_coin_ids = ','.join(validated_symbols)

        coin_objects = req.get(self._base_api+"/coins/markets?vs_currency=usd&ids="+validated_coin_ids).json()
        
        price_dict = {}
        for item in coin_objects:
            item_id = item['id']
            item_price = item['current_price']

            price_dict[item_id] = item_price

        return price_dict
    
    # need complete and enhance
    # def get_batch_price_list(self, coin_symbols_list):
    #     validated_symbols = coingecko.validate_batch_symbols(self._coins_id_dict, coin_symbols_list)
    #     price_list = []
    #     validated_coin_ids = ','.join(validated_symbols)

    #     coin_objects = req.get(self._base_api+"/coins/markets?vs_currency=usd&ids="+validated_coin_ids).json()
        
    #     price_dict = {}
    #     for item in coin_objects:
    #         item_id = item['id']
    #         item_price = item['current_price']

    #         price_dict[item_id] = item_price

    #     for item in validated_symbols:
    #         pass



    #     # i = 0
    #     # for symbol in validated_symbols:
    #     #     if symbol == '':
    #     #         price_list.append(0)
    #     #     else:  
    #     #         current_price = coin_objects[i]['current_price']
    #     #         price_list.append(current_price)
    #     #         #behine sazi in i
    #     #         i = i+1
        
    #     return price_list


    

    def get_mcap(self):pass

    def get_1d_volume(self):pass

    def get_7d_volume(self):pass

