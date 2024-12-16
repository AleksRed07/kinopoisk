import requests
from bs4 import BeautifulSoup
import csv

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None

def parse_movies(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    movies = []

    for movie in soup.select(".desktop-rating-selection-film-item"):
        title = movie.select_one(".selection-film-item-meta__name").get_text(strip=True)
        year = movie.select_one(".selection-film-item-meta__original-name").get_text(strip=True) if movie.select_one(".selection-film-item-meta__original-name") else "N/A"
        rating = movie.select_one(".rating__value").get_text(strip=True) if movie.select_one(".rating__value") else "N/A"
        movies.append({"title": title, "year": year, "rating": rating})

    return movies

def save_to_csv(movies, filename):
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "year", "rating"])
        writer.writeheader()
        writer.writerows(movies)

if __name__ == "__main__":
    url = "https://www.kinopoisk.ru/lists/top/"
    page_content = fetch_page(url)

    if page_content:
        movies = parse_movies(page_content)
        save_to_csv(movies, "kinopoisk_movies.csv")
        print("Data has been saved to kinopoisk_movies.csv")
