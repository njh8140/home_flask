from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')
# url_prefix = '/'
# 밑에 접속하는 주소 기본값
# 예) url_prefix = '/main'
# localhost:5000/main/

@bp.route('/hello') # 기본주소 뒤에 hello 입력하면 'Hello, Pybo!'
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/') # 기본주소
def index():
    return 'Pybo index'
