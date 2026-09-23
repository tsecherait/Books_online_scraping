# Scraper sur les données des livres du site Books Online

Comment exécuter le code fourni ici afin de surveiller des prix sur le site Books Online http://books.toscrape.com/

## Télécharger le code source

```code
git clone https://github.com/kenza12/formation.git
cd Books_online_scraping
```

## Créer un environnement virtuel nommé env

```code
python3.13 -m venv env
source env/bin/activate
```

## Installer les dépendances à partir du fichier requirements.txt

Le fichier `requirements.txt` contient toutes les dépendances nécessaires à l'exécution des scripts.

```code
pip3 install -r requirements.txt
```

## Extraire les informations d'une page d'un bouquin

Le script `scraping_p1.py` permet de visiter une page d'un bouquin spécifiée sur le site [Books Online](http://books.toscrape.com/), d'extraire les informations essentielles ci-dessous, puis de les écrire dans un fichier CSV avec des en-têtes de colonnes appropriées.

- product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

```code
# Exécuter le script scraping_p1.py avec les paramètres associés
python scraping_p1.py <url_page_produit>
```

**Exemple:**

```code
python scraping_p1.py http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html
```

Le fichier de sortie se trouve dans `output.csv`.

## Récupérer toutes les données nécessaires pour toute une catégorie d'ouvrages

Le script `scraping_p2.py` va parcourir plusieurs pages de livres d'une catégorie littéraire afin de récupérer les informations de la phase p1.

```code
# Exécuter le script scraping_p2.py avec les paramètres associés
python scraping_p2.py <url_page_categorie>
```

```code
python scraping_p2.py http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
```

Les données des livres de la catégorie donnée sont écrites dans `category_books_data.csv`.

## Extraire toutes les catégories de livres disponibles ainsi que toutes les informations produit de tous les livres

Le script `scraping_p3.py` va extraire toutes les informations de toutes les catégories littéraires de livres du site [Books Online](http://books.toscrape.com/).

Ce script permet aussi de télécharger et d'enregistrer les images de chaque page livres si on le souhaite.


```code
# Exécuter le script scraping_p3.py
python scraping_p3.py
```

Les données des livres de chaque catégorie sont enregistrées dans le dossier `folder/file` sous forme de fichiers CSV.
Si l'on indique lors de l'exécution du programme que l'on souhaite télécharger les images, elles seront téléchargés dans le dossier `folder/images` sous forme de JPG.

Vous pouvez ouvrir tous les fichiers CSV avec la commande open sous Mac :


**Exemple:**

````
open output.csv
```