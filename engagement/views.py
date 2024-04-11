from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact

# Create your views here.

@csrf_exempt
def create_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(request.POST)

        if name and email and message:
            contact = Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            return JsonResponse({'success': True, 'message': 'Contact created successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)