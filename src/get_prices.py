import json
from yahoo_fin import stock_info as si
from datetime import date

def get_static_prices(fn=r'/Users/xiaolan/Documents/repos/FinProject/local_src/static_prices.json'):
    """
    Get pre-saved prices to calculate positions. This is to speed up 
    position calculation by avoiding the time-consuming getting-live-stock-price
    step.
    """
    with open(fn, 'r') as fp:
        data = json.load(fp)
    return data

def get_live_prices(l):
    """
    Get real time stock prices to calculate positions. 
    This could be time-consuming.
    """
    data = {}
    for i, s in enumerate(l):
        print("getting {} of {}".format(i+1, len(l)))
        if s!='date':
            data[s.upper()] = si.get_live_price(s.lower())
        else:
            data['date'] = str(date.today())
    return data

def save_prices(data, fn=r'/Users/xiaolan/Documents/repos/FinProject/local_src/static_prices.json'):

    with open(fn, 'w') as fp:
        json.dump(data, fp)

if __name__ == "__main__":
    pre_data = get_static_prices()
    l = list(pre_data.keys())
    data = get_live_prices(l)
    save_prices(data)
    print('Done')
    