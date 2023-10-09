from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from  django.http import JsonResponse

from .forms import bask
from .models import *
from .admin import MatAdmin


class Home(ListView):
    model = MAT
    context_object_name = 'lib'
    template_name = 'lib/index.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bas = client.objects.all()
        form = bask(self.request.POST or None, self.request.FILES or None)
        context['form'] = form
        context['bas'] = bas
        return context

    def post(self, request, *args, **kwargs):
        bas = client.objects.all()
        form = bask(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

        context = self.get_context_data()
        context['form'] = form
        context['bas'] = bas
        return self.render_to_response(context)
class MATget(DetailView):
    model = MAT
    template_name = 'lib/book_p.html'
    context_object_name = 'lib'




def save(request):
    return_dict = dict()
    print(request.POST)
    data = request.POST
    product = data.get("product_name")
    price = data.get("product_price")
    nmb = data.get("quantity")
    name = data.get("client_name")
    phone = data.get("client_phone")
    all = data.get("all")
    new_order = order(title=product, price=price, kilo=nmb, name=name, phone=phone, all_price=all)
    new_order.save()
    return JsonResponse(return_dict)
