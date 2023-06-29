from flask import Flask,render_template
from newsapi import NewsApiClient

app =Flask(__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="f4c5d7534dea4c5b854bd30e6688339f")
    topheadlines = newsapi.get_top_headlines(
    sources='al-jazeera-english'
   )
    articles =topheadlines['articles']
    desc =[]
    news=[]
    img=[]
    content=[]  
    for i in range(len(articles)):
        myarticles=articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['content'])
        
        
    mylist =zip(news, desc,img,content)
        
    return render_template('index.html' , context=mylist)
    
if __name__ =="__main__":
    app.run(debug=True)
    
        