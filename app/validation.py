from urllib import request, error
import urllib

from .models import Problem
from .exceptions import Name_Error, UrlError


#nameのバリデーション
def validation_name(name):

    result = name

    if len(name) > 50:
        result = Name_Error('名前は50文字以下にしてください')
    elif len(name) == 0:
        result = Name_Error('問題名を入力してください')

    print(result)
    return result


#urlのバリデーション
def validation_url(url):

    result = url
    try:
        f = request.urlopen(url)
        f.close()
    except:
        result = UrlError('urlが不正です')
    
    return result
