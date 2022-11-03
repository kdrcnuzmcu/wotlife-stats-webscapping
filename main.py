import requests
from bs4 import BeautifulSoup
import pandas as pd

# Pandas ile sayfadaki bütün tabloları çektik.
stats = pd.read_html(io = * YOUR WOT-LIFE URL/KENDİ WOT-LIFE SAYFANIZ *)

# Aradığımız tablo 40 indeksinde bulunuyor.
tanks = stats[40]

# Veri setinin ilk iki anlamsız sütununu düşürdük.
tanks.drop(tanks.columns[:2], axis = 1, inplace = True)

# Web sayfasında görsel ile gösterilen değerleri manuel olarak almak için 'requests' modülünü kullandık.
html_data = requests.get(* YOUR WOT-LIFE URL/KENDİ WOT-LIFE SAYFANIZ *).text
soup = BeautifulSoup(html_data)

# HTML içinde 'tr' etiketlerini aradık ve istediğimiz etiket 536 indeksinde bulunuyor.
data = soup.find_all("tr")[536:]

# Her sütun için birer liste oluşturup, döngü yardımı ile her değeri ilgili listelere aktardık.
t_mastery = []
t_class = []
t_nation = []
for i in data:
    t_mastery.append(i.findChildren("span")[1]["title"])
    t_class.append(i.findChildren("span")[2]["title"])
    t_nation.append(i.findChildren("span")[3]["title"])

# Veri setimizde eksik olan verileri tanımladığımız listelerle doldurduk.
tanks.iloc[:, 1] = t_mastery
tanks.iloc[:, 2] = t_class
tanks.iloc[:, 3] = t_nation 

# Kesikli olması gereken değerler için bölme işlemi uyguladık.
tanks.iloc[:, 5] = tanks.iloc[:, 5] / 100
tanks.iloc[:, 9] = tanks.iloc[:, 9] / 100

# Veri setinin son görünümü için 'head' fonksiyonunu kullandık.
tanks.head()

# Hazırladığımız veri setini Excel dosyası olarak dışarı aktardık.
tanks.to_excel("Tanklar.xlsx")
