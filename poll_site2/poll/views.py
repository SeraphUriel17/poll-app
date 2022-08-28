
from django.shortcuts import render
from .forms import CreatePollForm
from django.shortcuts import redirect
from .models import Poll
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

@login_required(login_url='/accounts/login')
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'poll/create.html', context)

@login_required(login_url='/accounts/login')
def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)

@login_required(login_url='/accounts/login')
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        else:
            return HttpResponse(400, 'Invalid form option')
        poll.save()
        return redirect('results', poll.id)


    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)

@login_required(login_url='/accounts/login')
def profile(request):
    #poll_ids = request.user.profile.poll_number_set.all
    #polls = Poll.objects.all()
    #context = {
    #    'polls' : polls
    #}
    return render(request, 'poll/profile.html')#,context)