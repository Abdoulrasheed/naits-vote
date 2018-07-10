from channels import include

channel_routing = [
    # Include subrouting from an app with predefined path matching.
    include("bitpoint.messenger.routing.websocket_routing",
            path=r"^/")
]
