from flask import Flask, render_template, request
from PlotSystems import plot_thomas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    b = float(request.form['b'])
    fig = plot_thomas([0.2, 0.1, 0.1], b=b)
    return fig.to_html(full_html=False)

if __name__ == '__main__':
    app.run(debug=True)
