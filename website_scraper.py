import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"

response = requests.get(url)

if response.status_code == 200:
	soup = BeautifulSoup(response.content, "html.parser")
	#replace "title" with the name of the html tag u want to scrape
	elements = soup.find_all("title")
	for element in elements:
		print(element.text)
else:
	print("failed to retrieve website")
