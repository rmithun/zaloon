from rest_framework import permissions


class IsUserThenReadPatch(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj = None):
        

        allowed_methods = ['GET','PATCH','PUT']
        #if request.method in permissions.SAFE_METHODS:
        #    return True
        # Write permissions are only allowed to the respective user.
        if request.method in allowed_methods:
            return obj is None or obj.user == request.user
        return False

class ReadOnlyAuthentication(permissions.BasePermission):

    """
    read only permissions for reading data for populating forms
    """

    def has_permission(self, request, view):

        allowed_methods = ['GET',]
        ## only read method allowed for authenticated users
        if (request.method in allowed_methods and request.user.is_authenticated()):
            return True
        return False


class ReadWithoutAuthentication(permissions.BasePermission):

    """
    read only permissions for reading data for populating forms
    """

    def has_permission(self, request, view):

        allowed_methods = ['GET',]
        ## only read method allowed for authenticated users
        if (request.method in allowed_methods):
            return True
        return False

class IsUserThenPut(permissions.BasePermission):

    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj = None):
        

        allowed_methods = ['PUT']
        #if request.method in permissions.SAFE_METHODS:
        #    return True
        # Write permissions are only allowed to the respective user.
        if request.method in allowed_methods:
            return obj is None or obj.user == request.user
        return False

