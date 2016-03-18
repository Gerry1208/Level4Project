
from names.forms import UserForm, UserProfileForm, cardForm, groupsForm, picForm, bulkUpload
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
import logging
import json


logger = logging.getLogger(__name__)
#form.cleaned_data for all?

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

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            user = authenticate(username=user_form.cleaned_data['username'],password=user_form.cleaned_data['password'],)
            login(request,user)
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            return render(request,
                          'register.html',
                          {'user_form': "existing username", 'profile_form': profile_form.errors, 'error':"true"} )

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


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
    group_name = request.GET.get('name')
    cards = card.objects.filter(group=group_name)
    users = User.objects.values_list("username", flat=True)
    pictures = []
    group = groupModel.objects.filter(id=group_name)
    groupID = groupModel.objects.filter(id=group_name).values('id')
    UserID = card.objects.filter(group=group_name).values('id')
    for c in cards:
        pictures += cardPicture.objects.filter(student=c.id)
    return render_to_response('cardview.html', {'cards':cards, 'pictures':pictures, 'group':group, 'users':users, 'groupID':groupID, 'cardID':UserID}, context_instance=RequestContext(request))


@login_required
def quiz(request):

    count = -1
    group_name=request.GET.get('name')
    quiz_type=request.GET.get('quiz')
    cards = card.objects.values_list(flat=True).filter(group=group_name).order_by('?')
    pictures = cardPicture.objects.values_list(flat=True).order_by('?')

    cards = list(cards)
    pictures = list(pictures)

    request.session['cards'] = cards
    request.session['pictures'] = pictures
    request.session['count'] = count

    return render_to_response('readyquiz.html', {'cards':cards, 'pictures':pictures, 'count': count, 'quiz_type':quiz_type}, context_instance=RequestContext(request))
@login_required
def nextQuestion(request):
    cards = request.session.get('cards')
    pictures = request.session.get('pictures')
    count = request.session.get('count')
    cardNum = 10
    score = 0
    if(request.GET.get('score')):
        score = request.GET.get('score')

    # Gets the correct question number, and finishes the quiz if 10 questions have been answered
    if len(cards) < 10:
        if count==(len(cards)-1):
            count = 10
        if len(cards) < 4:
            return render(request, 'index.html')

    if count == 10:
        score = (score/count) * 100
        return render_to_response('selfmark.html', {'cards':cards, 'pictures':pictures, 'score':score, 'count':count}, context_instance=RequestContext(request))


    count += 1
    request.session['count'] = count

    # Gets the correct card and corresponding photo
    card = cards[count]
    for p in pictures:
        if p[1] == card[0]:
            pictures = p

    if len(pictures) > 1:
        pictures = []

    # Gets three random names to go along with it
    # Adds in the correct answer, and shuffles
    rndNames = []
    rndNames.append(card)
    while len(rndNames) < 4:
        choice = random.choice(cards)
        if choice not in rndNames:
            rndNames.append(choice)

    random.shuffle(rndNames)
    return render_to_response('quiz.html', {'cards':card, 'pictures':pictures, 'names':rndNames, 'score':score, 'count':count}, context_instance=RequestContext(request))



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

    if len(pictures) > 1:
        pictures = []


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


class addPicture(FormView):
    template_name='addpicture.html'
    form_class = pictureForm
    success_url = '/names/addpicture/'

    def form_valid(self, form):
        for each in form.cleaned_data['files']:
            studArray= each.name.split(".")
            #studName=studArray[0]
            #studCard = card.objects.filter(student=studName).first()
            cardPicture.objects.create(file=each, student=studCard)
        return super(addPicture,self).form_valid(form)

@csrf_protect
@login_required
def create_cards(request):
    groupList = groupModel.objects.values("id", "group_name")
    if request.method == 'POST':
        card_form = cardForm(data = request.POST)
        pic_form = picForm(request.POST, request.FILES)
        if card_form.is_valid() and pic_form.is_valid():

            card = card_form.save()
            card.save()

            pic = cardPicture(file = request.FILES['file'])
            pic.student = card
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
    g = groupModel.objects.get(id = groupName)
    u = User.objects.get(username=share_form)
    g.user.add(u.id)
    return render(request, "index.html")