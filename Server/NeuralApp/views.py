from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadImageForm
from .functions import handle_uploaded_file

def upload_file(request):
    form = 'Dummy String'
    form = UploadImageForm(data = request.POST, files = request.FILES)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            print('succes uploading file')
            handle_uploaded_file(request.FILES['image'])
            return HttpResponseRedirect('/NeuralApp/')
        else:
            print('coś się zjebało xd')
            form = UploadImageForm()
    return render(request, 'NeuralApp/home.html', {'form': form})

# Create your views here.