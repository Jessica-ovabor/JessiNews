from flask import Flask, render_template,request
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="f4c5d7534dea4c5b854bd30e6688339f")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')
    articles = topheadlines['articles']
    news = []
    desc = []
    img = []
    content = []
  
    for article in articles:
        news.append(article['title'])
        desc.append(article['description'])
        img.append(article['urlToImage'])
        content.append(article['content'])
        
    mylist = zip(news, desc, img, content)
        
    return render_template('index.html', context=mylist)
@app.route('/')
def aljazeera():
    newsapi = NewsApiClient(api_key="f4c5d7534dea4c5b854bd30e6688339f")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
    articles = topheadlines['articles']
    news = []
    desc = []
    img = []
    content = []
  
    for article in articles:
        news.append(article['title'])
        desc.append(article['description'])
        img.append(article['urlToImage'])
        content.append(article['content'])
        
    my_list = zip(news, desc, img, content)
        
    return render_template('index.html', context=my_list)


#subscribe email
@app.route('/subscribe', methods=['POST'])
def subscribe():
    subscribed_emails =[]
    email = request.form.get('email')
    if email:
        subscribed_emails.append(email)
        return "Thank you for subscribing to our daily news outlets!"
    else:
        return "Invalid email."


if __name__ == "__main__":
    app.run(debug=True)
