# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from api.auth import oidc


class V1Emails(Resource):

    @oidc.accept_token(require_token=True)
    def post(self):
        print(g.json)

        return None, 201, None
