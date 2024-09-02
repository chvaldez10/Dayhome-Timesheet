from ninja import NinjaAPI, Schema

api = NinjaAPI()

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None

@api.get("/user", response=UserSchema)
def get_user(request):
    return request.user