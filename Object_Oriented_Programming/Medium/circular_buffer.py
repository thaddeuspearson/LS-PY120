"""
Your task is to write a CircularBuffer class in Python that implements a
circular buffer for arbitrary objects. The class should be initialized with
the buffer size and provide the following methods:

    put: Add an object to the buffer
    get: Remove (and return) the oldest object in the buffer. Return None if
         the buffer is empty.

You may assume that none of the values stored in the buffer are None
(however, None may be used to designate empty spots in the buffer).

Put:
    - make a next idx and handle the mod
    - check the elem at the curr idx
        - if the elem at the curr idx is not None
            - increment oldest idx to the next idx
        - put the new elem at curr idx
        - increment curr to next idx
Get:
    - get the curr_value at the oldest_idx
    - set the value at the oldest index to None
    - if the curr_value is not None
        - increment oldest_idx
    - return the curr_val
"""


class CircularBuffer:
    def __init__(self, size):
        self.BUF_SIZE = size
        self.buffer = self._initialize_buffer(size)
        self.curr_idx = 0
        self.oldest_idx = 0

    def put(self, val: int | None):
        if self.buffer[self.curr_idx] is not None:
            self.oldest_idx = self._increment(self.curr_idx)

        self.buffer[self.curr_idx] = val
        self.curr_idx = self._increment(self.curr_idx)

    def get(self) -> int | None:
        curr_val = self.buffer[self.oldest_idx]
        self.buffer[self.oldest_idx] = None
        if curr_val is not None:
            self.oldest_idx = self._increment(self.oldest_idx)
        return curr_val

    def _initialize_buffer(size: int) -> list:
        return [None] * size

    def _increment(self, idx: int) -> int:
        return (idx + 1) % self.BUF_SIZE


def main():
    buffer = CircularBuffer(3)

    assert buffer.get() is None

    buffer.put(1)
    buffer.put(2)
    assert buffer.get() == 1

    buffer.put(3)
    buffer.put(4)
    assert buffer.get() == 2

    buffer.put(5)
    buffer.put(6)
    buffer.put(7)
    assert buffer.get() == 5
    assert buffer.get() == 6
    assert buffer.get() == 7
    assert buffer.get() is None

    buffer2 = CircularBuffer(4)

    assert buffer2.get() is None

    buffer2.put(1)
    buffer2.put(2)
    assert buffer2.get() == 1

    buffer2.put(3)
    buffer2.put(4)
    assert buffer2.get() == 2

    buffer2.put(5)
    buffer2.put(6)
    buffer2.put(7)
    assert buffer2.get() == 4
    assert buffer2.get() == 5
    assert buffer2.get() == 6
    assert buffer2.get() == 7
    assert buffer2.get() is None


if __name__ == "__main__":
    main()
