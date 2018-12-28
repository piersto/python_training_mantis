from sys import maxsize


class Project:
    def __init__(self, name=None, status=None, enabled=None, view_status=None, description=None):
        self.name = name
        self.status = status
        self.enabled = enabled
        self.view_status = view_status
        self.description = description

    def __eq__(self, other):
        return self.name == other.name

    '''def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize'''

    def __repr__(self):
        return "%s:%s;%s" % (self.name, self.status, self.enabled)
