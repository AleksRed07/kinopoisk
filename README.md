# Kinopoisk Movie Parser

This project is a simple web scraper for collecting data about movies from the Kinopoisk website.

## Task Description

The script fetches the list of top movies from the Kinopoisk website, extracting information such as:
- Movie title
- Year of release
- Rating

The parsed data is saved to a CSV file for further analysis or usage.

## How to Use

### Prerequisites
- Python 3.7 or higher
- `requests` and `beautifulsoup4` libraries installed (you can install them via `pip`).

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/kinopoisk-parser.git
    cd kinopoisk-parser
    ```
2. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Script
Run the script using Python:
```bash
python kinopoisk_parser.py
