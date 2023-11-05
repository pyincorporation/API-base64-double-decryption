from django.shortcuts import render
from .forms import *
from .models import *
from .crypto import *
from .api_request import *
from.request import *
from django.contrib.auth.hashers import make_password
# Create your views here.
def index(request):
    cont = False
    create = False
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            get_user = get_user_creadentions(username, password)
            jina = get_user[0]['majina']
            sex = get_user[0]['jinsia']
            reg = get_user[0]['usajili']
            cont=json.loads(get_user[2])
            try:
                for std in cont:
                    StudentResults.objects.create(username=encrypt_data(std['regno']), subject = encrypt_data(std['somo']), marks = encrypt_data(std['alama']))
                    create=True
            except Exception:
                print('error')
    return render(request, 'API/index.html',{
        'form':Form(), 
        'std_content':cont,
        'create': create
    })