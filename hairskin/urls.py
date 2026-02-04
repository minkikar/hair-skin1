from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("products/", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),
    path("products/<int:pk>/edit/", views.product_update, name="product_update"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
    path("recommendations/", views.recommendation_list, name="recommendation_list"),
    path("recommendations/new/", views.recommendation_create, name="recommendation_create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)