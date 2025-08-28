from rest_framework.permissions import BasePermission, SAFE_METHODS
    
# This is a custom permission using BasePermission Class
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:

            # If the methods(GET, OPTIONS, HEAD) in SAFE_METHODS
            return True
        
        # else return the boolean result if the currently log user is the author of that blog post
        return obj.author == request.user