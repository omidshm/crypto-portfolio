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
        validated_ids = []
        for symbol in symbol_list:
            try:
                id = coin_dict[symbol]
                validation_result.append(True)
                validated_ids.append(id)
            except:
                validation_result.append(False)
        
        return validation_result, validated_ids

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


    def get_batch_price(self, coin_symbols_list):
        validated_symbols,validated_ids_list = coingecko.validate_batch_symbols(self._coins_id_dict, coin_symbols_list)
        price_list = []
        validated_ids_str = ','.join(validated_ids_list)

        coin_objects = req.get(self._base_api+"/coins/markets?vs_currency=usd&ids="+validated_ids_str+"&sparkline=true").json()
        
        i = 0
        for symbol in validated_symbols:
            if symbol == True:
                current_price = coin_objects[i]['current_price']
                price_list.append(current_price)
            else:
                price_list.append(0)

            
            #behine sazi in i
            i = i+1
        
        return price_list


    def get_mcap(self):pass

    def get_1d_volume(self):pass

    def get_7d_volume(self):pass

