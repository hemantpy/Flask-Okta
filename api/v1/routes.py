# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.v1_users import V1Users
from .api.v1_users_user_id import V1UsersUserId
from .api.v1_tokens import V1Tokens
from .api.v1_tokens_token_id import V1TokensTokenId
from .api.v1_emails import V1Emails


routes = [
    dict(resource=V1Users, urls=['/v1/users'], endpoint='v1_users'),
    dict(resource=V1UsersUserId, urls=['/v1/users/<user_id>'], endpoint='v1_users_user_id'),
    dict(resource=V1Tokens, urls=['/v1/tokens'], endpoint='v1_tokens'),
    dict(resource=V1TokensTokenId, urls=['/v1/tokens/<int:token_id>'], endpoint='v1_tokens_token_id'),
    dict(resource=V1Emails, urls=['/v1/emails'], endpoint='v1_emails'),
]