import requests
import json

from fake_useragent import UserAgent

ua = UserAgent()


def collect_data(cat_type='', max_price = 75, min_price = 50, discount_procent = -10, users_id = 'guest'):
    offset = 0
    batch_size = 60
    result = []
    count = 0
    
    while True:
        for item in range(offset, offset + batch_size, 60):
            
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice={max_price}&minPrice={min_price}&offset={item}{cat_type}&withStack=true'
            response = requests.get(
                url = url,
                headers = {'user-agent': f'{ua.random}'}
            )
            
            offset += batch_size
            
            data = response.json()
            items = data.get('items')
            
            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < discount_procent:
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_over_price = i.get('overprice')
                    
                    result.append(
                        {
                            'full_name': item_full_name,
                            '3d': item_3d,
                            'overprice': item_over_price,
                            'item_price': item_price
                        }
                    )
                    
        count += 1
        print(f'Page №{count}') 
        print(url)           
        
        if len(items) < 60:
            break
    
    with open(f'Data/Result_and_setup/result{users_id}.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent = 4, ensure_ascii = False)
    
    print(str(len(result)) + ' предмета(ов)')


def main():
    collect_data()


if __name__ == '__main__':
    main()