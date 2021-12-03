from django.shortcuts import redirect, render
from django.http import HttpResponse
from .application import read_site
from .models import AmazonOnlyGoods, AmazonDomainOnlyGoods, AmazonOnlyBrand
from django.template import loader

# Create your views here.
def index(request):
    amazon_only_goods = AmazonOnlyGoods.objects.all()
    amazon_domain_only_goods = AmazonDomainOnlyGoods.objects.all()
    amazon_only_brand = AmazonOnlyBrand.objects.all()
    template = loader.get_template('amazonBrowse/index.html')
    context = {
        'amazon_only_goods':amazon_only_goods,
        'amazon_domain_only_goods':amazon_domain_only_goods,
        'amazon_only_brand':amazon_only_brand
    }
    return HttpResponse(template.render(context, request))

# ajaxでurl指定したメソッド
def update_db(request):
    if request.method == 'GET':
        soup1 = read_site.amazon_only(request.GET.get("input_data"))
        soup2 = read_site.amazon_domain_only(request.GET.get("input_data"))
        soup3 = read_site.amazon_only_brand(request.GET.get("input_data"))
        read_site.get_info(soup1, "amazonBrowse_amazononlygoods ")
        read_site.get_info(soup2, "amazonBrowse_amazondomainonlygoods")
        read_site.get_info(soup3, "amazonBrowse_amazononlybrand")
        return HttpResponse()