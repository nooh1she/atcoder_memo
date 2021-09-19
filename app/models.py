from django.db import models
from django.contrib.postgres.fields import JSONField

import json

# Create your models here.

#ログイン時に使用するUserモデル
class User(models.Model):

    user_name = models.CharField('ユーザー名', max_length = 50)
    password = models.CharField('パスワード', max_length = 50)


#問題のモデル
class Problem(models.Model):

    #問題のタイトル
    name = models.CharField('問題', max_length = 50)
    #問題のatcoder URL
    site_url = models.URLField('URL', max_length = 100)
    #登録したタグ
    tags = models.TextField('タグ', blank = True)
    #書いたコード
    code = models.TextField('自分の書いたコード', blank = True)
    #メモ
    memo = models.TextField('メモ', blank = True)


#JSONクラスにおいて、非ASCIIでエスケープしないよう設定
class StandardJSONField(JSONField):
    def get_prep_value(self, value):
        if value is not None:
            return json.dump(value, ensure_ascii=False)
        return value

#JSONFieldで作成するクラス
class SearchTag(models.Model):

    """tagごとに問題をまとめる
    JSONFieldに以下のように登録する
    ・問題a,b,cが存在するとき
    JSONField - ['tag1'] : [a,b]
              - ['tag2'] : [b,c]
              ...
    """
    #JSONClass
    tag_dic = StandardJSONField(blank = True)


    
