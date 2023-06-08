import requests
from bs4 import BeautifulSoup
import json
import datetime

def parse_item_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    item_titles = soup.find_all("ur item", class_="ur class name or id")
    item_titles_text = [title.a.text.strip() for title in item_titles if title.a]
    return item_titles_text

while True:
    url = input("input link: ")
    item_titles = parse_item_titles(url)
    if not item_titles:
        print("there are no item names on the specified page or the parameters are incorrect")
        continue
    
    data = {"item_titles": item_titles}
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"data_{current_datetime}.json"
    
    with open(filename, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    print(f"items name successfully saved: {filename}")
    
    while True:
        repeat = input("lets try again? (y/n): ")
        if repeat.lower() == "y":
            break
        elif repeat.lower() == "n":
            exit()
