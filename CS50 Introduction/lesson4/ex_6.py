import requests


def main():
    count = count_btc()
    price = price_btc()
    ans = (count * price)
    print(f"${ans:,.4f}")

def count_btc():
    while True:
        try:
            print('Print count btc: ')
            count = float(input())
            return count
        except:
            print('Print correct count!')


def price_btc():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        print('I dnt knw wht i shld do with it 0_o')

    bpi = response["bpi"]
    usd = bpi["USD"]
    price = float(usd["rate_float"])
    return price

if __name__ == '__main__':
    main()