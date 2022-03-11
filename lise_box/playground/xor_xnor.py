

def xor_gate(gate_input: (int, int)) -> int:
    return gate_input[0] ^ gate_input[1]


def xnor_gate(gate_input: (int, int)) -> int:
    return not (gate_input[0] ^ gate_input[1])