# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, current_app
from okta.framework.OktaError import OktaError

from . import Resource
from api.auth import get_okta_client, forgot_password


class V1Emails(Resource):

    def post(self):
        okta_client = get_okta_client(current_app, service="auth")

        try:
            forgot_password(
                auth_client=okta_client,
                username=request.json["username"],
                factor_type="EMAIL",
            )
            return None, 201, None
        except OktaError:
            return {"error": "Your username isn't correct."}, 400, None
