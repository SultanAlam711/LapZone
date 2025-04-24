from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='home'),
    path('contact/',TemplateView.as_view(template_name='contact.html'),name='contact'),
    path('about/',TemplateView.as_view(template_name='about.html'),name='aboutpage'),
    path('product/', include('product.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('payment/', include('payment.urls')),
    path('order/', include('order.urls')),
    path('userprofile/', include('userprofile.urls')),


    

]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT)