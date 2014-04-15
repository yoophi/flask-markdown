import codecs
import markdown
import os
import json
from flask import Flask, render_template

app = Flask(__name__)
current_dir = os.path.abspath(os.path.dirname(__file__))

@app.route('/<book>/book.js')
def book_js(book):
    filename = os.path.join(current_dir, 'pages', book, "book.json")
    input_file = codecs.open(filename, mode="r", encoding="utf-8")
    text = input_file.read()

    book = json.loads(text)
    components = json.dumps(book['components'])
    chapters = json.dumps(book['chapters'])
    metadata = json.dumps(book['metadata'])

    return render_template('book.js', components=components, chapters=chapters, metadata=metadata)


@app.route('/')
def index():
    return 'index'

@app.route('/<book>/')
def book_index(book):
    print 'book_index'
    print book
    return render_template('index.html', book=book)


@app.route('/<book>/pages/<pagename>.html')
def page(book, pagename):
    filename = os.path.join(current_dir, 'pages', book, "%s.md" % pagename)
    input_file = codecs.open(filename, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)
    return html


# html = markdown.markdown(your_text_string)
#
# input_file = codecs.open("some_file.txt", mode="r", encoding="utf-8")
# text = input_file.read()
# html = markdown.markdown(text)
