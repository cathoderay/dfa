import unittest

from dfa import DFA


class DFATest(unittest.TestCase):
    def test_simple_language(self):
        #Language = {a^nb : n >= 0}
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

        self.assertTrue(self.my_dfa._accepts("ab"))
        self.assertTrue(self.my_dfa._accepts("aaaab"))
        self.assertTrue(self.my_dfa._accepts("b"))

        self.assertFalse(self.my_dfa._accepts("aba"))
        self.assertFalse(self.my_dfa._accepts("aabbabaa"))
        self.assertFalse(self.my_dfa._accepts("aaaaa"))


    def test_load_from_yaml(self):
        self.my_dfa = DFA()
        self.my_dfa.load_from_yaml("example.yaml")

        self.assertTrue(self.my_dfa._accepts("ab"))
        self.assertTrue(self.my_dfa._accepts("aaaab"))
        self.assertTrue(self.my_dfa._accepts("b"))

        self.assertFalse(self.my_dfa._accepts("aba"))
        self.assertFalse(self.my_dfa._accepts("aabbabaa"))
        self.assertFalse(self.my_dfa._accepts("aaaaa"))


if __name__ == "__main__":
    unittest.main()
