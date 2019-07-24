from guardian.shortcuts import get_group_perms
from django.contrib.contenttypes.models import ContentType

def has_content_type_perm(user, model, perm):

    # get content_type instance from model
    content_type = ContentType.objects.get_for_model(model)

    # get user permissions
    if user.user_permissions.filter(content_type=content_type, codename=perm).count():
        return True

    # user groups
    user_groups = user.groups.all()

    # user permissions from groups

    for g in user_groups:
        if g.permissions.filter(content_type=content_type, codename=perm).count():
            return True

    return False