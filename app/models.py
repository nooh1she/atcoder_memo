from django.db import models
from django.contrib.postgres.fields import JSONField

import json

from django.db.models.base import Model

# Create your models here.

class Tag(models.Model):

    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


#問題のモデル
class Problem(models.Model):

    #ユーザーネーム
    u_id = models.IntegerField('ユーザid')
    #問題のタイトル
    name = models.CharField('問題', max_length = 50)
    #問題のatcoder URL
    site_url = models.URLField('URL', max_length = 150)
    #登録したタグ(内部)
    tags = models.ManyToManyField(Tag, blank=True)
    #タグ(見せる用)
    tags_visible = models.TextField('タグ', blank=True)
    #書いたコード
    code = models.TextField('自分の書いたコード', blank = True)
    #メモ
    memo = models.TextField('メモ', blank = True)


#JSONクラスにおいて、非ASCIIでエスケープしないよう設定
"""class StandardJSONField(JSONField):

    def get_prep_value(self, value):
        if value is not None:
            return json.dump(value, ensure_ascii=False)
        return value


#JSONFieldで作成するクラス
class SearchTag(models.Model):

    tagごとに問題をまとめる
    JSONFieldに以下のように登録する
    ・問題a,b,cが存在するとき
    JSONField - ['tag1'] : [a,b]
              - ['tag2'] : [b,c]
              ...
    
    #JSONClass
    tag_dic = StandardJSONField(blank = True)"""


    
