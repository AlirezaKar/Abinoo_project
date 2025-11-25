from django.shortcuts import render
from .models import Donation, User
from .forms import DonationForm

def index(request):
    if request.method == 'POST':
        data = DonationForm(request.POST)
        if data.is_valid():
            form_data = data.cleaned_data
            first_name = form_data.get("first_name")
            last_name = form_data.get("last_name")
            donation_type = form_data.get("donation_type")
            donation_amount = form_data.get("donation_amount")
            
            try:
                user = User.objects.get(first_name=first_name, last_name=last_name)
            except:
                user = User.objects.create(first_name=first_name, last_name=last_name, username=f"{first_name}-{last_name}")
            
            donation = Donation.objects.create(donation_type=donation_type, donation_amount=donation_amount, user=user)
        else:
            form_donation = DonationForm()
            context = {'form_donation':form_donation, 'error':'اطلاعات به درستی وارد نشده اند.'}
            return render(request=request, template_name='homepage/index.html', context=context)
            
    
    else:
        form_donation = DonationForm()
        context = {'form_donation':form_donation}
        return render(request=request, template_name='homepage/index.html', context=context)
    
def about(request):
    return render(request=request, template_name='homepage/about.html')

def license(request):
    return render(request=request, template_name='homepage/license.html')