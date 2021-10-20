
import tkinter as tk
from bs4 import BeautifulSoup
import requests
import lxml
import webbrowser
import random


root = tk.Tk()
root.geometry("400x100")

root.title("Generate random wikipedia article")


result = requests.get("https://en.wikipedia.org/wiki/Wikipedia:Featured_articles")
print(result)
content = result.content
soup = BeautifulSoup(content, "lxml")
urls = []
for li_tag in soup.find_all("li"):
    a_tag = li_tag.find("a")
    try:
        urls.append(a_tag.attrs["href"])
    except:
        pass
urls_2 = []
for x in range(1000):
    urls_2.append(urls[x])


def generate():
    webbrowser.open("https://en.wikipedia.org" + random.choice(urls_2), new=2)
generate_button = tk.Button(root, text="Generate", height=3, width=40, command=generate)
generate_button.place(x=60, y=30)




root.mainloop()