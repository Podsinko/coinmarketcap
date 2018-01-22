#!/usr/bin/python3
"""Coinmarketcap currencies info scraper."""
import requests


def coinmarket(coin):
    """Use this function to filter a list of dictionaries."""
    try:
        return [i for i in
                requests.get(
                    'https://api.coinmarketcap.com/v1/ticker/?limit=0').json()
                if i['symbol'] == coin][0]
    except:
        return False


if __name__ == "__main__":
    coinmarket(input('Enter coin name: '))
