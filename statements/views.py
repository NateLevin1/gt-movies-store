from django.shortcuts import render
from django.shortcuts import redirect
from .models import Statement
from django.contrib.auth.decorators import login_required

def index(request):
    template_data = {}
    statements = Statement.objects.all()
    template_data["statements"] = statements
    return render(request, 'statements/index.html',
                  {'template_data': template_data})

@login_required
def create_statement(request):
    if request.method == 'POST' and request.POST['thoughts'] != '':
        statement = Statement()
        statement.thoughts = request.POST['thoughts']
        if request.POST['name'] != '':
            statement.name = request.POST['name']
        else:
            statement.name = 'Anonymous'

        statement.save()
        return redirect('cart.purchase')
    else:
        template_data = {}
        return render(request, 'statements/create_statement.html',
                  {'template_data': template_data})
    
