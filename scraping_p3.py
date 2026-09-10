

def extract_and_load_images_category():
    pass


def load_all_category(all_category_books):
    pass

def extract_all_category(url):
    pass

def main():
    url = "http://books.toscrape.com/"
    all_category_books = extract_all_category(url)
    load_all_category(all_category_books)

if __name__ == "__main__":
    main()