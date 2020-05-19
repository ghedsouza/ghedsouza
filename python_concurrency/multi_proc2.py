import itertools
import multiprocessing

from algorithm import closest_pair, distance, generate_points


def segment_list(l, N):
    chunk_size, remainder = len(l) // N, len(l) % N
    first, rest = l[:chunk_size + remainder], l[chunk_size + remainder:]
    return itertools.chain([first], zip(*[iter(rest)] * chunk_size))


points = generate_points()

N = multiprocessing.cpu_count()  # 8 for me.
segments = segment_list(points, N)

def do_it(segment):
    return closest_pair(segment, points)

pool = multiprocessing.Pool(processes=N)
results = pool.map(do_it, segments)

closest = min(results, key=lambda res: distance(res[0], res[1]))
print(closest)
