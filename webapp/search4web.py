from flask import Flask, render_template, request, redirect
from vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'app_request', res: str) -> None:
    with open('webapp_search.log', 'a') as log:
        print(req, res, file=log)


@app.route('/search4',  methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


app.run(debug=True)

