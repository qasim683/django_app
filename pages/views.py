from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Contact

# Create your views here.
def home(request):
    return render(request, 'index.html',{'title': 'Home Page Title'})

def about(request):
    return render(request, 'about.html',{'title': 'about Page Title'})

def contact(request):
    if(request.method == 'POST'):
        data = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            address=request.POST['address'],
            city=request.POST['city'],
            zipcode=request.POST['zipcode']
        )
        data.save()
    cnt= Contact.objects.all()
    return render(request, 'contact.html', {'title': 'contact Page Title','rows' :cnt } )
    

def member(request, id):
    return HttpResponse("<h1>Team member ID: {}" .format(id))

#def team(request):
    #if(request.method == 'GET' and 'cat_id' in request.GET and 'mem_id' in request.GET):
        #return HttpResponse ("<h1> Team Members ID: {}</h1>".format(request.GET.get('mem_id'), request.GET.get('cat_id')))
    #else:
     #   return HttpResponse("<h1>Team Members Lists</h1>")
