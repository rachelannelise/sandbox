from playground.xor_xnor import xor_gate, xnor_gate


def test_xor_gate():
    fixtures = [(1, 1), (0, 1), (1, 0), (0, 0)]
    answers = [False, True, True, False]

    for i in range(len(fixtures)):
        xor_result = xor_gate(fixtures[i])
        assert xor_result == answers[i]


def test_xnor_gate():
    fixtures = [(1, 1), (0, 1), (1, 0), (0, 0)]
    answers = [True, False, False, True]

    for i in range(len(fixtures)):
        xor_result = xnor_gate(fixtures[i])
        assert xor_result == answers[i]
