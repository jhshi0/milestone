from flask import Flask, render_template, request, redirect
import bokeh, requests, pandas
from ipynb.fs.full.StockTickerPlot import plot

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=["POST"])
def read(): 
    usr_tick=request.form["ticker"]
    print(type(usr_tick))
    return render_template('display_plot.html')

if __name__ == '__main__':
  app.run(port=33507)
