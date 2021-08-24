"""
Copyright (C) 2021 Athos Ribeiro

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from unittest.mock import patch

from lppa.ppa import PPA


@patch('launchpadlib.launchpad.Launchpad.login_with')
def test_set_archive(MockedSession):
    ppa = PPA('ppa_name', ['arch'])
    assert ppa.archive is None
    ppa.set_existing_archive()
    assert ppa.archive is not None


def test_set_archive_not_found():
    pass


def test_create_already_exists():
    pass


def test_create_new():
    pass


def test_get_processors_no_archive():
    pass


def test_get_processors():
    pass


@patch('launchpadlib.launchpad.Launchpad.login_with')
def test_dput_str(MockedSession):
    ppa = PPA('ppa_name', ['arch'])
    ppa.me.name = 'user'  # Mock yet another LP request
    dput = ppa.get_dput_str()
    assert dput == 'dput ppa:user/ppa_name <source.changes>'


def test_delete():
    pass


def test_delete_no_archive():
    pass
