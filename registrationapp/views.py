from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['confirm_password']

        if password == con_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect('login/')  # Redirect to login page

        else:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')

    return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")

    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def contact_page(request):
    if request.method == 'POST':
        # Process the form data and save it to the database if needed
        # Redirect to the confirmation page
        return render(request, 'confirmation_page.html', {'confirmation_message': 'Order Confirmed!'})
    return render(request, 'contact.html')



