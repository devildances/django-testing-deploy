from django.shortcuts import render
from django.http import HttpResponse
from test_app.models import table_topic, table_webpage, table_AccessRecord # import table here
from . import forms # import forms from forms.py
from test_app.forms import newUserForm # import class from forms.py
from django.http import HttpResponse

# Create your views here.
def index(request):
    dt = {'text':'TempFil', 'number':100}
    return render(request,'test_inner_temp/index.html',context=dt)

def faker(request):
    webpages_list = table_AccessRecord.objects.order_by('col_AccessRecord2')
    dt = {'access_records':webpages_list}
    return render(request,'test_inner_temp/faker.html', context=dt)

# ============================= FORMS =============================================
def forms_name(request):
    f = newUserForm()
    if request.method == 'POST':
        f = newUserForm(request.POST)
        if f.is_valid():
            f.save(commit=True) # commit to DB
            return index(request) # return to index page
        else:
            print('ERROR FROM INVALID')
    return render(request,'test_inner_temp/form.html', {'form':f})
    # form = forms.FormName()

    # if request.method == 'POST':
    #     form = forms.FormName(request.POST)
    #     if form.is_valid():
    #         print("Name : ", form.cleaned_data['name'])
    #         print("Email : ", form.cleaned_data['mail'])
    #         print("Text : ", form.cleaned_data['txt'])

    # return render(request, 'test_inner_temp/form.html', {'form':form})


# ============================ RELATIVE URL TEMPLATE =============================================

def relative(request):
    return render(request,'test_inner_temp/relative_url_template.html')

# ============================ REGISTRATION USERPROFILE =============================================

from test_app.forms import UserProfileForm, UserProfileInfoForm

def register(request):
    registered = False

    if request.method == 'POST':
        UserProfile_Form = UserProfileForm(data=request.POST)
        UserProfile_Info = UserProfileInfoForm(data=request.POST)

        if UserProfile_Form.is_valid() and UserProfile_Info.is_valid():
            user = UserProfile_Form.save()
            user.set_password(user.password)
            user.save()

            profile = UserProfile_Info.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(UserProfile_Form.errors, UserProfile_Info.errors)

    else:
        UserProfile_Form = UserProfileForm()
        UserProfile_Info = UserProfileInfoForm()

    return render(request,'test_inner_temp/registration.html', {'UserProfile_Form':UserProfile_Form,
                                                        'UserProfile_Info':UserProfile_Info,
                                                        'registered':registered})

# ============================ USER LOGIN VIEWS =============================================

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == 'POST':
        un = request.POST.get('uname')
        pw = request.POST.get('pwd')

        user = authenticate(username=un, password=pw)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("You are not registered yet!")
        else:
            print("attempted to login and failed")
            return HttpResponse('Invalid login details!')

    else:
        return render(request,'test_inner_temp/login.html', {})


# ============================= CBV ====================================


from django.views.generic import View, TemplateView, ListView, DetailView # CBV default method

# class CBView(View):
#     def get(self,request):
#         dt = {'text':'TempFil', 'number':100}
#         return render(request,'test_inner_temp/index.html',context=dt)

class indexView(TemplateView):
    template_name = 'test_inner_temp/index.html'
    def get_context_data(self, **kwargs):
        dt = super().get_context_data(**kwargs)
        dt['text'] = 'TempFil'
        dt['number'] = 200
        return dt



class fakerListView(ListView):
    template_name = 'test_inner_temp/faker.html'
    context_object_name = 'webpages'
    model = table_webpage # OR queryset = table_webpage.objects.all()
    # if we dont define context_object_name, ListView will return table_AccessRecord to
    # HTML as table_AccessRecord + _list = table_AccessRecord_list automatically

class fakerDetailView(DetailView):
    context_object_name = 'webpages'
    model = table_webpage
    template_name = 'test_inner_temp/faker_CBV.html'


# ============================== CRUD =============================================


from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TopicCreateView(CreateView):
    template_name = 'test_inner_temp/crud.html'
    fields = ('col_topic1',)
    model = table_topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ttopic'] = table_topic.objects.all()
        return context

class TopicUpdateView(UpdateView):
    template_name = 'test_inner_temp/crud.html'
    fields = ('col_topic1',)
    model = table_topic

class TopicDeleteView(DeleteView):
    template_name = 'test_inner_temp/crud.html'
    model = table_topic
    success_url = reverse_lazy('test_app:create')