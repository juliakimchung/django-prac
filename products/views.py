from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

# Create your views here.

def home(request):
    product_list = Product.objects.order_by('created')[:20]
    context = {
        "product_list": product_list,
    }
    
    return render(request, "products/home.html", context)
# class Create_p(TemplateView):
#     template_name = 'myproduct_app/detail.html'

def create(request):
    data= request.POST
    Product.objects.create(
        name = data['name'],
        price = data['price'],
        description = data['description'],
        quantity = data['quantity'],
        user=request.user
        )
    return HttpResponseRedirect(redirect_to="/products/list")

def template_to_create(request):
    return render(request, "products/detail.html")


def specifics(request):
    product_item = Product.objects.get(pk=product_id)
    context = {
    "product_item": product_item
    }
    return render(request, "products/specific.html", context )

class IndexView(TemplateView):
    template_name = "products/login.html"


class Register(TemplateView):
    template_name = 'products/register.html'

def register_user(request):
    data = request.POST
    User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        )
    return login_user(request)

def login_user(request):
    data=request.POST
    username=data['username']
    password=data['password']
    user=authenticate(
        username=username,
        password=password)
    if user is not None:
        login(request=request, user=user)
    else:
        return HttpResponseRedirect(redirect_to='/')
    return HttpResponseRedirect(redirect_to='/products/list')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/')






