from unittest.mock import patch

import pytest

from ppa import auth


@patch('launchpadlib.launchpad.Launchpad.login_with')
@patch('launchpadlib.launchpad.Launchpad.login_anonymously')
def test_anonymous_session(MockedAnon, MockedAuth):
    session = auth.Session(anonymous=True)
    session.get_session()
    MockedAuth.assert_not_called()
    MockedAnon.assert_called_once()


@patch('launchpadlib.launchpad.Launchpad.login_with')
@patch('launchpadlib.launchpad.Launchpad.login_anonymously')
def test_authenticated_session(MockedAnon, MockedAuth):
    session = auth.Session()
    session.get_session()
    MockedAnon.assert_not_called()
    MockedAuth.assert_called_once()


@patch('launchpadlib.launchpad.Launchpad.login_with', side_effect=auth.AuthenticationError)
@patch('launchpadlib.launchpad.Launchpad.login_anonymously')
def test_auth_error_no_fallback(MockedAnon, MockedAuth):
    session = auth.Session()
    with pytest.raises(auth.AuthenticationError):
        session.get_session()
    MockedAuth.assert_called_once()
    MockedAnon.assert_not_called()


@patch('launchpadlib.launchpad.Launchpad.login_with', side_effect=auth.AuthenticationError)
@patch('launchpadlib.launchpad.Launchpad.login_anonymously')
def test_auth_error_with_fallback(MockedAnon, MockedAuth):
    session = auth.Session()
    session.get_session(anonymous_fallback=True)
    MockedAuth.assert_called_once()
    MockedAnon.assert_called_once()
