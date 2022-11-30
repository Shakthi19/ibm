from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/search')
def search():
   return render_template('search.html')   

@app.route('/contact.html')
def contact():
   return render_template('contact.html')

if __name__ == '__main__':
   app.run()
