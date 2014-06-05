# Installed packages
from django.conf.urls import patterns, url

# Local code
from views import Asset, AssetList, AssetJson

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

urlpatterns = patterns(
    '',
    url(r'^v1/$', AssetList.as_view()),
    url(r'^v1/(?P<filename>.+)\.json$', AssetJson.as_view()),
    url(r'^v1/(?P<filename>.+)$', Asset.as_view()),
)