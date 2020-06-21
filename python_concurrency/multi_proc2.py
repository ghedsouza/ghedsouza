import itertools
import multiprocessing
import math

from algorithm import closest_pair, generate_points


def segment_list(l, N):
    chunk_size, remainder = divmod(len(l), N)
    first, rest = l[: chunk_size + remainder], l[chunk_size + remainder :]
    return itertools.chain([first], zip(*[iter(rest)] * chunk_size))


def do_it(segment, points):
    return closest_pair(segment, points)


if __name__ == "__main__":
    N = multiprocessing.cpu_count()  # 8 for me.

    points = generate_points()
    segments = list(segment_list(points, N))
    proc_args = list(zip(segments, [points] * N))

    pool = multiprocessing.Pool(processes=N)
    results = pool.starmap(do_it, proc_args)

    closest = min(results, key=lambda res: math.dist(res[0], res[1]))
    print(closest)
