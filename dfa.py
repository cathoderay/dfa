class DFA:
    def __init__(self,
                 states,
                 alphabet,
                 delta,
                 initial,
                 terminals):
        self.Q = states
        self.S = alphabet
        self.D = delta
        self.q0 = initial
        self.F = terminals

    def accepts(self, string):
        return reduce(lambda state, symbol: self.D[(state, symbol)], string, self.q0) in self.F
