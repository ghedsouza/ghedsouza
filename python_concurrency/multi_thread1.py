import queue
import threading

from algorithm import closest_pair, distance, generate_points

points = generate_points()

q = queue.Queue()
x1 = threading.Thread(
    target=lambda *args: q.put(closest_pair(*args)),
    args=(points[:len(points) // 2], points),
)
x2 = threading.Thread(
    target=lambda *args: q.put(closest_pair(*args)),
    args=(points[len(points) // 2:], points),
)
x1.start()
x2.start()
x1.join()
x2.join()

res1 = q.get()
res2 = q.get()

closest = min([res1, res2], key=lambda res: distance(res[0], res[1]))
print(closest)
