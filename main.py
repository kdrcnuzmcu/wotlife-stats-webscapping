import requests
from bs4 import BeautifulSoup
import pandas as pd

stats = pd.read_html(io = * YOUR WOT-LIFE URL *)
tanks = stats[40]
tanks.drop(tanks.columns[:2], axis = 1, inplace = True)

html_data = requests.get(* YOUR WOT-LIFE URL *).text
soup = BeautifulSoup(html_data)
data = soup.find_all("tr")[536:]

t_mastery = []
t_class = []
t_nation = []
for i in data:
    t_mastery.append(i.findChildren("span")[1]["title"])
    t_class.append(i.findChildren("span")[2]["title"])
    t_nation.append(i.findChildren("span")[3]["title"])

tanks.iloc[:, 1] = t_mastery
tanks.iloc[:, 2] = t_class
tanks.iloc[:, 3] = t_nation 

tanks.iloc[:, 5] = tanks.iloc[:, 5] / 100
tanks.iloc[:, 9] = tanks.iloc[:, 9] / 100

tanks.head()

tanks.to_excel("Tanklar.xlsx")
