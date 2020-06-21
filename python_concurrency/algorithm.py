import math
from random import randrange, seed


def closest_pair(from_set, to_set):
    best_pair = None
    best_distance = math.inf

    for a in from_set:
        for b in to_set:
            if a != b:
                if (ab_distance := math.dist(a, b)) < best_distance:
                    best_pair = (a, b)
                    best_distance = ab_distance

    return best_pair


NUM_POINTS = 10_000


def generate_points(num_points=NUM_POINTS):
    seed(0)
    return [(randrange(0, 100), randrange(0, 100)) for _ in range(num_points)]
