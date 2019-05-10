# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from MyApi.models import FineFoods
from rest_framework import generics, mixins
from MyApi.serializers import FineFoodsSerializer


class RetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        =   'pk'
    queryset            =   FineFoods.objects.all()
    serializer_class    =   FineFoodsSerializer


class ListAndCreateApiView(generics.ListAPIView, mixins.CreateModelMixin):
    lookup_field        =   'pk'
    serializer_class    =   FineFoodsSerializer


    def get_queryset(self):
        query_data = FineFoods.objects.all()

        review_filter = self.request.GET.get('review')
        order_filter = self.request.GET.get('orderby')
        total_filter = self.request.GET.get('total')
        product_id_filter = self.request.GET.get('productid')
        user_id_filter = self.request.GET.get('userid')


        if total_filter and order_filter is not None:
            if order_filter == 'asc':
                query_data = FineFoods.objects.all().order_by('review')[:total_filter]
            elif order_filter == 'desc':
                query_data = FineFoods.objects.all().order_by('-review')[:total_filter]
        elif not total_filter and order_filter is not None:
            if order_filter == 'asc':
                query_data = FineFoods.objects.all().order_by('review')
            elif order_filter == 'desc':
                query_data = FineFoods.objects.all().order_by('-review')
        elif order_filter is not None:
            if order_filter == 'asc':
                query_data = FineFoods.objects.all().order_by('review')
            elif order_filter == 'desc':
                query_data = FineFoods.objects.all().order_by('-review')
        elif review_filter is not None:
            query_data = query_data.filter(
                Q(review__icontains=review_filter)
            ).distinct()
        elif product_id_filter:
            query_data = query_data.filter(
                Q(productId__icontains=product_id_filter)
            ).distinct()
        elif user_id_filter:
            query_data = query_data.filter(
                Q(userId__icontains=user_id_filter)
            ).distinct()
        elif not total_filter:
            query_data = FineFoods.objects.all()

        return query_data

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
