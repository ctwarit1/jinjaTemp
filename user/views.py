from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from user.models import User


# Create your views here.
class UserReg(View):

    def get(self, request):
        return render(request, 'user_reg.html')

    def post(self, request):
        try:
            # first_name = request.POST.get('first_name')
            # last_name = request.POST.get('last_name')
            # username = request.POST.get('username')
            # email = request.POST.get('email')
            # password = request.POST.get('password')
            # phone = request.POST.get('phone')
            # data = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
            #                                 email=email, password=password, phone=phone)
            # data = request.POST.dict()
            data = request.POST.dict()
            # request.POST._mutable= True
            data.pop('csrfmiddlewaretoken')

            # new_dict ={x: y[0] for x, y in request.POST.items()}
            User.objects.create_user(**data)

            return redirect('/login')
        except Exception as e:
            print(e)
            return render(request, 'user_reg.html')


class UserLogin(View):

    def get(self, request):
        return render(request, 'user_log.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        return HttpResponse('invalid Details')
        # return render(request, 'user_log.html')


class UserProfile(View):

    def get(self, request):
        return render(request, 'user_profile.html')


def user_logout(request):
    logout(request)
    return redirect('login')

