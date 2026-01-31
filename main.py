from uuid import uuid1

import requests


def download_file(file_url: str):
    response = requests.get(file_url)
    
    path = f'images/{uuid1()}.webp'
    with open(path, 'wb') as f:
        f.write(response.content)

    return path


def main() -> None:
    url = 'https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/thumbnail.webp'
    path = download_file(file_url=url)

    {
        'name': '',
        'image': path
    }

main()
