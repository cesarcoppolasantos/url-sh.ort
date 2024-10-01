import json
import os

from shortuuid_gen import shortuuid_gen


def create_json():
    if not os.path.exists('urls.json'):
        with open('urls.json', "w", encoding="UTF-8") as urls:
            json.dump([], urls, indent=4)


def store_urls(url):

    create_json()

    short_url = shortuuid_gen()

    urls_dict = {
            short_url: url
        }

    with open('urls.json', "r", encoding="UTF-8") as urls:
        data = json.load(urls)

    data.append(urls_dict)

    with open('urls.json', "w", encoding="UTF-8") as urls:
        json.dump(data, urls, indent=4)
    
    return short_url

def get_long_url(short_url):

    with open('urls.json', 'r', encoding="UTF-8") as urls:
        data = json.load(urls)

    for value in data:

        for key in value.keys():

            if key == short_url:

                return value[key]