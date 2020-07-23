# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import current_app, g

from . import Resource
from api.auth import get_okta_client


class V1Tokens(Resource):

    def post(self):
        okta_client = get_okta_client(current_app, service="auth")

        try:
            username = g.json["username"]
            password = g.json["password"]
        except KeyError:
            return {"error": "Payload doesn't have a correct structure"}, 400

        try:
            response = okta_client.authenticate(username, password)
        except:
            return {"error": "There are problems on the server. Please try "
                             "again later"}, 500

        if response.status == "SUCCESS":
            profile = response.embedded.user.profile
            response_payload = {
                "id": response.embedded.user.id,
                "token": response.sessionToken,
                "expires_at": response.expiresAt,
                "login": profile.login,
                "first_name": profile.firstName,
                "last_name": profile.lastName,
            }

            return response_payload, 201, None

        return {
            "error": "There are problems on the server. Please try again later"
        }, 500
