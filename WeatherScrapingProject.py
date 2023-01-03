import pandas as dp
import requests
from bs4 import BeautifulSoup
page=requests.get("https://weather.com/en-GH/weather/tenday/l/f30d357b88c355dbd3eacc1982f47358e760dca64a637e6a505eed7ecc13d43b#detailIndex5")
content_=BeautifulSoup(page.content, "html.parser")

day=content_.find_all(class_="DailyContent--daypartName--3emSU")
day_=[d.get_text() for d in day]
#print(day_)

temperature_=content_.find_all(class_="DailyContent--temp--1s3a7")
temp_=[temp.get_text() for temp in temperature_]
#to remove values for night, the i is more of a dummy, i don't know if it will bring up an error since i already used temp,  hence i
#print(temp_)


narrativ=content_.find_all(class_="DailyContent--narrative--3Ti6_")
narrative_=[narrate.get_text() for narrate in narrativ]
#print(narrative_)

database=dp.DataFrame({"The Day":day_, "The Highest Temperature":temp_, "The Narrative":narrative_})
print(database)
database.to_csv("The next 10 day Weather, by Richard Djirackor.csv")




