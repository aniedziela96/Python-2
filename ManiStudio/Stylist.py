class Stylist:
    def __init__(self, exp = 1):
        self.current_client = None
        self.experience = exp

    def tick(self):
        if self.current_client is None:
            return

        for i in range(self.experience):
            self.current_client.paint()

        if self.current_client.is_done():
            self.current_client = None

    def busy(self):
        return self.current_client is not None

    def __str__(self):
        if not self.busy():
            return "Stylist: idle"
        return "Stylist: doing mani, {} steps remaining".format(self.current_client.get_steps())

    def start_next(self, new_client):
        self.current_client = new_client