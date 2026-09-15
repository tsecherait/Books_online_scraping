def extract_and_load_images_category(all_category_books):
    pass

def load_all_category(all_category_books):
    pass


def extract_all_category(url):
    pass


def main():

    url = "http://books.toscrape.com/"
    download_image = input("écrivez oui si vous voulez télécharger les images:")
    
    all_category_books = extract_all_category(url)
    load_all_category(all_category_books)
    if download_image == "oui":
        extract_and_load_images_category(all_category_books)

if __name__ == "__main__":
    main()