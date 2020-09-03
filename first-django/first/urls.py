from django.urls import path, re_path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("select/", views.select, name="select"),
    path("result/", views.result, name="result"),

    # 정규표현식도 가능
    # re_path(r'^select/(?P<year>[0-9]{4}$)', views.select, name="select"),
    # path('select/<int:year>/', views.select, name="select")
    # <slug:>
    # <str:> 모든 문자열
]

# path parameter: /{aaa}/ (=pathVariable)
# query parameter: /?id=aaa (GET)
# form parameter: / (POST)