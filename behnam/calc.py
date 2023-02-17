import http

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(('POST',))
def clc_(request):
    return Response({"behnam":36},http.HTTPStatus.BAD_REQUEST)