
from django.shortcuts import render, redirect
from myprojectapp.models import Teacher,Department,Course

from .forms import MyForm
# Create your views here.
def demo(request):
    obj1=Teacher.objects.all()
    obj2=Department.objects.all()
    return render(request,'index.html',{'result':obj1,'res':obj2})

def contact_page(request):
    return render(request, 'contact.html')




def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            dob = form.cleaned_data['dob']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']
            department = form.cleaned_data['department']
            course = form.cleaned_data['course']
            return redirect('success_page')
            # Handle form submission here
            # You can access form.cleaned_data to get the submitted data
    else:
        form = MyForm()

    return render(request, 'contact.html', {'form': form})

