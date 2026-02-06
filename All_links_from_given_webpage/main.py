import requests as rq 
from bs4 import BeautifulSoup



url = input("Enter Link:")
if ("https" or "http") in url:
    data = rq.get(url)
    
else:
    data = rq.get(url)
    
soup = BeautifulSoup(data.text,"html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))
    

with open("mylinks.text","a") as saved:
    print(links[:10], file=saved)