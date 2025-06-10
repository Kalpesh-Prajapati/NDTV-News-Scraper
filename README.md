# NDTV News Scraper 📰

This Python script scrapes the latest news articles from [NDTV](https://www.ndtv.com/latest) and saves the data to a CSV file. It uses `requests` and `BeautifulSoup` to extract news headlines, dates, authors, images, and brief descriptions.

### 📄 Suggested Folder Structure

```
ndtv-news-scraper/
├── ndtv_scraper.py
├── README.md
└── news.csv (generated on runtime)
```

## 🔍 What It Does

- Fetches the latest news from the NDTV "Latest" section
- Extracts:
  - Date & Time
  - Author/Source
  - Headline Title
  - Image URL
  - News Description
- Saves everything into a structured CSV file: `news.csv`

## 🚀 Requirements

- Python 3.x
- requests
- beautifulsoup4

### 📦 Install Dependencies

```bash
pip install requests beautifulsoup4
````

## ▶️ How to Run

```bash
python ndtv_scraper.py
```

After execution, you'll find a file named `news.csv` in the same directory containing all the scraped news.

## ⚠️ Disclaimer

This project is for educational purposes only. Please refer to [NDTV's Terms of Service](https://www.ndtv.com/convergence/ndtv/ndtv_copyright.aspx) before using scraped data in any public or commercial context.

## 🙋‍♂️ Author

Created by Kalpesh Prajapati

1. **Create a new folder and move the script into it**:
   ```bash
   mkdir ndtv-news-scraper
   cd ndtv-news-scraper
   mv your_script.py ndtv_scraper.py  # Rename for clarity
    ````

2. **Create the README**:
   Save the above `README.md` content in this folder.

3. **Initialize Git and Push to GitHub**:

   ```bash
   git init
   git add .
   git commit -m "Initial commit: Add NDTV news scraper"
   git branch -M main
   git remote add origin https://github.com/Kalpesh-Prajapati/ndtv-news-scraper.git
   git push -u origin main
   ```
