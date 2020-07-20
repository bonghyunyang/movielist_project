from rest_framework.views import APIView
from rest_framework.response import Response


class ListView(APIView):
    def get(self, request):
        return Response("작동상태 확인", status=200)
