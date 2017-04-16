import pygal      
from flask import render_template,Flask
app = Flask(__name__)
@app.route('/charts/')
def line_route():
	app = Flask(__name__)                                                 # First import pygal
	bar_chart = pygal.Bar()                                            # Then create a bar graph object
	bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
	# bar_chart.render_to_file('bar_chart.svg')                          # Save the svg to a file
	chart = bar_chart.render_data_uri()
	return render_template( 'chart.html', chart = chart)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')