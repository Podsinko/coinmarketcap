#!/usr/bin/python3
"""Coinmarketcap currencies info scraper."""
import requests


def coinmarket(coin):
    """Use this function to filter a list of dictionaries."""
    try:
        if coin:
            return [i for i in
                    requests.get(
                        'https://api.coinmarketcap.com/v1/ticker/?limit=0'
                    ).json()
                    if i['symbol'] == coin and i['price_usd'] is not None]
        else:
            return [i for i in
                    requests.get(
                        'https://api.coinmarketcap.com/v1/ticker/?limit=0'
                    ).json() if i['price_usd'] is not None
                    ]
    except:
        return False


if __name__ == "__main__":
    coinmarket(input('Enter coin name: '))
