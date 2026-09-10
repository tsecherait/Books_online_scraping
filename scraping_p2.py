



def extract_and_transform_category(url):
    pass


def load_category(list_data_category):
    pass

def main():

    url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    list_data_category = extract_and_transform_category(url) 
    load_category(list_data_category)


if __name__ == "__main__":
    main()