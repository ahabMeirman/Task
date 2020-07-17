from django.shortcuts import render, redirect
from django.views.generic import View
import redis
import json
from basic.serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response

# Create your views here.
from basic.models import *
from basic.serializers import *
from basic.forms import *

# connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
								   port=settings.REDIS_PORT, db=0)


with open('data.json', 'r', encoding='utf-8') as f:
	templates = json.load(f)

g = Company.objects.values()
if g:
	for num, temp in enumerate(templates):
		if temp['employer'] != g[num]['employer']:
			print(g[num]['employer'], temp['employer'])
			Company.objects.create(rank=temp['rank'], employer=temp['employer'],employees=temp['employeesCount'],salary=temp['medianSalary'])
else:
	for temp in templates:
		Company.objects.create(rank=temp['rank'], employer=temp['employer'],employees=temp['employeesCount'],salary=temp['medianSalary'])
	



class Serializejson(APIView):

	def get(self, request):
		company = Company.objects.all()
		serializer = CompanySerializers(company, many=True)
		return Response({"data": serializer.data})



class Table(View):

	template_name = 'shema.html'



	def get(self, request):
		companys = Company.objects.all()

		context = {
			'companys' : companys,
		}
		return render(request, self.template_name, context)


class CreateCampony(View):

	def get(self, request):
		form = CompanyForm()
		return render(request, 'new_company_create.html', context={'form': form})
	
	def post(self, request):
		bound_form = CompanyForm(request.POST)

		company = Company.objects.all()
		serializer = CompanySerializers(company, many=True)

		if bound_form.is_valid():

			#добавляем в REDIS
			item = Company.objects.values('rank', 'employer', 'employees','salary').last()
			for n, i in enumerate(item):
				key = list(item.keys())[n]
				val = list(item.values())[n]
				redis_instance.set(key, val)
			
			print('successfully')

			new_tag = bound_form.save()
			return redirect('table_url')
		return render(request, 'new_company_create.html', context={'form': bound_form})


#проверка REDIS здесь только один отоброжаеться , неуспел сделать
@api_view(['GET', 'POST'])
def manage_items(request, *args, **kwargs):
	if request.method == 'GET':
		items = {}
		count = 0
		for key in redis_instance.keys("*"):
			items[key.decode("utf-8")] = redis_instance.get(key)
			count += 1
		response = {
			'count': count,
			'msg': f"Found {count} items.",
			'items': items
		}
		return Response(response, status=200)







