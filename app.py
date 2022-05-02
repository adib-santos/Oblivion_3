from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index(): 
    return render_template('/pages/index.html')

@app.route('/about')
def about(): 
    return render_template('/pages/about.html')

@app.route('/contact')
def contact(): 
    return render_template('/pages/contact.html')

@app.route('/glossary')
def glossary(): 
    return render_template('/pages/glossary.html')

@app.route('/cases')
def cases(): 
    return render_template('/pages/usecases.html')

if __name__ == '__main__': 
    app.run()