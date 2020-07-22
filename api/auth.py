import okta
from flask_oidc import OpenIDConnect

oidc = OpenIDConnect()


def get_okta_client(app, service, *args, **kwargs):
    CLIENT_MAPPING = {
        "app_instance": okta.AppInstanceClient,
        "auth": okta.AuthClient,
        "events": okta.EventsClient,
        "factors_admin": okta.FactorsAdminClient,
        "factors": okta.FactorsClient,
        "sessions": okta.SessionsClient,
        "user_groups": okta.UserGroupsClient,
        "users": okta.UsersClient,
    }

    if service not in CLIENT_MAPPING:
        raise ValueError(
            "Okta doesn't support current client service: {}. Use one "
            "of accepted: {}".format(type, list(CLIENT_MAPPING))
        )

    client_class = CLIENT_MAPPING[service]
    okta_client = client_class(
        app.config["OKTA_ORG_URL"],
        app.config["OKTA_AUTH_TOKEN"],
        *args, **kwargs
    )

    return okta_client
