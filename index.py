import pandas as pd # type: ignore
import requests  # type: ignore
from bs4 import BeautifulSoup# type: ignore
from flask import Flask,render_template # type:ignore
app = Flask(__name__)
def webScraping(textContent):
    soup = BeautifulSoup(textContent,'lxml')
    #print(soup.prettify())
    image = soup.find_all('img',class_="avatar")
    print(image[0].get('ayush',"Not found "))
    return image[0]['src']

@app.route('/')
def home():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    #textContent = requests.get("https://github.com/002ayush",headers=headers).text
    #imageUrl = webScraping(textContent)
    textContent = requests.get("https://github.com/002ayush?tab=repositories",headers=headers).text
    soup = BeautifulSoup(textContent,'lxml')

    languageUsed = soup.find_all('span',itemprop= "programmingLanguage")
   # print(languageUsed)
    languages = []
    for lang in languageUsed:
        languages.append(lang.text)
    languageItems = {}
    for i in languages:
        if (i in languageItems):
            languageItems[i] = languageItems[i] + 1
        else:
            languageItems[i] = 1
    object = dict(sorted(languageItems.items(), key=lambda item: item[1], reverse=True))

    labels = []
    data = []
    for i in object:
        labels.append(i)
        data.append(object[i])
    
    return render_template('index.html',labels=labels[:6],data=data[:6])




















































if __name__ == "__main__":
    #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    #textContent = requests.get("https://github.com/002ayush",headers=headers).text
    # webScraping(textContent)
    app.run(debug=True)
   # print(textContent)
    