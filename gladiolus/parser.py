#!/usr/bin/python3
"""Coinmarketcap currencies info scraper."""
import time

import requests


def localtime(epoch):
    """Convert epoch time to local time."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch)))


def coinmarket(coin):
    """Use this function to filter a list of dictionaries."""
    try:
        if coin:
            return [i for i in
                    requests.get(
                        'https://api.coinmarketcap.com/v1/ticker/?limit=0'
                    ).json()
                    if i['symbol'] == coin and i['percent_change_24h'
                                                 ] is not None]
        else:
            return [i for i in
                    requests.get(
                        'https://api.coinmarketcap.com/v1/ticker/?limit=0'
                    ).json() if i['percent_change_24h'] is not None
                    ][:10]
    except:
        return False


if __name__ == "__main__":
    coinmarket(input('Enter coin name: '))
