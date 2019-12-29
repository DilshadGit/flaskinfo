from flask import (
	Flask,
	render_template,
	url_for,
)

app = Flask(__name__)

posts = [
	{
		'title': 'Python3',
		'author': 'Dilshad',
		'date': '01 Dec 2019',
		'content': ' Welcome to Python3'
	},
	{
		'title': 'Django3',
		'author': 'Azad',
		'date': '01 Nov 2019',
		'content': ' Welcome to Django3'
	},
	{
		'title': 'Flask',
		'author': 'Shvan',
		'date': '01 Aug 2018',
		'content': ' Welcome to Flask'
	}
]


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', title='Post', posts=posts)


@app.route('/about')
def about():
	return render_template('about.html', title='About', posts=posts)


if __name__ == '__main__':
	app.run(debug=True)