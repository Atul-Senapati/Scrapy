"""API + frontend on one port:  python serve.py  ->  http://localhost:8000/app/"""
import bottle
from bottle import static_file, redirect
from cheroot import wsgi

import config
import routes  # noqa: F401


@bottle.hook("before_request")
def _root_to_frontend():
    # the site root opens the UI; /health still returns the API status
    if bottle.request.path == "/":
        redirect("/app/")


@bottle.route("/app")
def _app_redirect():
    redirect("/app/")


@bottle.route("/app/")
@bottle.route("/app/<path:path>")
def _frontend(path="index.html"):
    return static_file(path, root="frontend")


if __name__ == "__main__":
    print(f"Frontend: http://localhost:{config.PORT}/app/", flush=True)
    wsgi.Server(("0.0.0.0", config.PORT), bottle.default_app(), numthreads=16).start()
