from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view, obj):
        if request.METHOD in SAFE_METHODS:
            return True
        return obj.author == request.user