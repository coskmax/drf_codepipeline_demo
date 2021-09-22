from rest_framework.response import Response
from rest_framework.views import APIView

class HealthCheckAPIView(APIView):

    def get(self, request):
        return Response()


class HelloAPIView(APIView):

    def get(self, request):
        return Response({
            'status': True,
            'message': "Hello World"
        })
