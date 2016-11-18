from django.shortcuts import render

# Create your views here.
#views.py
from login.forms import DocumentForm
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
 
@login_required
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
    return render_to_response(
    'home.html',context
    )


@login_required
def subir(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('home'))
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

@login_required
def perfil(request):
    return render_to_response(
    'perfil.html',
    { 'user': request.user }
    )
