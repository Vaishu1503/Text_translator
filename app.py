from flask import Flask, request, jsonify, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    src_lang = request.form['src_lang']
    dest_lang = request.form['dest_lang']
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
