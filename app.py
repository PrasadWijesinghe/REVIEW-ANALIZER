from flask import Flask, render_template, request, redirect
from prediction import preprocessing, vectorizer, get_prediction, tokens

app = Flask(__name__)

data = dict()

reviews = ['Good products', 'Bad product', 'I like it']
positive = 2
negative = 1

@app.route("/")
def index():
    data['reviews'] = reviews
    data['negative'] = negative
    data['positive'] = positive
    return render_template('index.html', data=data)


@app.route("/",methods = ['post'])
def my_post():
    text = request.form['text']
    preprocessed_text = preprocessing(text)
    vectorized_text = vectorizer(preprocessed_text, tokens) 
    prediction = get_prediction(vectorized_text)

    if prediction == 'negative':
        global negative
        negative += 1
    else:
        global positive
        positive += 1

    
    reviews.insert(0, text)
    return redirect(request.url)




if __name__ == "__main__":
    app.run()