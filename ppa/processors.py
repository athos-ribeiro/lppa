import logging
from typing import List, Type

from lazr.restfulclient.errors import NotFound

from ppa.auth import Session


logger = logging.getLogger(__name__)


class Processors():
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

        param name: str, a name of a LP processor, such as amd64
        raises NotFound: processor with requested name is not available
        return: An Entry containing data on the processor specified by name
        rtype: lazr.restfulclient.resource.Entry
        """
        try:
            return self.processors.getByName(name=name)
        except NotFound:
            logger.error(f'Could not find processor: "{name}"')
            raise
