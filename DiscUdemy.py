class DiscUdemy:
    def __init__(self, bound_data):
        self.name = bound_data[1]
        self.url = bound_data[0]

    def __str__(self):
        return "name: {}, url : {}".format(self.name, self.url)

    def __repr__(self):
        return "{}, {}".format(self.name.replace(',', '-'), self.url)
