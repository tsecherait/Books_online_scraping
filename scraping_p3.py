from scraping_p2 import extract_and_transform_category
import requests
from bs4 import BeautifulSoup
import os
import csv

    
folder = "folder"


def extract_and_load_images_category(all_category_books):
    
    for category_name in all_category_books.keys():
        #create a folder with the category name
        image_folder = os.path.join(folder, "images", category_name)
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        #load images of a category in a folder with a category_name
        for book_data in all_category_books[category_name]:
            image_url = book_data["image_url"]
            image_name = book_data["universal_product_code"] + ".jpg"
            image_path = os.path.join(image_folder, image_name)
            response = requests.get(image_url)
            with open(image_path, 'wb') as image_file:
                image_file.write(response.content)
                


 




def load_all_category(all_category_books):
    #create folder/file folder
    file_folder = os.path.join(folder, "file")
    if not os.path.exists(file_folder):              
        os.makedirs(file_folder)
    for category_name in all_category_books.keys():
        #load files called category_name_books_data.csv in the folder called folder/file
        csv_filename = os.path.join(file_folder, f"{category_name}_books_data.csv")
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = all_category_books[category_name][0].keys()
            #create a writer csv object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book_data in all_category_books[category_name]:
                writer.writerow(book_data)
        

def extract_all_category(url):
    
    
    response = requests.get(url)
    all_category_books = {}
    
    soup = BeautifulSoup(response.content, 'html.parser')   
    category_links = soup.find('ul', class_='nav').find_all('a')
       
    for category_link in category_links:
        #generate the url of each category which will be the argument of an extract function
        category_url = url +'/'+ category_link['href']   
        category_name = category_url.split('/')[-2].split("_")[0]   
        if category_name != "books":
            #generate a list of dictionaries where the dictionnaries are the properties of each book of the category
            category_books_data = extract_and_transform_category(category_url)
            #put all categories books in a dictionnary where keys are the name of the category
            all_category_books.update({category_name: category_books_data})
    return all_category_books

def main():

    url = "http://books.toscrape.com/"
    download_image = input("écrivez oui si vous voulez télécharger les images:")
    
    all_category_books = extract_all_category(url)
    load_all_category(all_category_books)
    #ask if you want to download the images. Answer must be oui
    if download_image == "oui":
        extract_and_load_images_category(all_category_books)

if __name__ == "__main__":
    main()