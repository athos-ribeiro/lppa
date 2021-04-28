from launchpadlib.launchpad import Launchpad

API_VERSION = 'devel'
APP_NAME = 'ppa'
# LP_ENV = 'production'
LP_ENV = 'staging'


class AuthenticationError(Exception):
    pass


class Session():
    def __init__(self, anonymous=False, lp_env=LP_ENV):
        self.anonymous = anonymous
        self.lp_env = lp_env

    def _get_authenticated_session(self, anonymous_fallback):
        try:
            session = Launchpad.login_with(
                APP_NAME,
                self.lp_env,
                version=API_VERSION,
                credential_save_failed=self._no_auth_failure
            )
        except AuthenticationError:
            if not anonymous_fallback:
                raise

            self.anonymous = True
            session = self._get_anonymous_session()
        return session

    def _get_anonymous_session(self):
        return Launchpad.login_anonymously(APP_NAME, self.lp_env, version=API_VERSION)

    def _no_auth_failure(self):
        raise AuthenticationError(f"Could not Authenticate with Launchpad in '{self.lp_env}'")

    def get_session(self, anonymous_fallback=False):
        if self.anonymous:
            return self._get_anonymous_session()

        return self._get_authenticated_session(anonymous_fallback)
