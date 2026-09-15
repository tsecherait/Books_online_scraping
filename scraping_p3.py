from scraping_p2 import extract_and_transform_category
import requests
from bs4 import BeautifulSoup



def extract_and_load_images_category(all_category_books):
    pass

def load_all_category(all_category_books):
    pass


def extract_all_category(url):
    response = requests.get(url)
    all_category_books = {}
        
    soup = BeautifulSoup(response.content, 'html.parser')   
    category_links = soup.find('ul', class_='nav').findAll('a')
            
    for category_link in category_links:
        category_url = url +'/'+ category_link['href']   
        category_name = category_url.split('/')[-2].split("_")[0]   
        if category_name != "books":
            category_books_data = extract_and_transform_category(category_url)
            all_category_books.update({category_name: category_books_data})
    return all_category_books
    
    


def main():

    url = "http://books.toscrape.com/"
    download_image = input("écrivez oui si vous voulez télécharger les images:")
    
    all_category_books = extract_all_category(url)
    load_all_category(all_category_books)
    if download_image == "oui":
        extract_and_load_images_category(all_category_books)

if __name__ == "__main__":
    main()