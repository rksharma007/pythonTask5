import requests
from bs4 import BeautifulSoup
import pandas as pd
Title=[]  #List to store title of most popular TV shows
Year=[]   #List to store releasing year of each TV show
Rating=[] #List to store ratings of each TV show

url = "https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv"
content = requests.get(url).content

soup = BeautifulSoup(content, "html.parser")

for i in soup.find("tbody", {"class":"lister-list"}).find_all("tr"):
    h = i.find("td",{"class":"titleColumn"})
    title = h.find("a", href=True)
    year = i.find("span",{"class":"secondaryInfo"})
    rating = i.find("td",{"class":"ratingColumn imdbRating"})

    Title.append(title.text)
    Year.append(year.text)
    Rating.append(rating.text.strip("\n"))
    df=pd.DataFrame({'Most Popular TV Shows' : Title,'Year' : Year,'Rating' : Rating})
df.to_csv('IMDb.csv', index=False, encoding='utf-8')
data = pd.read_csv('IMDb.csv')
data.head()
