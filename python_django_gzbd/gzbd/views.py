import datetime
import json
import random;

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from gzbd.models import *;


# Create your views here.
def hello_world(request):
    user = User(user_name="Jayoung" + str(random.randint(1, 10)), password="111111",
                create_date=datetime.datetime.now(), user_email="JayoungLee@163.com");
    # user.save();

    users = User.objects.all();
    print("==== 查询所有 ====", users);

    users = User.objects.filter(id=1);
    print("==== 条件查询 ====", users);

    user = User.objects.get(id=1);
    print("==== 获取单个对象 ====", user);

    # 更新数据
    # user.user_name = "Ja" + str(random.randint(1, 10));
    user.user_email = "jiayounglee";
    user.save();

    users_json = serializers.serialize("json", User.objects.order_by("user_name")[0:2]);
    # json.loads 转化为json类型
    return JsonResponse(json.loads(users_json), safe=False);


def test_index(request):
    context = {};
    context["name"] = "Jayoung";
    context["name_list"] = ["Jayoung", "XiaoYong"];
    context["person"] = {"name": "XiaoYong", "age": 18};
    context["person1"] = {"name": "XiaoYong", "age": 18};
    context["birthday"] = datetime.datetime.now();
    context["number"] = "2048";
    context["url"] = "http://www.baidu.com";
    context["isman"] = True;
    return render(request, "test/index.html", context);


def index(request):
    context = {};
    return render(request, "index.html", context);


def index_simple(request):
    return render(request, "indexSimple.html");


def account_login(request):
    return render(request, "account/login.html");


def account_register(request):
    return render(request, "account/register.html");


def common_dashboard(request):
    return render(request, "common/dashboard.html");
