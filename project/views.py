from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action 
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import ToDo, Task
from .serializers import TaskSerializer, ToDoSerializer

class TaskView(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('order')
	serializer_class = TaskSerializer
	filter_backends = (DjangoFilterBackend, ) 
	filter_fields = ('toDo', )

	@action(methods=['post'], detail=True)
	def post(self, request):
		print(request.data)
		serializer = serialize_class(request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('order')
	serializer_class = TaskSerializer
	filter_backends = (DjangoFilterBackend, ) 
	filter_fields = ('toDo', ) 
	#permission_classes = []

	@action(methods=['get'], detail=True)
	def taskList(self, request):
		qs = queryset.filter('toDo' == request.query.get('toDo', None))
		print(request.query.toDo)
		return Response(serializer(qs), status=status.HTTP_200_OK)

	@action(methods=['post'], detail=True) 
	def move(self, request, pk): 
		""" Move a single Step to a new position """ 
		obj = self.get_object()
		#params = request.data
		new_order = request.data.get('order', None) 
		toDo_target = request.data.get('toDo', None)

		toDo = ToDo.objects.filter(pk=toDo_target).get()
		# Make sure we received an order  
		if new_order is None and toDo is None: 
			return Response( 
				data={'error': 'No order or toDo given'},
				status=status.HTTP_400_BAD_REQUEST, 
			) 
		
		# Make sure our new order is not below one 
		if int(new_order) < 1: 
			return Response( 
				data={'error': 'Order nd toDo cannot be zero or below'},
				status=status.HTTP_400_BAD_REQUEST, 
			)
		
		Task.objects.move(obj, new_order, toDo) 
		return Response({'success': True, 'order': new_order})


# Create order in toDo
class TodoViewSet(viewsets.ModelViewSet):
	queryset = ToDo.objects.all()
	serializer_class = ToDoSerializer
	filter_backends = (DjangoFilterBackend, ) 
	
	filter_fields = ('group', )