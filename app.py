from flask import Flask, render_template
from data import Articles

app = Flask(__name__)
Articles = Articles()


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data_visualization')
def about():
    return render_template('data_visualization.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


if __name__ == '__main__':
    app.run(debug=True)
