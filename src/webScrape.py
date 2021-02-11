from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests

#import random as rand
#rand.randint(2, 30)


my_url='https://www.allrecipes.com/recipe/279909'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#get recipe name works as needed
recipe_name = page_soup.findAll("div", {"class": "headline-wrapper"})
recipe_name[0].text.strip() 

#title_container = containers[0]
#title_container = container.findAll("h1":{"class":"headline heading-content"})
#title_container.text

#get the ingredients 
ingredients = page_soup.findAll("span", {"class": "ingredients-item-name"})
print(' '.join(str(x.text) for x in ingredients))
# not needed print(ingredients[0].text)
print(ingredients[1].text)

#get method number of recipe
methodNum_container = page_soup.findAll("span", {"class": "checkbox-list-text"})
len(methodNum_container)

#not needed
"""test_str = methodNum_container[0].text.strip()
length = len(test_str)
last_char = test_str[length -1]
new_char = int(last_char)
methodNum_container[new_char - 1].text.strip()"""

method_container = page_soup.findAll("div", {"class": "paragraph"})
len(method_container)
print(' '.join(str(x.text) for x in method_container))

#get nutrients 
nut_container = page_soup.findAll("div", {"class": "section-body"})
len(nut_container)
print(' '.join(str(x.text) for x in nut_container))

#get full nutrients
nutrName_container = page_soup.findAll("span", {"class": "nutrient-value"})
len(nutrName_container)
print(' '.join(str(x.text) for x in nutrName_container))