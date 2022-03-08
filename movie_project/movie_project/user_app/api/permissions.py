from rest_framework.permissions import BasePermission

# class UserAccessPermission(BasePermission):
#
#     message = 'You cannot access this resource.'
#
#     def has_permission(self, request, view):
#         if str(request.user.id) == view.kwargs['user_pk']:
#             return True
#         return False
