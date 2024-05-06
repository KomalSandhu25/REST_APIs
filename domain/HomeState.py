class HomeState:
    def __init__(self, ID, state, occupied, present):
        self.ID = ID
        self.state = state
        self.present = present
        self.occupied = occupied



    def __str__(self):
        return f"ID: {self.ID}, State: {self.state}, Present: {self.present}, Occupied: {self.occupied}"

