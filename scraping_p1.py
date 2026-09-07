import requests
import csv



def extract(url):
    response = requests.get(url)
    page = response.content

    product_page_url_to_transform = str(url)

    data_to_transform = {
                'product_page_url_to_transform': product_page_url_to_transform,
    }
    return data_to_transform


def transform(data_to_transform):
    data_to_load = {
            'product_page_url': data_to_transform['product_page_url_to_transform'],
    }
    return data_to_load
    
def load(data_to_load, filename="output.csv"):
    with open(filename, mode="w") as file:
        fieldnames = data_to_load.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        writer.writerow(data_to_load)


def main():
       
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    data_to_transform = extract(url)
    data_to_load = transform(data_to_transform)
    load(data_to_load, "output.csv")


if __name__ == "__main__":
    main()