import requests
import os


session = os.getenv('AOC_SESSION')

url = 'http://adventofcode.com/2017/day/{}/input'


def get_input(day):

    r = requests.get(url.format(day), cookies={'session': session})
    r.raise_for_status()

    return r.text
