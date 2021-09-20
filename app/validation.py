from urllib import request, error
import urllib

from .models import Problem
from .exceptions import NameError, UrlError


#nameのバリデーション
def validation_name(name):

    reuslt = name
    if len(name) > 50:
        retult = NameError('名前は50文字以下にしてください')
    elif len(name) == 0:
        result = NameError('問題名を入力してください')

    return reuslt


#urlのバリデーション
def validation_url(url):

    result = url
    try:
        f = request.urlopen(url)
        f.close()
    except:
        result = UrlError('urlが不正です')
    
    return result
