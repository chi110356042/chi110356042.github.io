from flask import Flask
from flask import render_template
from flask import url_for


app = Flask(__name__)



#home page
@app.route('/')
def home():
    return render_template('index.html')

#about page
@app.route('/about')
def about():
    return render_template('about.html')

#animal page
@app.route('/animal')
def animal():
    return render_template('Animal.html')

#food page
@app.route('/food')
def food():
    return render_template('food.html')


#life page
@app.route('/life')
def life():
    return render_template('Life.html')

#life_together page
@app.route('/life_together')
def life_together():
    return render_template('Life_together.html')

#meme page
@app.route('/meme')
def meme():
    return render_template('Meme.html')

#pay page
@app.route('/pay')
def pay():
    return render_template('pay.html')



if __name__=="__main__":
    app.run(debug=True) #Start server


