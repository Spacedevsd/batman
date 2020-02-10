from batman.template import Template
from webob import Request, Response
from werkzeug.serving import run_simple


class Batman:    
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.app_response(request)
        
        return response(environ, start_response)

    def route(self, path):
        def decorator(f):
            self.routes[path] = f
            return f
        return decorator
    
    def _render(self, response, text=None, view=None):
        if text and not view:
            response.body = text
        
    def app_response(self, request):
        response = Response()

        for path, f in self.routes.items():
            if path == request.path:
                response = self.check_response(response, f())
        
        return response 

    def check_response(self, response, raw):
        if isinstance(raw, str):
            response.content_type = "text/plain"
            response.text = raw

        if isinstance(raw, bytes):
            response.content_type = "text/html"
            response.body = raw

        return response
    
    def run(self, port=5000, reloader=False, host="127.0.0.1"):
        run_simple(host, port, self, use_reloader=reloader)
    