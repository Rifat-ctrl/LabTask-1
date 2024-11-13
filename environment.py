# simulation/environment.py

class Environment:
    def __init__(self, width, height):
        self.width = width      # Environment width
        self.height = height    # Environment height

    def limit_position(self, x, y):
        # Ensure that x and y are within environment boundaries
        x = max(0, min(x, self.width))
        y = max(0, min(y, self.height))
        return x, y
