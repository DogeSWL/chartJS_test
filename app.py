from flask import Flask
from flask import Markup
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def chart():
    legend = 'Temperatures'
    times = ['12:00PM', '12:10PM', '12:20PM', '12:30PM', '12:40PM', '12:50PM',
             '1:00PM', '1:10PM', '1:20PM', '1:30PM', '1:40PM', '1:50PM',
             '2:00PM', '2:10PM', '2:20PM', '2:30PM', '2:40PM', '2:50PM']
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
              61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
              70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    return render_template('chart.html', values=temperatures, labels=times, legend=legend)


if __name__ == "__main__":
    app.run()
