from django.shortcuts import render

from market.models import Product


def post_list(request):
    return render(request, 'market/post_list.html', {})

