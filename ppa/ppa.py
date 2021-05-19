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
from ppa.processors import Processors


logger = logging.getLogger(__name__)


class PPA():
    """Launchpad PPA manager class"""
    def __init__(self, name, architectures):
        """Initializer

        param name: str, the name for the PPA to be managed
        param architectures: list[str], list of launchpad processors, such as arm64
        """
        self.name = name
        self.session = Session().get_session()
        self.me = self.session.me
        self.team = self.session.people[self.me.name]
        self.architectures = architectures

    def get(self):
        """get the PPA archive interface

        return: An Entry representing a launchpad archive
        rtype: lazr.restfulclient.resource.Entry
        """
        try:
            return self.me.getPPAByName(name=self.name)
        except NotFound:
            logger.warning(
                f'No "{self.name}" PPA available. Try creating one with the "create" method'
            )

    def create(self, displayname=None, description=None):
        """get the PPA archive interface

        param displayname: str, the display name for the PPA to be managed
        param description: str, the description for the PPA to be managed
        return: An Entry representing a launchpad archive
        rtype: lazr.restfulclient.resource.Entry
        """
        ppa = self.get()
        if not ppa:
            displayname = displayname or self.name
            # TODO: why isn't the documented person.createPPA working?
            ppa = self.team.createPPA(
                name=self.name,
                displayname=displayname,
                description=description,
            )
        processors_api = Processors()
        processor_urls = []
        for arch in self.architectures:
            processor_urls.append(processors_api.get_by_name(arch).self_link)
        ppa.setProcessors(processors=processor_urls)
        return ppa