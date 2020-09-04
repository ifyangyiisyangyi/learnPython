# Create your views here.
from django.http import JsonResponse
from django.views import View


class Cbvdemo(View):
    context = {
        'code': 0,
        'msg': ''
    }
    def get(self, request):
        self.context['msg'] = '这是Cbvdemo get请求'
        return JsonResponse(self.context)

    def pose(self, request):
        self.context['msg'] = '这是Cbvdemo post请求'
        return JsonResponse(self.context)
