from django.conf.urls import url
from stockandflow.views import stock_line_chart


urlpatterns = [
    url(r"^stock/line/(?P<slug>[-\w]+)/$", stock_line_chart, name="stock_line_chart"),
]
