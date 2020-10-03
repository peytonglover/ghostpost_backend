from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from homepage.serializer import BoastSerializer, RoastSerializer
from homepage.models import boast, roast
from drf_multiple_model.views import ObjectMultipleModelAPIView
# Create your views here.
class HomeAPIView(ObjectMultipleModelAPIView):
    querylist=[
        {'queryset': boast.objects.order_by('posted_at'), 'serializer_class': BoastSerializer},
        {'queryset': roast.objects.order_by('posted_at'), 'serializer_class': RoastSerializer}
    ]


class boastViewSet(viewsets.ModelViewSet):
    queryset = boast.objects.all()
    serializer_type = BoastSerializer

    @action(detail=True, methods=['post'])
    def upvote_boast(self, request, pk=None):
        boast = self.get_object()
        serializer = BoastSerializer(data=request.data)
        if serializer.is_valid():
            boast.upvotes += 1
            boast.save()
            return Response({'status': 'boast upvoted'}) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def downvote_boast(self, request, pk=None):
        boast = self.get_object()
        serializer = BoastSerializer(data=request.data)
        if serializer.is_valid():
            boast.downvotes += 1
            boast.save()
            return Response({'status': 'boast downvoted'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class roastViewSet(viewsets.ModelViewSet):
    queryset = roast.objects.all()
    serializer_type = RoastSerializer

    @action(detail=True, methods=['post'])
    def upvote_roast(self, request, pk=None):
        roast = self.get_object()
        serializer = RoastSerializer(data=request.data)
        if serializer.is_valid():
            roast.upvotes += 1
            roast.save()
            return Response({'status': 'roast upvoted'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def downvote_roast(self, request, pk=None):
        roast = self.get_object()
        serializer = RoastSerializer(data=request.data)
        if serializer.is_valid():
            roast.downvotes += 1
            roast.save()
            return Response({'status': 'roast downvoted'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    