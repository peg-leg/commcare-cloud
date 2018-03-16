import jsonobject


class MetaConfig(jsonobject.JsonObject):
    _allow_dynamic_properties = False
    deploy_env = jsonobject.StringProperty(required=True)
    env_name = jsonobject.StringProperty(required=True)
