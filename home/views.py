from django.http import HttpResponse
from django.template import loader
from .models import Info

def index(request):
    all_info=Info.objects.all()
    template =loader.get_template('home/index.html')
    context={
        'all_info':all_info,
    }
    return HttpResponse(template.render(context, request))
    return HttpResponse("<h1>Welcome To Consultadd</h1> "
                        "<form action='#'>"
                        "<table aligh='center'>"
                        
                        "<tr><th>First Name</th><td><input type='text' name='fname'></tr>"
                        "<tr><th>Last Name</th><td><input type='text' name='lname'></tr>"
                        "<tr><th>Email ID</th><td><input type='email' name='email'></tr>"
                        "<tr><th>Pnone No.</th><td><input type='tel' name='number'></tr>"
                        "<tr><th> Country of Citizenship</th><td><input type='text' name='citizen'></tr>"
                        "<tr><th>Current City</th><td><input type='text' name='city'></td></tr>"
                        "</table>"
                        "<input type='submit' value='Submit'>"
                        "</form >"
    )





