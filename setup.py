from publication_scraper import fetch_posts
from database_functions import create_tables

create_tables()

fetch_posts(200)
