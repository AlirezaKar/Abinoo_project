from django import forms
from app_main.models import Donation


class DonationForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='نام*', required=True, widget=forms.TextInput)
    last_name = forms.CharField(max_length=50, label='نام خانوادگی*', required=True, widget=forms.TextInput)
    email = forms.CharField(max_length=60, required=False, label='ایمیل (اختیاری)',widget=forms.EmailInput)
    donor_type = forms.ChoiceField(label='اهدا کننده*', choices=Donation.DonorType.choices, widget=forms.Select)
    donation_type = forms.ChoiceField(required=True, label="شیوه کمک*", choices=Donation.DonationType.choices, widget=forms.Select)
    donation_amount = forms.IntegerField(label='مقدار کمک', widget=forms.NumberInput)
    message = forms.CharField(max_length=1000, required=False, label='توضیحات', widget=forms.Textarea)
    anonymize_donation = forms.ChoiceField(label='ناشناس', required=False, choices=Donation.AnonymizeDonation.choices, widget=forms.Select)