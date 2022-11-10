import requests
from bs4 import BeautifulSoup
import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 175)

def get_news_report():
    #request the homepage and create a Beautiful Soup object
    home_url = "https://www.aljazeera.com/"
    home_page = requests.get(home_url)
    home_soup = BeautifulSoup(home_page.content, "html.parser")

    #variable which will hold the completed news report
    news_report = ""

    #find all of the headline articles and store them as a list
    headline_articles = home_soup.find_all("li", class_="fte-featured-articles-list__item")

    #iterate through each of the articles to extract the text and their corresponding links
    for h_article in headline_articles:
        headline = h_article.find("a", class_="fte-article__title-link u-clickable-card__link")

        #select the article's link
        article_link = home_url + headline["href"]

        #request the article and create a new BS object
        article_page = requests.get(article_link)
        article_soup = BeautifulSoup(article_page.content, "html.parser")

        #select the header element
        article_header = article_soup.select("header", class_="article-header")


        #select the title and subtitle
        article_title = article_header[1].h1.text
        article_subtitle = article_header[1].em.text

        news_report += article_title + "," + article_subtitle + ". "

        #add in a one second delay to avoid spamming the website
        time.sleep(1)

    return news_report


engine.say(get_news_report())
engine.runAndWait()


