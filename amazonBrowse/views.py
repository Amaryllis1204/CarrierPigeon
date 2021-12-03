from django.shortcuts import render
from django.http import HttpResponse
# application/write_data.pyをインポートする
from .application import write_data, write_csv
from .models import AmazonGoods
from django.template import loader
import pandas as pd
import sqlite3

# Create your views here.
def index(request):
    latest_amazon_goods_list = AmazonGoods.objects.all()
    template = loader.get_template('amazonBrowse/index.html')
    context = {
        'latest_amazon_goods_list':latest_amazon_goods_list,
    }
    return HttpResponse(template.render(context, request))

# ajaxでurl指定したメソッド
def call_write_data(req):
    if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        write_data.write_csv(req.GET.get("input_data"))

        data = write_data.return_text()

        return HttpResponse(data)

def call_write_csv(request):
    if request.method == 'GET':
        soup = write_csv.ama(request.GET.get("input_data"))
        write_csv.get_info(soup)
        return HttpResponse(request)