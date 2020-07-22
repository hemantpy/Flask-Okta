# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, current_app

from . import Resource
from api.auth import get_okta_client


class V1Users(Resource):

    def post(self):
        okta_client = get_okta_client(current_app, service="users")

        username = g.json["username"]
        password = g.json["password"]

        return [], 200, None
