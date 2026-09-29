from scraping_p3 import extract_all_category
from scraping_p3 import extract_and_load_images_category
from scraping_p2 import extract_and_transform_category
from scraping_p2 import load_category
from scraping_p1 import extract
from scraping_p1 import transform
from scraping_p1 import load

url = input("donnez l'url correspondant à la partie du site Books to scrape que vous voulez scraper: ")




    
#if it's not a category page, continue to test
if not("category" in url.split('/')):
    #if a not a request for the index.html page of the website. Then it's a product page and go to scraping_p1.py script
    if not(url == "https://books.toscrape.com" or url == "https://books.toscrape.com/index.html"):
        data_to_transform = extract(url)
        data_to_load = transform(data_to_transform)
        load(data_to_load, "output.csv")
    
    #if it's the index.html website page, then go to scraping_p3.py
    else:

        url = "https://books.toscrape.com"
        all_category_books = extract_all_category(url)
        image_bool = input("Ecrivez oui si vous voulez télécharger les images du site: ")
        if image_bool == "oui":
            extract_and_load_images_category(all_category_books)
#if it's a ctegory page, go to scraping_p2.py
else:
    list_data_category = extract_and_transform_category(url) 
    load_category(list_data_category)

