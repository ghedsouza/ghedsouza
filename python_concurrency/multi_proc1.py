import math
from multiprocessing import Process, Queue
from algorithm import closest_pair, generate_points


def doit(q, *args):
    q.put(closest_pair(*args))


if __name__ == "__main__":
    q = Queue()

    points = generate_points()

    x1 = Process(target=doit, args=(q, points[: len(points) // 2], points),)
    x2 = Process(target=doit, args=(q, points[len(points) // 2 :], points),)
    x1.start()
    x2.start()
    x1.join()
    x2.join()

    res1 = q.get()
    res2 = q.get()

    closest = min([res1, res2], key=lambda res: math.dist(res[0], res[1]))
    print(closest)
