import os
from flask import Flask, render_template, request
from rewrite_engine import generate_correction, generate_rewrite

app = Flask(__name__)

MAX_LENGTH = 1000

@app.route('/', methods=['GET', 'POST'])
def index():
    correction = None
    rewrite = None
    error = None
    input_text = ''
    selected_tone = '丁寧'

    if request.method == 'POST':
        input_text = request.form.get('input_text', '').strip()
        selected_tone = request.form.get('tone', '丁寧')

        if not input_text:
            error = "文章を入力してください。"
        elif len(input_text) > MAX_LENGTH:
            error = f"入力は{MAX_LENGTH}文字以内でお願いします。現在の文字数: {len(input_text)}"
        else:
            correction = generate_correction(input_text, selected_tone)
            rewrite = generate_rewrite(input_text, selected_tone)

    return render_template('index.html',
                           correction=correction,
                           rewrite=rewrite,
                           input_text=input_text,
                           error=error,
                           selected_tone=selected_tone,
                           max_length=MAX_LENGTH)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Cloud Runが指定するポートを取得
    app.run(host='0.0.0.0', port=port, debug=True)
