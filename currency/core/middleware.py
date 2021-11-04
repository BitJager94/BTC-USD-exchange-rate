from django.conf import settings
from django.http import HttpResponse, response
class MWare:  
    def __init__(self, get_response):  
        self.get_response = get_response  
      
    def __call__(self, request):

        if "api" in request.path:
            try:
                if request.method == 'GET':
                    api_key = request.GET["apikey"]
                else:
                    api_key = request.POST['apikey']

                if api_key != settings.API_KEY:
                    return HttpResponse("You Are Not Authorized To Use This API")
                else:
                    response = self.get_response(request)
                    return response
            except Exception as e:
                return HttpResponse("You Are Not Authorized To Use This API")
        else:
            response = self.get_response(request)
            return response
