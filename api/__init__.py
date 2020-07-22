# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask, g

from . import v1
from .auth import oidc, get_okta_client


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object("api.config")

    oidc.init_app(app)
    okta_client = get_okta_client(app, service="users")

    @app.before_request
    def before_request():
        if getattr(g, "oidc_id_token", None) is not None:
            g.user = okta_client.get_user(oidc.user_getfield("sub"))
        else:
            g.user = None

    app.register_blueprint(v1.bp, url_prefix='/api')
    return app
