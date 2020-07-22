# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.api_v1_users import ApiV1Users
from .api.api_v1_users_user_id import ApiV1UsersUserId
from .api.api_v1_tokens import ApiV1Tokens
from .api.api_v1_tokens_token_id import ApiV1TokensTokenId
from .api.api_v1_emails import ApiV1Emails


routes = [
    dict(resource=ApiV1Users, urls=['/api/v1/users'], endpoint='api_v1_users'),
    dict(resource=ApiV1UsersUserId, urls=['/api/v1/users/<int:user_id>'], endpoint='api_v1_users_user_id'),
    dict(resource=ApiV1Tokens, urls=['/api/v1/tokens'], endpoint='api_v1_tokens'),
    dict(resource=ApiV1TokensTokenId, urls=['/api/v1/tokens/<int:token_id>'], endpoint='api_v1_tokens_token_id'),
    dict(resource=ApiV1Emails, urls=['/api/v1/emails'], endpoint='api_v1_emails'),
]