import os

OIDC_CLIENT_SECRETS = "client_secrets.json"
OIDC_COOKIE_SECURE = False  # TODO: turn on it when use SSL
OIDC_CALLBACK_ROUTE = "/oidc/callback"
OIDC_SCOPES = ["openid", "email", "profile"]
OIDC_RESOURCE_SERVER_ONLY = True
SECRET_KEY = "713e392fa89614ae56b780e43d3a5ed79515cb3518cbf406"

OKTA_ORG_URL = "https://dev-553399.okta.com"
OKTA_AUTH_TOKEN = "00PwSKyh9hedpxEWz_wsGmYLYpdUBm94Z4rpIKcjSv"
