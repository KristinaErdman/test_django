def my_middleware(next):
    def core_middleware(request):
        hosts = {
            'localhost:8000': 'rus',
            'localhost:9000': 'kz',
        }
        request.using_db = hosts.get(request.get_host(), None)
        response = next(request)
        return response

    return core_middleware
