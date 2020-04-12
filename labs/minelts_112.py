from priority_queue_112 import PQ
import sys

def main():
    o = int(sys.argv[1])
    p_q = PQ()

    for t in sys.stdin:
        t = int(t.strip())

        if p_q.size() < o:
            p_q.insert(t)
            continue

        elif t < p_q.getMax():
            p_q.delMax()
            p_q.insert(t)

    while not p_q.is_empty():
        print(p_q.delMax())

if __name__ == '__main__':
    main()
