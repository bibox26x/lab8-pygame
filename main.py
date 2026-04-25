import random
from typing import TypedDict

import pygame


WIDTH = 800
HEIGHT = 600
FPS = 60

SQUARE_COUNT = 100
MIN_SQUARE_SIZE = 10
MAX_SQUARE_SIZE = 50
FLEE_DISTANCE = 120
FLEE_STRENGTH = 1.5


Color = tuple[int, int, int]


class Square(TypedDict):
	x: float
	y: float
	size: int
	speed_x: float
	speed_y: float
	color: Color


def random_direction(speed: int) -> int:
	"""Return either +speed or -speed."""
	return random.choice([-speed, speed])


def create_square() -> Square:
	"""Create one square with random position, color, and movement."""
	size = random.randint(MIN_SQUARE_SIZE, MAX_SQUARE_SIZE)
	x = random.randint(0, WIDTH - size)
	y = random.randint(0, HEIGHT - size)

	color: Color = (
		random.randint(0, 255),
		random.randint(0, 255),
		random.randint(0, 255),
	)

	speed = max(1, 6 - (size // 10))
	speed_x = random_direction(speed)
	speed_y = random_direction(speed)

	return {
		"x": x,
		"y": y,
		"size": size,
		"speed_x": speed_x,
		"speed_y": speed_y,
		"color": color,
	}


def get_square_center(square: Square) -> tuple[float, float]:
	"""Return the center point of a square."""
	size = square["size"]
	return square["x"] + size / 2, square["y"] + size / 2


def calculate_flee_offset(square: Square, squares: list[Square]) -> tuple[float, float]:
	"""Small squares run away from nearby bigger squares."""
	square_cx, square_cy = get_square_center(square)
	away_x = 0.0
	away_y = 0.0

	for other in squares:
		if other is square:
			continue
		if other["size"] <= square["size"]:
			continue

		other_cx, other_cy = get_square_center(other)
		dx = square_cx - other_cx
		dy = square_cy - other_cy
		distance_squared = dx * dx + dy * dy

		if distance_squared == 0:
			continue
		if distance_squared > FLEE_DISTANCE * FLEE_DISTANCE:
			continue

		distance = distance_squared ** 0.5
		# Closer bigger squares push harder; farther ones push less.
		closeness = (FLEE_DISTANCE - distance) / FLEE_DISTANCE

		away_x += (dx / distance) * closeness
		away_y += (dy / distance) * closeness

	return away_x * FLEE_STRENGTH, away_y * FLEE_STRENGTH


def main() -> None:
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Bouncing Squares")
	clock = pygame.time.Clock()

	squares = [create_square() for _ in range(SQUARE_COUNT)]

	running = True
	while running:
		dt = clock.tick(FPS) / 1000.0
		frame_scale = dt * FPS

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for square in squares:
			size = square["size"]
			flee_x, flee_y = calculate_flee_offset(square, squares)
			square["x"] += (square["speed_x"] + flee_x) * frame_scale
			square["y"] += (square["speed_y"] + flee_y) * frame_scale

			if square["x"] <= 0 or square["x"] >= WIDTH - size:
				square["speed_x"] *= -1
				square["x"] = max(0, min(square["x"], WIDTH - size))

			if square["y"] <= 0 or square["y"] >= HEIGHT - size:
				square["speed_y"] *= -1
				square["y"] = max(0, min(square["y"], HEIGHT - size))

		screen.fill((20, 20, 20))
		for square in squares:
			size = square["size"]
			pygame.draw.rect(
				screen,
				square["color"],
				(int(square["x"]), int(square["y"]), size, size),
			)

		pygame.display.flip()

	pygame.quit()


if __name__ == "__main__":
	main()
