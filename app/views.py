from django.shortcuts import render

# this is to render the single page app developed using vue
# any routing other than the api will be handled by the SPA
def home(request):
    return render(request, 'main.html')
