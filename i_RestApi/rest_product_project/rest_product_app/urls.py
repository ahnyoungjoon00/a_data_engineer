from django.urls import path
from . import views
urlpatterns = [
    # path("", views.index, name ="index"),
    path("products/", views.prdsAPI, name ="prdsAPI"),
    path("product/<int:prd_no>/", views.prdAPI, name ="prdAPI"),

    path("cbv/products/", views.ProductsAPI.as_view(), name ="ProductsAPI"),
    path("cbv/product/<int:prd_no>/", views.ProductAPI.as_view(), name ="ProductAPI"),

    path("mixin/products/", views.ProductsAPIMinxins.as_view(), name ="ProductsAPIMinxins"),
    path("mixin/product/<int:prdno>/", views.ProductAPIMinxins.as_view(), name ="ProductAPIMinxins"),

    path("generic/products/", views.ProductAPIgenList.as_view(), name ="ProductsAPIgen"),
    path("generic/product/<int:prdno>/", views.ProductAPIgenRetri.as_view(), name ="ProductAPIgen"),
]
