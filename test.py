import unittest

from dfa import DFA


class DFATest(unittest.TestCase):
    def test_simple_language(self):
        m = {'states'    : ["q0", "q1", "q2"],
             'alphabet'  : ["a", "b"],
             'initial'   : "q0",
             'terminals' : ["q1"],
             'delta'     : {("q0", "a") : "q0",
                            ("q0", "b") : "q1",
                            ("q1", "a") : "q2",
                            ("q1", "b") : "q2",
                            ("q2", "a") : "q2",
                            ("q2", "b") : "q2"}}

        self.my_dfa = DFA()
        self.my_dfa.load(m)

        self.assertTrue(self.my_dfa.accepts("ab"))
        self.assertTrue(self.my_dfa.accepts("aaaab"))
        self.assertTrue(self.my_dfa.accepts("b"))

        self.assertFalse(self.my_dfa.accepts("aba"))
        self.assertFalse(self.my_dfa.accepts("aabbabaa"))

    def test_load_from_yaml(self):
        self.my_dfa = DFA()
        self.my_dfa.load_from_yaml("example.yaml")

        self.assertTrue(self.my_dfa.accepts("ab"))
        self.assertTrue(self.my_dfa.accepts("aaaab"))
        self.assertTrue(self.my_dfa.accepts("b"))

        self.assertFalse(self.my_dfa.accepts("aba"))
        self.assertFalse(self.my_dfa.accepts("aabbabaa"))


if __name__ == "__main__":
    unittest.main()
