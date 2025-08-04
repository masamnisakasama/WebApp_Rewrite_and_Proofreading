FROM python:3.10-slim

WORKDIR /app

COPY . /app

# 日本語表示の問題を回避する　by　環境変数
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
