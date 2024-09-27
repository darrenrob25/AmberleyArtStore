from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ A view to view your basket """

    return render(request,'basket/basket.html')