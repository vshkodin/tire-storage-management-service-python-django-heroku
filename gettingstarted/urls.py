from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

admin.autodiscover()

import hello.views as h

urlpatterns = [
    path("", h.index, name="index"),
    path("home/", h.home, name="home"),
    path("admin/", admin.site.urls),
    #path("db/", h.db, name="db"),
    path("removeClient/", h.removeClient, name="removeClient"),
    path("createClient/", h.createClient, name="createClient"),
    path("updateClient/", h.updateClient, name="updateClient"),
    path("editClient/", h.editClient, name="editClient"),
    path("pdf/", h.GeneratePdf.as_view(), name="pdf"),

]
