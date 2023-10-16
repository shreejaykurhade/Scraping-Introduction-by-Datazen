import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

### Defining the HTTP Agent
headers = ( {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0', 'Accept-Language': 'en-US, en;q=0.5'})
r = requests.get(url, headers=headers)
print(r)

type(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup)

### Lists to Store Info
countryName = []
countryCapital = []
countryPopulation = []
countryArea = []

### First lets extract the entire element for the countries
data = soup.find_all("div", class_ = "col-md-4 country")
print(len(data))

### Using a loop to iterate through our list
for element in data:
  country_name = element.find("h3", class_ = "country-name")
  value = country_name.text
  countryName.append(value)

print(countryName)

for element in data:
  country_capital = element.find("span", class_ = "country-capital")
  value = country_capital.text
  countryCapital.append(value)

print(countryCapital)

for element in data:
  country_population = element.find("span", class_ = "country-population")
  value = country_population.text
  countryPopulation.append(value)

print(countryPopulation)

for element in data:
  country_area = element.find("span", class_ = "country-area")
  value = country_area.text
  countryArea.append(value)

print(countryArea)

df = pd.DataFrame({"Country Name": countryName, "Country Capital": countryCapital, "Country Population": countryPopulation, "Country Area(sq. km)": countryArea})
print(df)

df['Country Name'] = df['Country Name'].str.strip()
print(df)

df.to_csv('Scraped Data.csv', index = False)

df.isnull().sum()

df.info()

df['Country Population'] = pd.to_numeric(df['Country Population'])

df['Country Area(sq. km)'] = pd.to_numeric(df['Country Area(sq. km)'])

df.describe()

df=df.sort_values(['Country Population','Country Area(sq. km)'],ascending=False)

df1=pd.read_csv("Scrapped Data.csv")
df1.to_excel("excel_formal_scrapped_data.xlsv",index=False)







