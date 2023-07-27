# 기본 파이썬 파일.
# 여기에 서버를 빌드할 서버 로직과 라우팅을 넣게 된다.

from flask import Flask, render_template, request

app = Flask(__name__)
