from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allows users to update their own Profile """

    def has_object_permission(self, request, view, obj):
        """ check if user has permission to do this action """

        if request.method in permissions.SAFE_METHODS:
            return True

        """ check if the user is trying to update his own profile """
        return obj.id == request.user.id

