import portfolio

def main():
    welcome_lines_list = [
            'Welcome to Crypto Portfolio Manager App',
            '+++++++++++++++++++++++++++++++++++++++'
        ]
    help_lines_list = [
            '',
            '1: Show your portfolio',
            '2: Add new item',
            '3: Sell an item',
            '4: Delete an item',
            '0: Exit'
    ]
    print('\n'.join(welcome_lines_list+help_lines_list))

    exit = False
    Portfolio = portfolio.Portfolio()

    while True:
        user_input = int(input('\nEnter a Number you want:'))
        
        if user_input == 0: break
        elif user_input ==1: print(Portfolio.portfo_table())

        elif user_input ==2:
            itemname = input('\nEnter Item Name:')
            amount = float(input('\nEnter amount you bought:'))
            buyprice = float(input('\nEnter your buy price:'))

            try:
                Portfolio.add_item(itemname,amount,buyprice)
                print('Item added successfully')
            except:
                print('something wont wrong.. try again')
            

        elif user_input ==3:
            pass

        elif user_input ==4:
            pass


        print('\n'.join(help_lines_list))

    print('Thanks for use CryptoPortfolio !!!')





if __name__ == '__main__':main()