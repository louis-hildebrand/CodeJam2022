from django.http import HttpResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def test(request):
    """
    {
        "name": "Bob"
    }
    """
    print(request.data)
    name = request.data['name']
    return HttpResponse(f"Hello, {name}.")
