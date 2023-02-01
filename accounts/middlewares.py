class AdminUserMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                request.has_admin_access = True
            else:
                request.has_admin_access = False
        return self.get_response(request)
