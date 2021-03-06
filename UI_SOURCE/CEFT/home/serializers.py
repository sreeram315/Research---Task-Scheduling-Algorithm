from django.db.models import Count
from django.conf import settings
from django.db import connection
from rest_framework import serializers



class CEFTSerializer(serializers.Serializer):
	nprocessors = serializers.IntegerField(min_value=1, max_value=100)
	ntasks 		= serializers.IntegerField(min_value=1, max_value=1000)
	nedges 		= serializers.IntegerField()
	processing_time 	= serializers.ListField()
	edges 		= serializers.ListField()

	def validate_processing_time(self, processing_time):
		np = self.initial_data['nprocessors']
		nt = self.initial_data['ntasks']
		s = len(processing_time)
		try:
			if(int(np)!=int(s) or (not all([len(t)==int(nt) for t in processing_time]))):
				raise serializers.ValidationError(f"INVALID DATA. Give processing time for exactly {nt} tasks for {np} processors | Got {s} tasks")
			return processing_time
		except:
			raise serializers.ValidationError(f"Bad input for processing times | Give processing time for exactly <{nt}> tasks and  <{np}> processors | Got {s} tasks")

	def validate_edges(self, edges):
		ne = self.initial_data['nedges']
		s = len(edges)
		try:
	#		print(f"ne={ne} s={s} {type(ne)} {type(s)}")
			if(int(ne)!=int(s)):
				raise serializers.ValidationError(f"INVALID DATA. Give exactly {ne} edges and corresponding weights | Needed:{ne} Got:{s}")
			return edges
		except:
			raise serializers.ValidationError(f"Bad input for dependencies | Give exactly <{ne}> edges and corresponding weights | Needed:<{ne}> Got:<{s}>")



















