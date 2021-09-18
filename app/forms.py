from django.forms import ModelForm
from app.models import Problem

#問題の登録フォーム
class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = ('name', 'site_url', 'tag', 'code', 'memo')
