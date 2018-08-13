from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
import pytz
from datetime import datetime


# Create your views here.
@login_required(login_url='/users/login/')
def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.owner = request.user
            new_item.addedTime = datetime.now(pytz.utc)
            new_item.save()
            # form.save()
            # all_items = List.objects.all
            all_items = List.objects.filter(owner=request.user)
            messages.success(request, 'Okay! An item has been added to the List!')
            return render(request, 'home.html', {'all_items': all_items})
        else:
            messages.warning(request, 'Attention: the input area can not be empty!')
            all_items = List.objects.filter(owner=request.user)
            return render(request, 'home.html', {'all_items': all_items})
    else:
        # all_items = List.objects.all
        all_items = List.objects.filter(owner=request.user)
        return render(request, 'home.html', {'all_items': all_items})


# the about function will redirect to the about.html page
# the about.html page display information such as the development team and Tools used for this project.
def about(request):
    return render(request, 'about.html', {})


# the delete function is triggered when user click the DELETE button for certain task item
# we use list_id as primary key to make sure database only delete the task that is supposed to be deleted
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'An item has been Deleted.')
    return redirect('home')


# @login_required(login_url='/users/login/')
# The cross_off function is triggered when users click DONE button in their list
# We set their completedTime as the current sever time and mark the status of that task to True
def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.completedTime = datetime.now(pytz.utc)
    item.save()
    messages.success(request, 'Well done! The task is completed.')
    return redirect('home')


def uncross(request, list_id):
    # use list_id as primary key to make sure we are updating certain task item
    item = List.objects.get(pk=list_id)
    item.completed = False
    # when users choose to redo a task item, we are resetting the addedTime(Starting Time of a task) to current time
    item.addedTime = datetime.now(pytz.utc)
    item.save()
    messages.success(request, 'Task been reset')
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item Has Been Edited!')
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'editList.html', {'item': item})


# redirect to the Code of Conduct page
# this function is triggered when users click on the Communication button on the Top Navigation bar
def coc(request):
    return render(request, 'coc.html', {})



