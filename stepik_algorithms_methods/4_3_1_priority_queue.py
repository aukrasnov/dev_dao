class PriorityQueue(list):
    @staticmethod
    def parent(i):
        return (i + 1) // 2 - 1

    @staticmethod
    def right_child(i):
        return (i + 1) * 2

    @staticmethod
    def left_child(i):
        return (i + 1) * 2 - 1

    def safe_value(self, i):
        try:
            return self[i]
        except IndexError:
            return -float("inf")

    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def next(self, i):
        r_i = self.right_child(i)
        l_i = self.left_child(i)
        return r_i if self.safe_value(r_i) > self.safe_value(l_i) else l_i

    def last_idx(self):
        return len(self) - 1

    def sift_up(self, n, i):
        j = self.parent(i)
        if j >= 0 and self[j] < n:
            self.swap(i, j)
            self.sift_up(n, j)

    def sift_down(self, n, i):
        j = self.next(i)
        if j <= self.last_idx() and self[j] > n:
            self.swap(i, j)
            self.sift_down(n, j)

    def append(self, n):
        super().append(n)
        self.sift_up(n, self.last_idx())

    def extract_max(self):
        self.swap(0, self.last_idx())
        max = self.pop()
        if len(self) > 0:
            self.sift_down(self[0], 0)
        return max


def main():
    total = int(input())
    pq = PriorityQueue()
    for i in range(total):
        command = input()
        if command.startswith('Insert'):
            _, n = command.split()
            pq.append(int(n))
        elif command.startswith('ExtractMax'):
            print(pq.extract_max())


if __name__ == '__main__':
    main()
