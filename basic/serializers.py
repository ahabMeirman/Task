from rest_framework import serializers
from basic.models import *


class CompanySerializers(serializers.ModelSerializer):

	class Meta:
		model = Company
		fields = ("rank", "employer", "employees", "salary")

