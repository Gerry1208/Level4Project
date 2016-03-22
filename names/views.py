from names.forms import UserForm, cardForm, groupsForm, picForm, bulkUpload
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from names.models import card
from django.views.generic.edit import FormView
from .forms import pictureForm
from .models import cardPicture, User, groupModel
import random

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed.")
            return redirect("/names/index")
    else:
        form = PasswordChangeForm(request.user)
    data = {
        'form': form
    }
    return render(request, "changepass.html", data)


def index(request):
    return render(request, 'index.html', {})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user = authenticate(username=user_form.cleaned_data['username'],password=user_form.cleaned_data['password'],)
            login(request,user)
            registered = True
        else:
            return render(request,
                          'register.html',
                          {'user_form': "existing username", 'error':"true"} )
    else:
        user_form = UserForm()
    return render(request,
                  'register.html',
                  {'user_form': user_form, 'registered': registered})

@login_required
def upload(request):
    if request.method == "POST":
        form = bulkUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            context = {"form":form}
            return render_to_response('upload.html', context, context_instance=RequestContext(request))
    else:
        form = bulkUpload()
        context = {"form":form}
        return render_to_response('upload.html', context, context_instance=RequestContext(request))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/names/index/')
            else:
                return HttpResponse("Your rango account is disabled")

        else:
            print "invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'login.html', {})

@csrf_protect
@login_required
def groups(request):
    if request.method == 'POST':
        group = groupsForm(request.POST)
        if group.is_valid():
            g = group.save(commit=False)
            g.group_name = request.POST.get('groupname')
            g.save()
    else:
        group = groupsForm()

    return render_to_response('groups.html',{"group":group},context_instance=RequestContext(request))

@csrf_protect
@login_required
def cardview(request):
    if request.method == "POST":
        cardID = request.POST.get('card')
        cardItem = card.objects.get(id=cardID)
        pic = cardPicture(file = request.FILES['file'])
        pic.card = cardItem
        pic.save()
    group_name = request.GET.get('name')
    cards = card.objects.filter(group=group_name)
    users = User.objects.values_list("username", flat=True)
    pictureCards = cardPicture.objects.values_list('card', flat=True)
    pictures = []
    group = groupModel.objects.filter(group_name=group_name)
    for c in cards:
        pictures += cardPicture.objects.filter(card=c.id)
    return render_to_response('cardview.html', {'pictureCards':pictureCards, 'cards':cards, 'pictures':pictures, 'group':group, 'users':users}, context_instance=RequestContext(request))


@login_required
def quiz(request):

    count = -1
    group_name=request.GET.get('name')
    quiz_type=request.GET.get('quiz')
    cards = card.objects.values_list(flat=True).filter(group=group_name).order_by('?')
    pictures = cardPicture.objects.values_list(flat=True).order_by('?')
    message=""

    cards = list(cards)
    pictures = list(pictures)

    if len(cards) < 4:
        message = "Unfortunately you do not have enough cards in that group to do a multiple choice quiz"


    request.session['cards'] = cards
    request.session['pictures'] = pictures
    request.session['count'] = count

    return render_to_response('readyquiz.html', {'cards':cards, 'pictures':pictures, 'count': count, 'quiz_type':quiz_type, 'msg':message}, context_instance=RequestContext(request))

@login_required
def nextQuestion(request):
    cards = request.session.get('cards')
    pictures = request.session.get('pictures')
    count = request.session.get('count')
    score = 0

    if(request.GET.get('score')):
        score = request.GET.get('score')

    # Gets the correct question number, and finishes the quiz if 10 questions have been answered
    if len(cards) < 10:
        if count==(len(cards)-1):
            count = 10

    if count == 10:
        return render_to_response('selfmark.html', {'cards':cards, 'pictures':pictures, 'score':score, 'count':count}, context_instance=RequestContext(request))


    count += 1
    request.session['count'] = count

    # Gets the correct card and corresponding photo
    card = cards[count]
    for p in pictures:
        if p[1] == card[0]:
            pictures = p


    # Gets three random names to go along with it
    # Adds in the correct answer, and shuffles
    rndNames = []
    rndNames.append(card)
    while len(rndNames) < 4:
        choice = random.choice(cards)
        if choice not in rndNames:
            rndNames.append(choice)

    random.shuffle(rndNames)
    return render_to_response('quiz.html', {'cards':card, 'pictures':pictures, 'names':rndNames, 'score':score, 'count':count, 'len':(len(cards)-1)}, context_instance=RequestContext(request))



@login_required
def SelfMarkQuiz(request):
    cards = request.session.get('cards')
    pictures = request.session.get('pictures')
    count = request.session.get('count')

    score = 0
    if(request.GET.get('score')):
        score = request.GET.get('score')

    if len(cards) < 10:
        if count==(len(cards)-1):
            count = 10

    if count == 10:
        return render_to_response('selfmark.html', {'cards':cards, 'pictures':pictures, 'score':score, 'count':count}, context_instance=RequestContext(request))

    # Gets the correct question number, and finishes the quiz if 10 questions have been answered
    count += 1
    request.session['count'] = count

    cards = cards[count]
    for p in pictures:
        if p[1] == cards[0]:
            pictures = p



    return render_to_response('selfmark.html', {'cards':cards, 'pictures':pictures, 'score':score, 'count':count}, context_instance=RequestContext(request))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/names/index/')


@csrf_protect
@login_required
def groupview(request):
    if request.method == 'POST':
        group_form = groupsForm(data = request.POST)
        if group_form.is_valid():
            g = group_form.save(commit=False)
            g.save()
            g.user.add(request.user.id)
            g.save()
    groups = groupModel.objects.filter(user = request.user)
    group_form = groupsForm()
    return render_to_response('groups.html', {'groups':groups, 'group_form':group_form}, context_instance=RequestContext(request))

# This class is for adding pictures with student numbers as their filename, and linking it to the relevant card
# Not needed for this version of the app, but could still be useful
# class addPicture(FormView):
#     template_name='addpicture.html'
#     form_class = pictureForm
#     success_url = '/names/addpicture/'
#
#     def form_valid(self, form):
#         for each in form.cleaned_data['files']:
#             studArray= each.name.split(".")
#             studName=studArray[0]
#             studCard = card.objects.filter(student=studName).first()
#             cardPicture.objects.create(file=each, student=studCard)
#         return super(addPicture,self).form_valid(form)

@csrf_protect
@login_required
def create_cards(request):
    groupList = groupModel.objects.values("group_name")
    if request.method == 'POST':
        card_form = cardForm(data = request.POST)
        pic_form = picForm(request.POST, request.FILES)
        if card_form.is_valid() and pic_form.is_valid():

            card = card_form.save()
            card.save()

            pic = cardPicture(file = request.FILES['file'])
            pic.card = card
            pic.save()
    else:
        card_form = cardForm()
        pic_form = picForm()
    return render_to_response('create.html', {'card_form': card_form, 'pic_form':pic_form,'groups':groupList},
                              context_instance=RequestContext(request))

@login_required
def complete(request):
    score = request.GET.get('score')
    return render_to_response('complete.html', {'score':score}, context_instance=RequestContext(request))

def share(request):
    share_form = request.POST.get('usr')
    groupName=request.GET.get('name')
    g = groupModel.objects.get(group_name = groupName)
    u = User.objects.get(username=share_form)
    g.user.add(u.id)
    return render(request, "index.html")