# lindcraft/views.py

from django.shortcuts import render_to_response, render
from .models import productSelect, navSetup

#### Get a dictionary that contains the querysets and some other vars needed by the
#### Nav.html and other templates
d = navSetup()

# Get a directory of the common URLs used in the templates and add to context
from .exits import get_exits
d['exit'] = get_exits()

def index(request):
    d['pageName'] = 'Welcome'
    return render_to_response('index.html', d)

def product(request, prod_id="0"):
    model_list = productSelect(int(prod_id))
    d['model_list'] = model_list
    d['showGroups'] = False
    if model_list :
        # get some product info from the first row of querySet
        d['prodName'] = model_list[0].product.name
        d['prodDesc'] = model_list[0].product.desc
        d['prodImage'] = model_list[0].product.image
        d['pageName'] = d['prodName']
    else:
        d['pageName'] = "No models found"
    
    return render_to_response('product.html', d)

def prices(request):
    d['model_list'] = productSelect() # Get all active products
    d['pageName'] = 'Prices'
    d['showGroups'] = True
    return render_to_response('prices.html', d)

from django.core.mail import send_mail, BadHeaderError
from lindcraft.settings import DEBUG, EMAIL_ADDRESS, ADMIN_EMAIL
def contact(request):
    d['pageName'] = 'Contact Us'
    d['emailSentOk'] = False
    if not request.POST.get('Quote_Coupon', '') and request.POST.get('Quote_Question', '') :
        message = "Name: " + request.POST.get('Quote_Name', '') + "\n\n"
        message += "Company Name: " + request.POST.get('Company_Name', '') + "\n\n"
        message += "Address: " + request.POST.get('Quote_Address', '') + "\n\n"
        message += "Phone: " + request.POST.get('Quote_Phone', '') + "\n\n"
        message += "Email: " + request.POST.get('Quote_email', '') + "\n\n"
        message += "Message: " + request.POST.get('Quote_Question', '') + "\n\n"
        d['message'] = message
        from_email = request.POST.get('Quote_email', d['exit']['emailAddress'])
        try:
            send_mail("Lindcraft Web Contact", message, from_email ,[EMAIL_ADDRESS,ADMIN_EMAIL],fail_silently=(not DEBUG))
            d['emailSentOk'] = True
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
            
        return render(request,'contact.html', d)
    else:
        return render_to_response('contact.html', d)
        

def about(request):
    d['pageName'] = 'About'
    return render_to_response('about.html', d)

def parkingIntro(request):
    d['pageName'] = 'Parking Racks'
    return render_to_response('parkingIntro.html', d)

def displayIntro(request):
    d['pageName'] = 'Display Racks'
    return render_to_response('displayIntro.html', d)

    