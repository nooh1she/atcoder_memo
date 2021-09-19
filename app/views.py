from django.shortcuts import render
from django.shortcuts import get_list_or_404, render, redirect
from django.views.generic.list import ListView

from app.models import Problem

# Create your views here.
def top(request):
    return render(request, 'app/top.html')

def submit(request):
    return render(request, 'app/submit.html')

#問題の登録
def form_submit(request):

    problem = Problem()
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
        """tagで、'#'で登録されたタグを分離"""
        tags = tags.split('#')[1::]

        #レコードに挿入
        problem.objects.create(name = name, site_url = site_url, 
                                tags = tags, code = code, memo = memo)
        problem.save()

    else:
        print("test")
        return render(request, 'app/top.html')
    
    return render(request, 'app/top.html')


