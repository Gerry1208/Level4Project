from names.forms import UserForm, UserProfileForm, cardForm, groupsForm, picForm
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from names.models import groupModel, card



#form.cleaned_data for all?

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
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                 'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

@csrf_protect
@login_required
def create_cards(request):
    if request.method == 'POST':
        card_form = cardForm(data = request.POST)
        pic_form = picForm(request.POST, request.FILES)
        if card_form.is_valid() and pic_form.is_valid():

            card = card_form.save()
            card.save()

            pic = pic_form.save(commit=False)
            pic.student = card
            pic.file = request.FILES['file']
            pic.save()
    else:
        card_form = cardForm()
        pic_form = picForm()
    return render_to_response('create.html', {'card_form': card_form, 'pic_form':pic_form},
                              context_instance=RequestContext(request))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/cards/index/')
            else:
                return HttpResponse("Your rango account is disabled")

        else:
            print "invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/names/index/')

@csrf_protect
@login_required
def groups(request):
    if request.method == 'POST':
        group_form = groupsForm(request.POST)

        if group_form.is_valid():

            group = group_form.save(commit=False)

            group.user = request.user
            group.save()
    else:
        group_form = groupsForm()

    return render_to_response('groups.html', {'group_form': group_form},
                              context_instance=RequestContext(request))

@csrf_protect
@login_required
def groupview(request):
    user = request.user
    groups = groupModel.objects.filter(user = user.id).order_by('group_name')
    return render(request, 'groupview.html', {'groups':groups})
