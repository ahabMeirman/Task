from django.shortcuts import render, redirect
from django.views.generic import View
import json
from basic.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from basic.models import *
from basic.serializers import *
from basic.forms import *



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
	

# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))

# class Serializejson(View):

# 	template_name = 'shema.html'

# 	def get(self, request):
# 		#value = data["employer"]

# 		# context = {
# 		# 	'value' : value,
# 		# }

# 		return render(request, self.template_name )

class Serializejson(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializers(company, many=True)
        return Response({"data": serializer.data})

    # def post(self, request):
    #     Room.objects.create()
    #     return Response(status=201)

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

		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect('table_url')
		return render(request, 'new_company_create.html', context={'form': bound_form})






