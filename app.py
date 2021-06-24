import pathlib
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
import sys
from django.core.wsgi import get_wsgi_application
import os
from decouple import config
import django



settings.configure(DEBUG=True,
                   SECRET_KEY=config('SECRET_KEY'), 
                   ALLOWED_HOST=['*'],
                   ROOT_URLCONF=__name__,            
                )

def home_view(request, *args, **kwargs):
    return HttpResponse('<h3>Funcionandos.</h3>')

    
application = get_wsgi_application()

urlpatterns = [
   path('', home_view, name='home'),
]


if __name__ == '__main__':
    try:
        from django.core.management import execute_from_command_line
        django.setup()
    except ImportError as exc:
        raise ImportError(
            """
            teste
            """
        ) from exc 
    execute_from_command_line(sys.argv)
    

    
    