from django.urls import path

from user.views import log, reg, prof

app_name = 'user'

urlpatterns = [
    path('login/', log, name='log'),
    path('reg/', reg, name='reg'),
    path('prof/', prof, name='prof'),

]
