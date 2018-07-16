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
            new_item.save()
            # form.save()
            # all_items = List.objects.all
            all_items = List.objects.filter(owner=request.user)
            messages.success(request, 'Okay! An item has been added to the List!')
            return render(request, 'home.html', {'all_items': all_items})
    else:
        # all_items = List.objects.all
        all_items = List.objects.filter(owner=request.user)
        return render(request, 'home.html', {'all_items': all_items})


def about(request):
    my_name = "Justin Wang"

    return render(request, 'about.html', {'name': my_name})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'An item has been Deleted.')
    return redirect('home')


@login_required(login_url='/users/login/')
def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.completedTime = datetime.now(pytz.utc)
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
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


