import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_correction(text, tone="丁寧"):
    tone_detail = {
        "丁寧": "丁寧なトーン",
        "カジュアル": "カジュアルなトーン",
        "難しい文体": "専門的で難解な文体",
        "フレンドリー": "親しみやすくフレンドリーなトーン",
        "ビジネス": "実務的で堅めのビジネス文書のトーン"
    }
    tone_prompt = tone_detail.get(tone, tone)

    prompt = f"""
以下の日本語文章の文法や表現をチェックして、間違いがあれば修正案を示してください。
さらに、{tone_prompt}で、より自然で読みやすい校正案を具体的に示してください。

文章:
{text}

修正案・校正案:
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()


def generate_rewrite(text, tone="丁寧"):
    tone_detail = {
        "丁寧": "丁寧なトーン",
        "カジュアル": "カジュアルなトーン",
        "難しい文体": "専門的で難解な文体",
        "フレンドリー": "親しみやすくフレンドリーなトーン",
        "ビジネス": "実務的で堅めのビジネス文書のトーン"
    }
    tone_prompt = tone_detail.get(tone, tone)

    prompt = f"""
以下の日本語文章を{tone_prompt}で、より魅力的でわかりやすくリライトしてください。
元の意味を変えずに、簡潔かつ読みやすい文章にしてください。

文章:
{text}

リライト案:
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()
