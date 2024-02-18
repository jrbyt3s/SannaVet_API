
from rest_framework import permissions

class RolePermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        #
        edad = 20
        if edad > 40:
            return True

        return False
