from django.shortcuts import render

# Create your views here.
#views.py

from django.db.models import Q

from login.forms import DocumentForm , RegistrationForm
from login.forms import DocumentForm, RegistrationForm
from login.models import Document
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from login.models import Publisher
from django.shortcuts import get_object_or_404
import time



from django.contrib.auth.models import User


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required(login_url='/login/')
def home(request):
    context  = RequestContext(request)
    context['user'] = request.user
    #if request.method == 'POST':
     #   print 'asd --->', request.FILES
    #    uplo = request.FILES['uplo']
    #    fs = FileSystemStorage()
     #   filename = fs.save(uplo.name, uplo)
    #    uploaded_file_url = fs.url(filename)
     #   return render(request, 'home.html', {
    #       'uploaded_file_url': uploaded_file_url
    #    })
    form = DocumentForm(request.POST, request.FILES)
    documents = Document.objects.all()
    return render(
        request,
        'home.html',
        {'documents': documents, 'form': form}
    )


@login_required(login_url='/login/')
def subir(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print time.strftime("%d/%m/%y") + " a las " + time.strftime("%H:%M:%S")
            print  "zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            newdoc.user= "gosheau"
            newdoc.save()
            print  "zxxxaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaxxxx"
            newdoc.fecha= time.strftime("%d/%m/%y") + " a las " + time.strftime("%H:%M:%S")
            newdoc.save()
            print  "zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            newdoc.description= "descrwetui"
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/home/')
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'home.html',
        {'documents': documents, 'form': form}
    )

@login_required(login_url='/login/')
def perfil(request):
    return render_to_response(
    'perfil.html',
    { 'user': request.user }
    )

@login_required(login_url='/login/')
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(username__contains=query) 
        )
        results = User.objects.filter(qset)
#        results = result.sorted(key = str.lower)
    else:
        results = []
        

    return render_to_response("search.html", {
        "results": results.order_by('username'),
        "query": query
    })

@login_required(login_url='/login/')
def delete(request):
    print "gfogfof"
    if request.method != 'GET':
        raise HTTP404

    docId = request.POST.get('docfile', None)
    docToDel = get_object_or_404(Document, pk = docId)
    docToDel.docfile.delete()
    docToDel.delete()
    
    

    return HttpResponseRedirect('/home/')



