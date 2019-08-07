import random
from tkinter import *
import requests
import itertools
from bs4 import BeautifulSoup

root = Tk('Burgers')

url = 'https://www.google.com/search?client=safari&rls=en&q=burgers+near+me&ie=UTF-8&oe=UTF-8'


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
soup.find_all(role='heading')
results = soup.find_all(role='heading')


BurgerList = []

for results in results[:]:
	all_results = results.find('span')
	for n in all_results:
		choices = all_results.text
		choices = choices.split('"')
		BurgerList.append(choices)
		flat = itertools.chain.from_iterable(BurgerList)
flat = list(flat)
place = random.choice(flat)

url2 ='https://www.google.com/search?client=safari&rls=en&q=chicken+near+me&ie=UTF-8&oe=UTF-8'
response_c = requests.get(url2)
soup_c = BeautifulSoup(response_c.text, "html.parser")
soup_c.find_all(role='heading')
results_c = soup_c.find_all(role='heading')

ChickenList = []
for results_c in results_c[:]:
	all_results_c = results_c.find('span')
	for n in all_results_c:
		choices = all_results_c.text
		choices = choices.split('"')
		ChickenList.append(choices)
		flat2 = itertools.chain.from_iterable(ChickenList)
flat_c = list(flat2)

url3 ='https://www.google.com/search?client=safari&rls=en&q=mexican+near+me&ie=UTF-8&oe=UTF-8'
response_m = requests.get(url3)
soup_m = BeautifulSoup(response_m.text, "html.parser")
soup_m.find_all(role='heading')
results_m = soup_m.find_all(role='heading')

MexicanList = []
for results_m in results_m[:]:
	all_results_m = results_m.find('span')
	for n in all_results_c:
		choices = all_results_m.text
		choices = choices.split('"')
		MexicanList.append(choices)
		flat3 = itertools.chain.from_iterable(MexicanList)
flat_m = list(flat3)

T = Text(root, height=40, width=30)
T.pack()
Button(root, text="Burgers", command=lambda: T.insert(END, str(random.choice(flat)) + "\n")).pack()
Button(root, text="Chicken", command=lambda: T.insert(END, str(random.choice(flat_c)) + "\n")).pack()
Button(root, text="Mexican", command=lambda: T.insert(END, str(random.choice(flat_m)) + "\n")).pack()
T.insert(END, "generate a random selection" + "\n")
root.mainloop()
