from django.shortcuts import render,HttpResponse
def index(request):
    # return render(request, "index.html")
    return HttpResponse('hello')





def main(request):
    return render(request, 'main.html')

# Create your views here.
