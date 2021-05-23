from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth

# Create your views here.
def register(request):
    print(request.method)
    if request.method == 'POST':
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      email = request.POST['email']
      password1 = request.POST['password1']
      password2 = request.POST['password2']
      username = request.POST['username']
      
      if User.objects.filter(username=username).exists():
        messages.info(request, 'User Taken')
        print("uexist")
        return redirect("/accounts/register/")
      elif User.objects.filter(email=email).exists():
        messages.info(request, 'Email Taken')
        return redirect("/accounts/register/")
      elif User.objects.filter(first_name=first_name).exists():
        messages.info(request, 'first name exist')
        return redirect("/accounts/register/")
      elif User.objects.filter(last_name=last_name).exists():
        messages.info(request, 'last name exist')
        return redirect("/accounts/register/")
      else:
        user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
        user.save();              
        return redirect("/accounts/login")
    else:
      return render(request, 'register.html')


def login(request):
  if request.method == 'POST':
          
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect("/")
    else:
      messages.info(request, 'invalid credentials')
      return redirect('/accounts/login')


  else:
    return render(request, 'login.html')


def logout(request):
  auth.logout(request)
  return redirect("/")