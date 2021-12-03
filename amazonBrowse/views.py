from django.shortcuts import redirect, render
from django.http import HttpResponse
from .application import write_csv
from .models import AmazonGoods
from django.template import loader

# Create your views here.
def index(request):
    latest_amazon_goods_list = AmazonGoods.objects.all()
    template = loader.get_template('amazonBrowse/index.html')
    context = {
        'latest_amazon_goods_list':latest_amazon_goods_list,
    }
    return HttpResponse(template.render(context, request))

# ajaxでurl指定したメソッド
def call_write_csv(request):
    if request.method == 'GET':
        soup = write_csv.ama(request.GET.get("input_data"))
        write_csv.get_info(soup)
        return HttpResponse()