# simulation/agent.py

class Agent:
    def __init__(self, environment, x=0, y=0, speed=5):
        self.environment = environment  # Link to the environment
        self.x = x                      # Initial x position
        self.y = y                      # Initial y position
        self.speed = speed              # Movement speed

    def move(self, direction):
        if direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed
        elif direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed

        # Ensure the agent stays within environment boundaries with wrap-around
        self.x = self.x % self.environment.width
        self.y = self.y % self.environment.height
