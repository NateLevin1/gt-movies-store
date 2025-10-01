from django.shortcuts import render

def index(request):
    template_data = {}
    template_data['title'] = 'Petitions'
    return render(request, 'petitions/index.html', {'template_data': template_data })
