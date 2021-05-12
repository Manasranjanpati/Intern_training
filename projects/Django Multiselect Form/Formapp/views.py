from django.shortcuts import render

# Create your views here.
from .models import EnquiryData
from .forms import EnquiryForm



def enquiry_view(request):
    if request.method == "POST":
        eform = EnquiryForm(request.POST)
        if eform.is_valid():
            name = eform.cleaned_data.get('name')
            email = eform.cleaned_data.get('email')
            mobile = eform.cleaned_data.get('mobile')
            cources = eform.cleaned_data.get('cources')
            trainer = eform.cleaned_data.get('trainer')
            shift = eform.cleaned_data.get('shift')
            location = eform.cleaned_data.get('location')
            gender = eform.cleaned_data.get('gender')
            
            data = EnquiryData(
                name=name,
                email=email,
                mobile=mobile,
                cources=cources,
                trainer=trainer,
                shift=shift,
                location=location,
                gender=gender
            )
            data.save()
            eform = EnquiryForm()
            context = {'form':eform}
            return render(request,'enquiry.html',context)
    else:
        eform = EnquiryForm()
        context = {'form':eform}
        return render(request,'enquiry.html',context)