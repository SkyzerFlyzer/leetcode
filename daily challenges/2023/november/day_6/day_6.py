import heapq


class SeatManager:

    def __init__(self, n: int):
        self.seat_heap = list(range(1, n + 1))
        heapq.heapify(self.seat_heap)

    def reserve(self) -> int:
        return heapq.heappop(self.seat_heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seat_heap, seatNumber)