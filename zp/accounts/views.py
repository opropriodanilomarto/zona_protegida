"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>

Implementing the login and logout feature
"""

from django.contrib.auth import views


class Login(views.LoginView):
    pass


class Logout(views.LogoutView):
    pass
