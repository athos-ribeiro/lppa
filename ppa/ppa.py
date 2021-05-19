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
            logger.debug(
                'No %s PPA available. Try creating one with the "create" method', self.name
            )

    def create(self, displayname=None, description=None):
        """get the PPA archive interface

        param displayname: str, the display name for the PPA to be managed
        param description: str, the description for the PPA to be managed
        return: An Entry representing a launchpad archive
        rtype: lazr.restfulclient.resource.Entry
        """
        ppa = self.get()
        if ppa:
            logger.debug('A PPA named %s already exists', self.name)
        else:
            logger.debug('Creating PPA: %s', self.name)
            displayname = displayname or self.name
            # TODO: why isn't the documented person.createPPA working?
            ppa = self.team.createPPA(
                name=self.name,
                displayname=displayname,
                description=description,
            )
        processors_api = Processors(session=self.session)
        processor_urls = []
        for arch in self.architectures:
            logger.debug('Fetching processor url for "%s"', arch)
            processor_urls.append(processors_api.get_by_name(arch).self_link)
        ppa.setProcessors(processors=processor_urls)
        logger.info('PPA: "%s" is available for arches: %s', self.name, self.get_processors(ppa))
        return ppa

    def get_processors(self, ppa):
        """get the processors enabled for the PPA archive

        param ppa: lazr.restfulclient.resource.Entry, An Entry representing an LP archive
        return: List of strings representing LP processor names such as amd64
        rtype: list
        """
        arches = []
        for arch in ppa.processors:
            arches.append(arch.name)
        return arches
