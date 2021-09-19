from django.shortcuts import render
from django.shortcuts import get_list_or_404, render, redirect
from django.views.generic.list import ListView

from app.models import Problem

# Create your views here.
def top(request):
    return render(request, 'app/top.html')

#問題の登録画面への遷移
def move_create(request):
    return render(request, 'app/move_create.html')

#問題の登録
def create_problem(request):

    if request.method == 'POST':
        #name
        name = request.POST['name']
        print(name)
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
        cnt = 0
        split_char = ['#', ' ', ',']
        for chara in tags:
            if chara in split_char:
                if cnt != 0:
                    tag_new += ' '
            else:
                tag_new += chara
            cnt += 0

        print(tag_new)

        #レコードに挿入
        Problem.objects.create(name = name, site_url = site_url, 
                                tags = tag_new, code = code, memo = memo)

    else:
        print("test")
        return render(request, 'app/top.html')
    
    return render(request, 'app/top.html')


#問題の編集画面への遷移
def move_modify(request, problem_id=None):
    pass
#問題の編集
def modify_problem(request):
    pass


#問題の一覧画面への遷移
def items_problem(request):
    items = Problem.objects.all()
    return render(request, 'app/items.html', {'items':items})




