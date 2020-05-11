import itertools
import math
from random import randrange, seed


def closest_pair(from_set, to_set):
    closest_pair = None
    closest_distance = math.inf

    for a in from_set:
        for b in to_set:
            if a != b:
                ab_distance = distance(a, b)
                if ab_distance < closest_distance:
                    closest_pair = (a, b)
                    closest_distance = ab_distance

    return closest_pair


def distance(a, b):  # https://docs.python.org/3.8/library/math.html#math.dist
    return math.sqrt(sum((ad - bd) ** 2 for ad, bd in zip(a, b)))


NUM_POINTS = 3500

def generate_points(num_points=NUM_POINTS):
    seed(0)
    return [(randrange(0, 100), randrange(0, 100)) for _ in range(num_points)]
