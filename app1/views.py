from django.shortcuts import render
from django import forms
from django.views.generic import View ,ListView,DetailView ,TemplateView
from . import models
from django.http import HttpResponse
# Create your views here.
class MyForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    a = forms.CharField(max_length=500)

def index(request):
    a=0
    form = MyForm()
    if request.method == 'POST':
        print('form post')
        form = MyForm(request.POST)
        print(form)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            print('test')
            # now in the object cd, you have the form as a dictionary.
            a = cd.get('a')
    injectme = {'injectme': a }
    return render(request,'index.html',context=injectme)

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED ARE COOL")
#

# class IndevView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['injectme']='BASIC INJECTION1'
#         return context

# class SchoolListView(ListView):
#     model= models.School
#
# class SchoolDetailView(DetailView):
#     model= models.Students
#     template_name = 'index.html'