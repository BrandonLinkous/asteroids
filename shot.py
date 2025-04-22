from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, position, radius=SHOT_RADIUS):
        super().__init__(position.x, position.y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 83, 73), (self.position.x, self.position.y), SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt
