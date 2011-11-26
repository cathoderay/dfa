import unittest

import dfa


class DFATest(unittest.TestCase):
    def setup(self):
        states = ["q0", "q1", "q2"]
        alphabet = ["a", "b"]
        delta = {("q0", "a") : "q0",
                 ("q0", "b") : "q1",
                 ("q1", "a") : "q2",
                 ("q1", "b") : "q2",
                 ("q2", "a") : "q2",
                 ("q2", "b") : "q2"}
        initial = "q0"
        terminals = ["q1"]

        self.my_dfa(states,
                    alphabet,
                    delta,
                    initial,
                    terminals)

    def test_accepts_simple_language(self):
        self.my_dfa.accepts("aba")



if __name__ == "__main__":
    unittest.main
