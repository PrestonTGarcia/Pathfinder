class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def get_weight(self):
        return self.weight