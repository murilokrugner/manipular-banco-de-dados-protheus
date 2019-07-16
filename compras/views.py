from .models import Sc7010

def pedidos(request):
    c = list(Sc7010.objects.all())

    return render(request, 'pedidos.html', {'c': c})