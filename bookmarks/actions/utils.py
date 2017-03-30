from django.contrib.contenttypes.models import ContentType
from .models import Action


def create_action(user, verb, target=None):
    """
    The create_action() function allows to create actions that
    optionally include a target object. Function can by use
    anywhere in code to add new actions to the activity stream.
    """
    action = Action(user=user, verb=verb, target=target)
    action.save()