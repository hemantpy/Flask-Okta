# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, current_app

from . import Resource
from api.auth import oidc, get_okta_client


class V1UsersUserId(Resource):

    @oidc.accept_token(require_token=True)
    def patch(self, user_id):
        okta_client = get_okta_client(current_app, service="users")
        print(g.json)

        return {}, 200, None
