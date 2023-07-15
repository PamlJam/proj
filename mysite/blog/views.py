from django.shortcuts import render
from .models import Article

def index(request):

    ls = Article.objects.all()
    # 文章列表
    ls.order_by('-pub_date')
    # 重新排序
    context = {
    # 上下文字典，传入模板提供数据参数
        'article_list': ls,
    }
    return render(request, 'blog/index.html', context)


from django.shortcuts import get_object_or_404

def detail(request, article_id):
    a = get_object_or_404(Article, id = article_id)
    
    context = {
        'article': a,
    }

    return render(request, 'blog/detail.html', context)