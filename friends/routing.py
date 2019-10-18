from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import mychat.routing

application = ProtocolTypeRouter({

    'websocket': AuthMiddlewareStack(
        URLRouter(
            mychat.routing.websocket_urlpatterns
        )
    ),
})
