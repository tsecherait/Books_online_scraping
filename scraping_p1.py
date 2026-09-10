import requests
import csv
from bs4 import BeautifulSoup
import re



def extract(url):
    #downloading the web page
    response = requests.get(url)
    page = response.content

    soup = BeautifulSoup(page, 'html.parser')

    #Extraction of the different properties required
    product_page_url_to_transform = str(url)
    tds = soup.find_all('td')  
    universal_product_code_to_transform = tds[0].string
    number_available_to_transform = tds[5].string
    title_to_transform =soup.h1.text
    price_including_tax_to_transform = tds[3].string
    price_excluding_tax_to_transform = tds[2].string
    product_description_to_transform = soup.find("meta", {"name": "description"}).get("content")
    category_to_transform = soup.find("ul", class_="breadcrumb").find_all("li")[-2].find("a").text
    review_rating_to_transform = soup.find('p', class_='star-rating')['class'][1]
    image_url_to_transform = soup.find('article', class_='product_page').find("div").find("img").get("src")
    #put the properties in a dictionnary
    data_to_transform = {

        'product_page_url_to_transform': product_page_url_to_transform,
        'universal_product_code_to_transform': universal_product_code_to_transform,
        'number_available_to_transform': number_available_to_transform,
        'title_to_transform': title_to_transform,
        'price_including_tax_to_transform': price_including_tax_to_transform,
        'price_excluding_tax_to_transform': price_excluding_tax_to_transform,
        'product_description_to_transform': product_description_to_transform,
        'category_to_transform': category_to_transform,
        'review_rating_to_transform': review_rating_to_transform,
        'image_url_to_transform': image_url_to_transform,

    }
    return data_to_transform


def transform(data_to_transform):
    #to convert the number property in letters in real numbers
    rating_mapping = {

        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    #Transform the properties value as it required
    data_to_load = {


        'product_page_url': data_to_transform['product_page_url_to_transform'],
        'universal_product_code': data_to_transform['universal_product_code_to_transform'],
        'number_available': int(re.search(r'\d+', data_to_transform['number_available_to_transform']).group()),
        'title': data_to_transform['title_to_transform'],
        'price_including_tax': float(data_to_transform['price_including_tax_to_transform'][1:]),
        'price_excluding_tax': float(data_to_transform['price_excluding_tax_to_transform'][1:]),
        'product_description': data_to_transform['product_description_to_transform'].strip(),
        'category': data_to_transform['category_to_transform'],
        'review_rating': rating_mapping.get(data_to_transform['review_rating_to_transform'],None),
        'image_url': 'product_page_url_to_transform'.rsplit('/', 2)[0] + '/' + data_to_transform['image_url_to_transform'],
    }
    return data_to_load
    
def load(data_to_load, filename="output.csv"):

    #Write the properties ans their value in csv file
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