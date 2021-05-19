from launchpadlib.launchpad import Launchpad


API_VERSION = 'devel'
APP_NAME = 'ppa'
LP_ENV = 'production'  # or staging


class AuthenticationError(Exception):
    """Error for authentication failures"""


class Session():
    """Launchpad session interface"""
    def __init__(self, anonymous=False, lp_env=LP_ENV):
        """Initializer

        param anonymous: bool, whether to use an anonimous session
        param lp_env: string, launchpad environment to pass to launchpadlib
        """
        self.anonymous = anonymous
        self.lp_env = lp_env

    def _get_authenticated_session(self, anonymous_fallback):
        """Retrieve a new launchpad authenticated session

        param anonymous_fallback: bool, whether to fallback to an anonimous session on
            authentication failures
        raises AithenticationError: Failed to authenticate without anonymous fallbacks enabled
        return: Launchpad session
        rtype: launchpadlib.launchpad.Launchpad
        """
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
        """Retrieve a new anonymous launchpad session

        return: Launchpad session
        rtype: launchpadlib.launchpad.Launchpad
        """
        return Launchpad.login_anonymously(APP_NAME, self.lp_env, version=API_VERSION)

    def _no_auth_failure(self):
        raise AuthenticationError(f"Could not Authenticate with Launchpad in '{self.lp_env}'")

    def get_session(self, anonymous_fallback=False):
        """Retrieve a new launchpad session

        param anonymous_fallback: bool, whether to fallback to an anonimous session on
            authentication failures
        return: Launchpad session
        rtype: launchpadlib.launchpad.Launchpad
        """
        if self.anonymous:
            return self._get_anonymous_session()

        return self._get_authenticated_session(anonymous_fallback)
