# Web-Scrapping using Beautifulsoup

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan dari projek ini adalah melakukan simple webscrapping untuk mendapatkan informasi. Kita juga akan memanfaatkan flask dashboard sederhana untuk menampilkan hasil scrap dan visualisasi kita.

## Objectives
Secara singkat, tujuan dari project ini adalah melakukan web-scraping berdasarkan data film yang rilis di tahun 2021 dari `https://www.imdb.com/search/title/?release_date=2021-01-01,2021-12-31`

- Dari laman web tersebut kita tarik data berupa `judul film` , `imdb rating` , `metascore`, dan `votes`
- Selanjutnya kita buat plot dari 7 film paling populer di tahun 2021.

## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

## Rubics

- Environment preparation (2 points)
- Finding the right key to scrap the data  & Extracting the right information (5 points)
- Creating data frame & Data wrangling (5 points)
- Creating a tidy python notebook as a report. (2 points)
- Implement it on flask dashboard (2 points)

## Environment Preparation
Cukup dengan menginstall requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
```

## Data Scraping with `BeautifulSoup`

Menemukan kunci utama untuk melakukan data scraping dgn fungsi sederhana berikut: 
```python
table = soup.find(___)
movie_list = table.find_all(___)
```

Hasil dari data scraping kemudian disimpan dalam dataframe `df`

```python
df = pd.DataFrame({'movie_title':title,
                    'movie_ratings':ratings,
                    'metascore':meta,
                    'votes':votes_imdb    
                    })
```

untuk selanjutnya kita rapikan dan persiapkan sesuai dengan kebutuhan.

## Reporting
Melakukan analisa sederhana berdasarkan hasil data scrapping & visualisasi, guna menemukan **Top 7 Most Popular Movies 2021**.

## Visualisation using Flask 
Implementasi code ke dalam file `app.py` dan menampilkannya dalam dashboard flask

**<p align="right">By: Theresia Londong | 06-Jan-2023</p>**
