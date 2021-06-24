from django.urls import path
from .views import *

urlpatterns = [
    path('init_state/', get_workflow_init_state, name="get_workflow_init_state"),
    path('ticket_list/', ticket_list, name="ticket_list"),
    path('ticket_detail/', ticket_detail, name="ticket_detail"),
    path('ticket_transition/', ticket_transition, name="ticket_transition"),
    path('create_ticket/', create_ticket, name="create_ticket"),
    path('handle_ticker/', handle_ticket, name="handle_ticket"),
    path('user_login', user_login, name="login"),
    path('user_logout', user_logout, name="user_logout"),
]
