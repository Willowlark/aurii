from imgurpython import ImgurClient
from os import makedirs
import urllib.request
import argparse

album_id = 'MSdbLa6'
request_url = 'https://api.imgur.com/3/album/' + album_id
client_id = 'c33352ff1bdd5e2'
client_secret = 'a4c9ebfe300b6e7297b160ed23f267aa3a34e86e'

def dl(album_id):
    client = ImgurClient(client_id, client_secret)

    makedirs(f"assets/imgur/{album_id}")
    items = client.get_album_images(album_id)
    for item, page in zip(items, range(100, 100+len(items))):
        extension = item.link.split('.')[-1]
        urllib.request.urlretrieve(item.link, f"assets/imgur/{album_id}/{album_id}-{page}.{extension}")
        print(item.link)
    
parser = argparse.ArgumentParser()
parser.add_argument("album_id", help="album hash")
args = parser.parse_args()
dl(args.album_id)