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
import logging

from lazr.restfulclient.errors import NotFound

from ppa.auth import Session


logger = logging.getLogger(__name__)


class Processors():
    """Launchpad builder platform's abstractions"""
    def __init__(self):
        self.session = Session().get_session()
        self.processors = self.session.processors

    def list(self):
        """List all processors available in LP instance

        return: A list with all processors available in a LP instance
        rtype: list
        """
        return [p.name for p in self.processors]

    def get_by_name(self, name):
        """Get a processor object by its arch name

        param name: str, a name of an LP processor, such as amd64
        raises NotFound: processor with requested name is not available
        return: An Entry containing data on the processor specified by name
        rtype: lazr.restfulclient.resource.Entry
        """
        try:
            return self.processors.getByName(name=name)
        except NotFound:
            logger.error(f'Could not find processor: "{name}"')
            raise
