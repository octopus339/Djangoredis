from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection


def index(request):
    strict_redis = get_redis_connection()
    strict_redis.set('a',1)
    strict_redis.set('b',2)

    a= strict_redis.get('a')
    b = strict_redis.get('b')
    text = '%s %s'%(a.decode(),b.decode())


def set_session(request):
    """"保存session数据"""

    request.session['username'] = 'Django'
    request.session['verify_code'] = '123456'
    return HttpResponse('保存session数据成功')


def get_session(request):
    """获取session数据"""

    username = request.session.get('username')
    verify_code = request.session.get('verify_code')
    text = 'username=%s, verify_code=%s' % (username, verify_code)
    return HttpResponse(text)