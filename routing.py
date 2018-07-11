from channels import include
from django.conf.urls import url

channel_routing = [
    # Include subrouting from an app with predefined path matching.
    include("bitpoint.messenger.routing.websocket_routing",
            url=r"^/")
]
