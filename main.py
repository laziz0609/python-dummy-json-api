import json

from uuid import uuid1

import requests


def get_produts() -> list:
    url = "https://dummyjson.com/products"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("xato")
    return response.json()["products"]


def download_file(data: dict) -> list:
    images: list = data["images"]
    
    image_paths = []
    for image in images:
        path = f'images/{uuid1()}.webp'
        with open(path, 'wb') as f:
            f.write(requests.get(image).content)
        
        image_paths.append(path)

    return image_paths

def main() -> None:
    products: list[dict[str, str | int]] = []
    data = get_produts()

    for product in data:
        image_paths = download_file(product)
    
        products.append({
                "id":    product["id"],
                "title": product["title"],
                "description": product["description"],
                "category": product["category"],
                "price":    product["price"],
                "image_paths": image_paths
                })

    json_path = "products.json"
    
    with open(json_path, "w") as json_file:
        json_file.write(json.dumps(products, indent=4))
         
main()
