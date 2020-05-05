from django.shortcuts import render
from django.views import generic
import json
import requests
from django.http import JsonResponse

# Create your views here.
from pulse_tracer.models import Device
from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(generic.ListView):
    template_name = 'pulse_tracer/index.html'
    def get(self, request, **kwargs):
        #id = []
        #device_model=[]
        #devices=Device.objects.all()
        #firstItem=devices[0].device_model
        lastItem=Device.objects.filter(id__range=(2,4)).values('id','device_model')
        #lastItem=Device.objects.filter(id__range=(0,3)).values('id','device_model')
        args = {'device':lastItem}
        #args=list(lastItem)
        #for log in lastItem :
        #        id.append(log.get(headline="id"))
        return render(request, self.template_name, args)
        #return JsonResponse(args, safe=False)  

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        
        min_id= request.GET.get('min_id') or 1  #Se lay min_id ben index.html
        #min_id = request.GET['min_id']
        max_id = request.GET.get('max_id') or 10
        # more stuff
        print("DEBUGGINNGGGGGGG")
        print(request.GET)

        lastItem=Device.objects.filter(id__range=(min_id,max_id)).values('id','device_model')
        data = {'device':lastItem}


        return Response(data)

class DataSummaryView(generic.TemplateView):
    template_name = 'pulse_tracer/data_summary.html'

    def get(self, request, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class HealthCareProviderDetail(generic.TemplateView):
    template_name = 'pulse_tracer/health_care_provider_detail.html'

    def get(self, request, **kwargs):
        context = {}
        return render(request, self.template_name, context)