from django.shortcuts import render, redirect
from .forms import BasicNoteForm, ScheduleBlockForm
from .models import BasicNote, ScheduleBlock
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    if request.user.is_authenticated:
        me = request.user
        usernotes = BasicNote.objects.filter(user=me)
        schedulemonday = ScheduleBlock.objects.filter(user=me, day="Monday").order_by('startTime')
        scheduletuesday = ScheduleBlock.objects.filter(user=me, day="Tuesday").order_by('startTime')
        schedulewednesday = ScheduleBlock.objects.filter(user=me, day="Wednesday").order_by('startTime')
        schedulethursday = ScheduleBlock.objects.filter(user=me, day="Thursday").order_by('startTime')
        schedulefriday = ScheduleBlock.objects.filter(user=me, day="Friday").order_by('startTime')
        schedulesaturday = ScheduleBlock.objects.filter(user=me, day="Saturday").order_by('startTime')
        schedulesunday = ScheduleBlock.objects.filter(user=me, day="Sunday").order_by('startTime')
    else:
        usernotes = None
        schedulemonday = None
        scheduletuesday = None
        schedulewednesday = None
        schedulethursday = None
        schedulefriday = None
        schedulesaturday = None
        schedulesunday = None
    if request.method == "POST":
        noteForm = BasicNoteForm(request.POST, request.FILES)
        scheduleForm = ScheduleBlockForm(request.POST)
        if 'noteSubmit' in request.POST:
            if noteForm.is_valid():
                noteForm.instance.user = request.user
                noteForm.save()
                return redirect('index')
        if 'scheduleSubmit' in request.POST:
            if scheduleForm.is_valid():
                scheduleForm.instance.user = request.user
                scheduleForm.save()
                return redirect('index')
    else:
        noteForm = BasicNoteForm
        scheduleForm = ScheduleBlockForm
    context = {
        'noteForm': noteForm,
        'scheduleForm': scheduleForm,
        'usernotes': usernotes,
        'schedulemonday': schedulemonday,
        'scheduletuesday': scheduletuesday,
        'schedulewednesday': schedulewednesday,
        'schedulethursday': schedulethursday,
        'schedulefriday': schedulefriday,
        'schedulesaturday': schedulesaturday,
        'schedulesunday': schedulesunday,
    }
    return render(request, "notes/index.html", context)


@login_required(login_url='/users/login_user/')
def delete_note(request, note_id):
    try:
        note = BasicNote.objects.get(pk=note_id)
    except ObjectDoesNotExist:
        messages.success(request, "You don't have the permission to perform this action!")
        return redirect('index')
    if note.user == request.user:
        note.delete()
    else:
        messages.success(request, "You don't have the permission to perform this action!")
    return redirect('index')


@login_required(login_url='/users/login_user/')
def delete_block(request, block_id):
    try:
        block = ScheduleBlock.objects.get(pk=block_id)
    except ObjectDoesNotExist:
        messages.success(request, "You don't have the permission to perform this action!")
        return redirect('index')
    if block.user == request.user:
        block.delete()
    else:
        messages.success(request, "You don't have the permission to perform this action!")
    return redirect('index')