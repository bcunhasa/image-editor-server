"""Define the URL patterns for the API"""

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from editor.views import ImageResultView, ImageCreateView, GalleryView

helper_patterns = [
    # Return the final image
    url(r'^image/$', ImageResultView.as_view(), name='image'),
    
    # Create a new image
    url(r'^image/create/$', ImageCreateView.as_view(), name='create'),
    
    # Return the itens of the image gallery
    url(r'^image/gallery/$', GalleryView.as_view(), name='gallery')
]

urlpatterns = helper_patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
