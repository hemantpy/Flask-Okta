# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class ApiV1UsersUserId(Resource):

    def patch(self, user_id):
        print(g.json)

        return {}, 200, None
