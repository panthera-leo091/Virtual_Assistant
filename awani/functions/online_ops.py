import requests
import pywhatkit as pkit
import wikipedia as wiki


NEWS_API_KEY = "7318af2657e04bbd92cf95e1634e2703"
OPENWEATHER_APP_ID = "2f1702c5aaf758683ce38b7823d1d76a"
TMDB_API_KEY = "705eb5dc12551a74ccd3e8bec3ec6c39"



def search_Wiki(query):
    res = wiki.summary(query, sentences = 2)
    return res

def play_Youtube(video):
    pkit.playonyt(video)

def search_Google(query):
    pkit.search(query)

def send_wp_msg(number, message):
    pkit.sendwhatmsg_instantly(f"+91{number}", message)


# key def fun
def get_latest_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]  #it will only return 5 top news only

def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


# print(get_latest_news())
# print(get_weather_report("lucknow"))
# print(get_trending_movies())
# print(get_random_joke())
# print(get_random_advice())