from django.shortcuts import redirect, render
from .models import Petition
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template_data = {}
    template_data['title'] = 'Petitions'

    petitions = Petition.objects.all()
    template_data['petitions'] = petitions

    if request.method == 'POST' and request.POST['vote-id'] != '':
        vote_id = request.POST['vote-id']
        petition = Petition.objects.get(id=vote_id)
        if not petition.liked_by.contains(request.user):
            petition.liked_by.add(request.user)
            template_data['message'] = f'Voted for {petition.desired_movie}!'
        else:
            template_data['message'] = f'You have already voted for {petition.desired_movie}!'

    return render(request, 'petitions/index.html', {'template_data': template_data })

@login_required
def create_petition(request):
    if request.method == 'POST' and request.POST['desired'] != '':
        petition = Petition()
        petition.desired_movie = request.POST['desired']
        petition.user = request.user
        petition.save()
        return redirect('petitions.index')
    else:
        template_data = {}
        template_data['title'] = 'Create Petition'
        return render(request, 'petitions/create_petition.html', {'template_data': template_data })
