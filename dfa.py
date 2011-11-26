import yaml


class DFA:
    def load(self,
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

    def load_from_yaml(self, filename):
        o = yaml.load(open(filename, 'r+'))
        self.load(states=o['states'],
                  alphabet=o['alphabet'],                 
                  delta=o['delta'],
                  initial=o['initial'],
                  terminals=o['terminals'])

    def accepts(self, string):
        return reduce(lambda st, sy: self.D[(st, sy)], string, self.q0) in self.F


