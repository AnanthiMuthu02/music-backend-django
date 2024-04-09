from django.http import JsonResponse

class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if 'x-api-key' header exists in the request
        api_key = request.headers.get('x-api-key')

        # Replace 'YOUR_EXPECTED_API_KEY' with your actual expected API key
        expected_api_key = 'x-api-key'

        # Check if the API key matches the expected API key
        if api_key != expected_api_key:
            # Return a 403 Forbidden response if API key is missing or invalid
            return JsonResponse({'error': 'Unauthorized'}, status=403)

        # Pass the request to the next middleware or view function
        response = self.get_response(request)
        return response
