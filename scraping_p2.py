import requests
from bs4 import BeautifulSoup
from scraping_p1 import extract
from scraping_p1 import transform


def extract_and_transform_category(url):
    list_data_category = []
    condition = True
        #loop to create a list of dictionnaries whose values are books properties
    while condition:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    
        books = soup.find_all('h3')
        for book in books:
            book_link = book.find('a')['href']
                
            data_book_category = transform(extract(url.rsplit('/', 4)[0] +'/'+ book_link.split('/', 3)[3]))
            list_data_category.append(data_book_category)
    
        next_page = soup.find('li', class_='next')
        if next_page:
            next_page_link = next_page.find('a')['href']
    
                
            next_page_url = url.rsplit('/',2)[0]+'/'+next_page_link
            url = next_page_url
            condition = url
        else:
            condition = next_page
            
    
    return list_data_category


def load_category(list_data_category):
    pass

def main():

    url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    list_data_category = extract_and_transform_category(url) 
    load_category(list_data_category)


if __name__ == "__main__":
    main()