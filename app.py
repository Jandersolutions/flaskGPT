from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Defina sua chave da API da OpenAI aqui
openai.api_key = 'sua_chave_da_openai'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=50
    )
    bot_response = response.choices[0].text.strip()
    return {'bot_response': bot_response}

if __name__ == '__main__':
    app.run(debug=True)
 
