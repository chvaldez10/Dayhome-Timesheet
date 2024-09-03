from ninja import NinjaAPI, Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController


api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None

@api.get("/user", response=UserSchema, auth=JWTAuth())
def get_user(request):
    return request.user