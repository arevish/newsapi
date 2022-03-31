# read latest new paper

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Today's latest news from times of india.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ec49a4af13924dffa6ca6b8f6ace01bf"
    # url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=ec49a4af13924dffa6ca6b8f6ace01bf"
    
    # data = requests.get(url=url)
    # india = data.json()
    # # print(india['articles'][0]['description'])
    # for i in range(20):
    #     print(i, india['articles'][i]['source']['name'])
    # no = int (input("choose the news paper: "))
    # speak(india['articles'][no]['title'])
    # print("for more",india['articles'][no]['url'])
    # speak(india['articles'][no]['content'])
    # speak(india['articles'][no]['description'])
  
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']

    for article in arts:
        print(article['title'],"\n")
        speak(article['title'])
        print("For more click on the link: ",article['url'],"\n")
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...to today's latest news")


