#!/opt/app/kns/bin/python
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/opt/app/kns/releases/current/")
sys.path.insert(0, "/opt/app/kns/releases/current/kns")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "kns.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
