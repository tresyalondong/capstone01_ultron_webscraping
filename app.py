from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests
import re

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

# initiation
title=[] # initiate tuple for movie title
ratings=[] # initiate tuple for viewer ratings
meta=[] # initiate tuple for metascore
votes_imdb=[] # initiate tuple for viewer votes
rank=7 #any number to perform subsetting of the Top <Rank> Movies

#request data from website for the first 300 data (or the first 6 pages)
for n in range(1, 252, 50):
	# start scraping here
	url_get=requests.get('https://www.imdb.com/search/title/?release_date=2021-01-01,2021-12-31&start=' + str(n) + '&ref_=adv_nxt')
    # Create BeautifulSoup object
	soup = BeautifulSoup(url_get.content,"html.parser")
	# Finding Key to scrap the data needed
	table = soup.find('div',attrs={'class':'lister-list'})
    # To find the row length for each page iteration 
	movie_list=table.find_all('div', attrs={'class':'lister-item mode-advanced'})
	row_length= len(movie_list)

    # Data scraping loop, based on row_length information, to get data from each page 
	for i in range(0, row_length):		
		# Scraping the movie's name
		name = table.find_all('h3', attrs={'a':''})[i].get_text().strip()
		name_clean=re.findall('\n(.*)\n', name)  #using regex to cleance movie title from unwanted characters, resulted in series of lists
		title.append(name_clean[0]) # take only first element of each lists in the name_clean object 

        # Scraping the imdb ratings
		rate_imdb = table.find_all('strong')[i].get_text().strip()
		ratings.append(rate_imdb)  

        # Scraping metascores value, if any, otherwise return with None 
		if table.find_all('div', attrs={'class':'ratings-bar'})[i].find('span', class_ = 'metascore') is not None:
			m_score=table.find_all('div', attrs={'class':'ratings-bar'})[i].find('span', class_ = 'metascore').get_text().strip()
			meta.append(m_score)
		else:
			meta.append(0) #assign value 0 to movies with no metascore (for statistical purpose) 

        # Scraping voting result
		votes=table.find_all('p', attrs={'class':'sort-num_votes-visible'})[i].find('span', attrs = {'name':'nv'}).get_text().strip()
		votes_imdb.append(votes)

#change into dataframe
data = pd.DataFrame({'movie_title':title,
                    'movie_ratings':ratings,
                    'metascore':meta,
                    'votes':votes_imdb    
                    })

#insert data wrangling here
#to clean and change data type of column movie_ratings, metascore and votes
data['movie_ratings'] = data['movie_ratings'].astype('float64')
data['votes'] =data['votes'].str.replace(",","").astype('int64')
data['metascore'] =data['metascore'].astype('int64')

#add column for metascore in scale of 1 to 10, for side to side comparison with viewer ratings later
max_meta=100 #maximum scale of metascore
max_ratings=10 #maximum scale of viewer ratingsdata['meta_adj']data['metascore']/max_meta*max_ratings
data['meta_adj']=data['metascore']/max_meta*max_ratings

#set movie_title as index
data=data.set_index('movie_title') 

#to find 7 most popular movies based on movie ratings  
top7_ratings=data.sort_values(by='movie_ratings', ascending=False).head(rank).loc[:,['movie_ratings']]

#to find 7 most popular movies based on viewer votes  
top7_votes=data.sort_values(by='votes', ascending=False).head(rank).loc[:,['votes']]

#to find 7 most popular movies based on movie critics (metascore)
top7_meta=data.sort_values(by='metascore', ascending=False).head(rank).loc[:,['metascore','meta_adj']]

#Comparison Table of 7 Top Movies on Each Category (Based on: Viewer Ratings, Votes, and Metascore)
top7=pd.DataFrame().assign(Top7_Ratings=top7_ratings.reset_index()['movie_title'],
                           Top7_Votes=top7_votes.reset_index()['movie_title'], Top7_Meta=top7_meta.reset_index()['movie_title'])

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{data["movie_ratings"].median().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = top7_ratings.plot.bar(figsize = (20,9), grid=True, color='g') 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)