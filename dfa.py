import yaml


class DFA:
    def load(self, m):
        self.Q = m['states']
        self.S = m['alphabet']
        self.D = m['delta']
        self.q0 = m['initial']
        self.F = m['terminals']

    def load_from_yaml(self, filename):
        try:
            self.load(yaml.load(open(filename, 'r+')))
        except Exception, e:
            print e

    def accepts(self, string):
        return reduce(lambda st, sy: self.D[(st, sy)], string, self.q0) in self.F


