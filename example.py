from dfa import DFA


m = DFA()
m.load_from_yaml("automata/example.yaml")

#accepted! =)
m.accepts("b")
m.accepts("ab")
m.accepts("aab")

#rejected, =(
m.accepts("ba")
m.accepts("aba")
m.accepts("bbba")
