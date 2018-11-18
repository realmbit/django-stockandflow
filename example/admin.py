"""
Create a second admin site for the stocks and flows.
"""
from django.http import HttpResponseRedirect
from django.urls import reverse

from stockandflow.admin import StockAndFlowAdminSite


site = StockAndFlowAdminSite("sfadmin")

