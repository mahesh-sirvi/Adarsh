from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from datetime import datetime
from card.models import Contact, Buy_Model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import collections

# Create your views here.
item_name = ''


class Song(View):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print(item_name)
            if 'authenticate_logout' in request.POST or 'authenticate_login' in request.POST:
                if request.user.is_authenticated:
                    username = request.user.username
                    logout(request)
                    messages.warning(request, 'Logged out successfully from {}'.format(username))
                    return redirect('/')
                else:
                    return redirect('/login')

    def get(self, request, *args, **kwargs):
        global item_name
        if 'item' in request.GET:
            if request.user.is_anonymous:
                messages.warning(request, 'You need to login to buy items')
                return render(request, 'card/login.html')
            item_name = request.GET.get('item')
            print(item_name)
            context = {'quality':item_name}
            return render(request, 'card/buy.html', context=context)
        return render(request, 'card/song.html')


class AboutUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/about.html')


class ContactUs(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            feedback = request.POST.get('feedback')
            if len(name) == 0 and len(email) == 0 and len(phone) == 0:
                messages.warning(request, 'Kindly fill the form before submitting!')
                return redirect('/contact')
            elif len(name) != 0 and len(email) == 0 and len(phone) == 0:
                messages.warning(request, "'Email' and 'Contact Number' fields cannot be blank!")
                return redirect('/contact')
            elif len(name) == 0 and len(email) == 0 and len(phone) != 0:
                messages.warning(request, "'Name' and 'Email' fields cannot be blank!")
                return redirect('/contact')
            elif len(name) == 0 and len(email) != 0 and len(phone) == 0:
                messages.warning(request, "'Name' and 'Contact Number' fields cannot be blank!")
                return redirect('/contact')

            elif len(name) != 0 and len(email) != 0 and len(phone) != 0 and ('@' and '.' not in email):
                messages.warning(request, 'Incorrect Email!')
                return redirect('/contact')
            elif len(name) == 0 or len(email) == 0 or len(phone) == 0:
                messages.warning(request, 'Incorrect values entered!')
                return redirect('/contact')

            elif len(name) != 0 and len(email) != 0 and len(phone) != 0:
                for num in phone:
                    if num.isalpha():
                        messages.warning(request, 'Phone number should contain numeric values!')
                        return redirect('/contact')
                    else:
                        contact = Contact(name=name, email=email, phone=phone, feedback=feedback, date=datetime.today())
                        contact.save()
                        messages.success(request, 'Form submitted successfully!')
                        return redirect('/')
            else:
                return redirect('/contact')

    def get(self, request, *args, **kwargs):
        return render(request, 'card/contact.html')


class Shreeji(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc01.html')


class SafariSilk(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/safari_silk.html')


class Sonika(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sonika.html')


class AllProducts(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/view_all.html')


class Search(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            q = request.GET.get('q').lower()
            context = {'q': q}
            if len(context['q']) == 0:
                return redirect('/')
            else:
                return render(request, 'card/search.html', context=context)


class SC02(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'card/sc02.html')


class SC03(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc03.html')


class SCO4(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc04.html')


class SC05(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc05.html')


class SC06(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc06.html')


class SC07(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc07.html')


class SC08(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc08.html')
class SC09(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc09.html')
class SC10(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc10.html')
class SC11(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc11.html')
class SC12(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'card/sc12.html')


class Register(View):
    form = UserCreationForm()

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'User created successfully! You can now sign in!')
                return redirect('/login')
            else:
                messages.warning(request, 'Incorrect Credentials! Please try again.')
                return redirect('/register')

    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'card/register.html', context=context)


class Login_Adarsh(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully as {}'.format(user))
                return redirect('/')
            else:
                messages.warning(request, 'Incorrect values entered! If you are a new user, consider registering yourself first.')
                return redirect('/login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'card/login.html')


class Buy(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            qt = request.POST.get('quantity')
            update_database = Buy_Model(item=item_name, quantity=qt, user=request.user)
            update_database.save()
            messages.success(request, 'Added to cart successfully!')
            return redirect('/cart')


class CartView(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user = Buy_Model.objects.filter(user=request.user)
            items = []
            for x in request.POST:
                items.append(x)
            item_name = items[1]
            if 'authenticate_logout' in request.POST:
                messages.warning(request, 'Logged out successfully from {}'.format(request.user))
                logout(request)
                return redirect('/')
            if 'authenticate_logout' or 'authenticate_login' not in request.POST:
                return redirect('/products/{}'.format(item_name))

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = Buy_Model.objects.filter(user=request.user)
            quantity_list = []
            quality = []
            for i in user:
                print(i)
                quantity_list.append(i.quantity)
                quality.append(i.item)
            pair = zip(quality, quantity_list)
            empty = []
            for x in pair:
                print(x)
                empty.append(x)
            print(empty)
            total_pcs = sum(quantity_list)
            print(quality)
            print(quantity_list)
            context = {'quantity_list':quantity_list, 'items':user, 'total_pcs':total_pcs}
            return render(request, 'card/cart.html', context=context)
        else:
            return render(request, 'card/cart.html')