from django.db.models.fields.related_descriptors import ManyToManyDescriptor
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from django.db.models import Q
import re

from app.models import Problem, Tag
from .validation import validation_name, validation_url

from django.contrib.auth.decorators import login_required


#トップページ
@login_required
def top(request):
    print(type(Problem.objects.all()))
    return render(request, 'app/top.html')


#問題の登録画面への遷移
@login_required
def create(request):
    return render(request, 'app/create.html')


#問題の登録
@login_required
def done_create(request):

    #既存のタグ一覧
    all_tag_list = {}
    for t in Tag.objects.all():
        all_tag_list[str(t)] = True

    print('all:', all_tag_list)
    if request.method == 'POST':

        flag = True
        #userid
        u_id = request.user.id
        #name
        name = request.POST['name']
        #url
        site_url = request.POST['site_url']
        #tag
        tag_visible = request.POST['tags']
        #code
        code = request.POST['code']
        #memo
        memo = request.POST['memo']
        
        
        """tagで、'#', ' ', ',', で登録されたタグを分離"""
        #tags = tags.split('#')[1::]
        tag_new = ''
        tag_list = []
        for chara in list(filter(None, re.split('#| |,', tag_visible))):
            if (len(chara) <= 50):
                print('chara:', chara)
                tag_new += chara + ' '

                #タグを重複して作らないように、既存のタグをチェックする
                if chara not in all_tag_list:
                    t = Tag(tag_name = chara)
                    tag_list.append(t)
                    t.save()
                else:
                    #タグが存在するならオブジェクトを取得する
                    tag_list.append(Tag.objects.get(tag_name = chara))

        print('tag_new:', tag_new)
        print('tag_list:', tag_list)

        #nameバリデーション
        #name = validation_name(name)

        #urlバリデーション
        #site_url = validation_url(site_url)


        #要素の登録
        problem = Problem()
        problem.u_id = u_id
        problem.name = name
        problem.site_url = site_url
        problem.tags_visible = tag_new
        problem.code = code
        problem.memo = memo

        problem.save()

        problem.tags.set(tag_list)

        #レコードに挿入
        #Problem.objects.create(u_id = u_id, name = name, site_url = site_url, 
        #                        tags = tag_new, code = code, memo = memo)

        print(problem.tags.all())
        print(Problem.objects)

    else:
        print("test")
        return render(request, 'app/done_create.html')
    
    #文字列で見せる用のタグをhtmlに返す
    return render(request, 'app/done_create.html', {tag_new: tag_new})


#問題の編集画面への遷移
@login_required
def modify(request, pk):
    problem = get_object_or_404(Problem, pk = pk, u_id = request.user.id)
    return render(request, 'app/modify.html', {'Problem': problem, 'pk': pk})


#問題の編集
@login_required
def done_modify(request, pk):

    #既存のタグ一覧
    all_tag_list = {}
    for t in Tag.objects.all():
        all_tag_list[str(t)] = True

    problem = get_object_or_404(Problem, pk = pk, u_id = request.user.id)
    if request.method == 'POST':
        #name
        problem.name = request.POST['name']
        #site_url
        problem.site_url = request.POST['site_url']
        #code
        problem.code = request.POST['code']
        #memo
        problem.memo = request.POST['memo']

        #タグを分離
        tags = request.POST['tags']
        tag_new = ''
        tag_list = []
        for chara in list(filter(None, re.split('#| |,', tags))):
            if (len(chara) <= 50):
                tag_new += chara + ' '
                print('chara:', chara)

                #タグを重複して作らないように、既存のタグをチェックする
                if chara not in all_tag_list:
                    t = Tag(tag_name = chara)
                    tag_list.append(t)
                    t.save()
                else:
                    tag_list.append(Tag.objects.get(tag_name = chara))

        problem.tags_visible = tag_new
        problem.save()      
        problem.tags.set(tag_list)

    else:
        return render(request, 'app/top.html')

    return render(request, 'app/done_modify.html', {'Problem': problem, 'pk': pk})


#問題削除の確認
@login_required
def confirm_delete(request, pk):
    return render(request, 'app/confirm_delete.html', {'pk' : pk})


#問題の削除
@login_required
def delete(request, pk):

    problem = Problem.objects.get(pk = pk)

    if problem.u_id != request.user.id:
        return redirect('app:top')

    problem.tags.clear()
    problem.delete()
    #Problem.objects.filter(pk = pk).delete()
    return redirect('app:items')


#問題の一覧画面への遷移
@login_required
def items_problem(request):
    items = Problem.objects.filter(u_id = request.user.id)
    return render(request, 'app/items.html', {'items': items})


#問題の詳細確認
@login_required
def content_problem(request, pk):

    problem = get_object_or_404(Problem, pk = pk, u_id = request.user.id)
    return render(request, 'app/content.html', {'Problem': problem, 'pk': pk})


#問題の検索
@login_required
def search_problem(request):
    
    if request.method == 'POST':

        #既存のタグ一覧
        all_tag_list = {}
        for t in Tag.objects.all():
            all_tag_list[str(t)] = True

        tags_search = request.POST['tags_search']

        if tags_search == '':
            return redirect('app:items')

        #タグを分離
        tag_new = ''
        tag_list = []
        for chara in list(filter(None, re.split('#| |,', tags_search))):
            if len(chara) <= 50 and chara in all_tag_list:
                tag_list.append(chara)

        #Qにタグ情報を追加しOR検索
        q_tags_search = Q()
        for item in tag_list:
            q_tags_search.add(Q(u_id = request.user.id, tags=Tag.objects.get(tag_name = item)), Q.OR)

        #タグの重複を消す
        if len(tag_list) == 0:
            search_result = []
        else:
            search_result = Problem.objects.filter(q_tags_search).distinct()

        print(search_result)

        return render(request, 'app/items.html', {'search_result': search_result})

    return render(request, 'app/top.html')


#ログアウトの確認
def confirm_signout(request):
    return render(request, 'app/confirm_signout.html')



