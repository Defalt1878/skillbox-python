print('Задача 4. Последовательность Хофштадтера')


class HofstadterSequence:
    def __init__(self, initial_state: list[int]):
        self.s = initial_state[:]

    def __next__(self):
        try:
            new = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(new)
            return new
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


def hofstadter_sequence(initial_state: list[int]):
    state = initial_state[:]
    try:
        while True:
            q = state[-state[-1]] + state[-state[-2]]
            state.append(q)
            yield q
    except IndexError:
        pass


hs = HofstadterSequence([1, 1])
print([next(hs) for _ in range(20)])

hs_gen = hofstadter_sequence([1, 1])
print([next(hs_gen) for _ in range(20)])
