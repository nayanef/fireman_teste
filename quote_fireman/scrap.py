import requests
from bs4 import BeautifulSoup
from quote_fireman.wsgi import *
from quotes.models import Quote



def scrap():
    
    i = 1

    while True:
        url = 'https://quotes.toscrape.com/page/' + str(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        if(soup.find(class_='quote')):
            quotes = soup.find_all(class_='quote')
            for q in quotes:
                q_text = q.find(class_='text').text
                q_author = q.find(class_='author').text
                quote = Quote()
                if Quote.objects.filter(text=q_text).exists():
                    print("Citação já existe")
                else:                
                    quote.text = q_text
                    quote.author = q_author
                    quote.save()   
        else:
            break         

        i = i + 1

if __name__ == '__main__':
    scrap()