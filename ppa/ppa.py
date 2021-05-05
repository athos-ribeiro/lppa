from lazr.restfulclient.errors import NotFound

from ppa.auth import Session

class PPA():
    def __init__(self, name):
        self.name = name
        self.session = Session().get_session()
        self.me = self.session.me

    def get(self):
        try:
            return self.me.getPPAByName(name=self.name)
        except NotFound:
            # TODO: debug log entry
            pass

    def create(self):
        ppa = self.get()
        if not ppa:
            pass
        return ppa
