from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/main.html'
    )
def main(request):
    return render(request, 'single_pages/main.html')
# Create your views here.
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )