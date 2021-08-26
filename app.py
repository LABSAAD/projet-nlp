from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline
import math
import sentiment_analysis

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] =r"\Users\labrhaddasaad\Desktop\projet_nlp\static"

@app.route('/index',methods=['GET','POST'])

def index():

    if request.method == 'POST':
        
        text=request.form["text"]

        lang=request.form["lang"]

        if lang=="1":
            result= sentiment_analysis.ang_sentiment(text)
            if result[0]['score']<0.55 and result[0]['score']>0.45:
                result[0]['label']="NEUTRAL"
        elif lang=="2":
            result= sentiment_analysis.fr_sentiment(text)
            if result[0]['score']<0.55 and result[0]['score']>0.45:
                result[0]['label']="NEUTRAL"
        else:
            result= sentiment_analysis.ar_sentiment(text)
            if result[0]['label']=="LABEL_0":
                result[0]['label']="NEUTRAL"
                
            elif result[0]['label']=="LABEL_1":
                result[0]['label']="NEGATIVE"

            else:
                result[0]['label']="POSITIVE"
            
        print(result)

        n = ((100-math.floor(result[0]['score']*100))/100)*math.pi*(115*2)

        print(n)

        return render_template("index.html",number= n,text=text ,note=result[0]['label'],result=result[0]['score'])
 
    return render_template("index.html",number=720,result=0)

  
if __name__ == "__main__":
    app.run()
