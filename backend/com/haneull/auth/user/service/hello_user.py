from com.haneull.auth.user.service.abstract_user import AbstractUser


class HelloUser(AbstractUser):

    def handle(self, **kwargs):
        return "Hello User!"
