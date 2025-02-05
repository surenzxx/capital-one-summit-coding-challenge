from flask import Flask, render_template
from data import Articles
import json
import plotly
import pandas as pd
import numpy as np

app = Flask(__name__)
Articles = Articles()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data_visualization')
def data_visualization():
    rng = pd.date_range('1/1/2011', periods=7500, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)

    graphs = [
        dict(
            data=[
                dict(
                    x=[1, 2, 3],
                    y=[10, 20, 30],
                    type='scatter'
                ),
            ],
            layout=dict(
                title='first graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=[1, 3, 5],
                    y=[10, 50, 30],
                    type='bar'
                ),
            ],
            layout=dict(
                title='second graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=ts.index,  # Can use the pandas data structures directly
                    y=ts
                )
            ]
        )
    ]

    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('data_visualization.html',
                           ids=ids,
                           graphJSON=graphJSON)

# @app.route('/data_visualization')
# def data_visualization():
#     return render_template('data_visualization.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


if __name__ == '__main__':
    app.run(debug=True)
