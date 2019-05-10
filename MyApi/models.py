# -*- coding: utf-8 -*-

from django.db import models


class FineFoods(models.Model):
    productId       =       models.CharField(max_length=20, blank=False, null=False)
    userId          =       models.CharField(max_length=20, blank=False, null=False)
    profileName     =       models.CharField(max_length=20, blank=False, null=False)
    helpfulness     =       models.IntegerField(null=True, blank=True)
    review          =       models.FloatField(null=True, blank=True, default=None)
    review_time     =       models.DateTimeField(auto_now_add=True)
    review_summary  =       models.TextField(blank=False, null=False)
    review_text     =       models.TextField(blank=False, null=False)

    def __str__(self):
        return self.profileName
