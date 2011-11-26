class DFA:
    def __init__(self,
                 states,
                 alphabet,
                 delta,
                 initial,
                 terminals):
        self.Q = states
        self.S= alphabet
        self.D = delta
        self.q0 = initial
        self.F = terminals

    def accepts(self, string):
        c = self.q0
        for symbol in string:
            c = self.D[(c, symbol)]
        return c in self.F
