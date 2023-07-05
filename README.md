# Web-Scrapping using Beautifulsoup

This project was developed as one of the capstone projects of the Algorithm Academy Data Analytics Specialization. The expected deliverables from this project are doing simple web scraping to get information. We'll also make use of a simple Flask dashboard to display our scrap results and visualizations.

## Objectives
In short, the goal of this project is to do web-scraping based on data on films released in 2021 from 
https://www.imdb.com/search/title/?release_date=2021-01-01,2021-12-31

- From the web page we retrieve information such as: `movie title`, `imdb rating`, `metascore`, and `votes`
- Next, we will plot the 7 most popular films in 2021.
  
## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

## Rubics

- Environment preparation (2 points)
- Finding the right key to scrape the data  & extract the right information (5 points)
- Creating data frame & Data wrangling (5 points)
- Creating a tidy Python notebook as a report. (2 points)
- Implement it on the Flask dashboard (2 points)

## Environment Preparation
Simply by installing the `requirements.txt` in the following way

```python
pip install -r requirements.txt
```

## Data Scraping with `BeautifulSoup`

Find the primary key to perform data scraping with the following function:

```python
table = soup.find(___)
movie_list = table.find_all(___)
```

The output of the data scraping process above is then stored in the `df` data frame

```python
df = pd.DataFrame({'movie_title':title,
                    'movie_ratings':ratings,
                    'metascore':meta,
                    'votes':votes_imdb    
                    })
```

for further cleansed and processed according to our business needs.

## Reporting
Conducting a simple analysis based on the results of data scraping and visualization, in order to find **Top 7 Most Popular Movies 2021**.

## Visualization using Flask 
Implement the code in the `app.py` file and visualization using the Flask dashboard

**<p align="right">By: Theresia Londong | 06-Jan-2023</p>**
