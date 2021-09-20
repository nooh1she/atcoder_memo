from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
import re

from app.models import Problem, SearchTag, User
from .validation import validation_name, validation_url

#トップページ
def top(request):

    return render(request, 'app/top.html')


#問題の登録画面への遷移
def create(request):

    return render(request, 'app/create.html')


#問題の登録
def done_create(request):

    if request.method == 'POST':

        flag = True

        #name
        name = request.POST['name']
        validation_url(name)
        #url
        site_url = request.POST['site_url']
        #tag
        tags = request.POST['tags']
        #code
        code = request.POST['code']
        #memo
        memo = request.POST['memo']
        
        
        """tagで、'#', ' ', ',', で登録されたタグを分離"""
        #tags = tags.split('#')[1::]
        tag_new = ''
        for chara in re.split('#| |,', tags):
            print(chara)
            tag_new += chara + ' '

        print('tag_new:', tag_new)

        #バリデーション
        #valid_flag = valid_problem(name, site_url, tags, code, memo)


        #レコードに挿入
        Problem.objects.create(name = name, site_url = site_url, 
                                tags = tag_new, code = code, memo = memo)

    else:
        print("test")
        return render(request, 'app/done_create.html')
    
    return render(request, 'app/done_create.html')


#問題の編集画面への遷移
def modify(request, pk):
    problem = get_object_or_404(Problem, pk = pk)
    return render(request, 'app/modify.html', {'Problem': problem, 'pk': pk})


#問題の編集
def done_modify(request, pk):

    problem = get_object_or_404(Problem, pk = pk)
    if request.method == 'POST':
        #name
        problem.name = request.POST['name']

        #site_url
        problem.site_url = request.POST['site_url']

        #tags
        problem.tags = request.POST['tags']

        #code
        problem.code = request.POST['code']

        #memo
        problem.code = request.POST['memo']

        problem.save()

    else:
        return render(request, 'app/top.html')

    return render(request, 'app/done_modify.html', {'Problem': problem, 'pk': pk})


#問題の削除
def done_delete(request, pk):

    Problem.objects.filter(pk = pk).delete()
    return render(request, 'app/done_delete.html')


#問題の一覧画面への遷移
def items_problem(request):

    items = Problem.objects.all()
    return render(request, 'app/items.html', {'items': items})


#問題の詳細確認
def content_problem(request, pk):

    problem = get_object_or_404(Problem, pk=pk)
    return render(request, 'app/content.html', {'Problem': problem, 'pk': pk} )





