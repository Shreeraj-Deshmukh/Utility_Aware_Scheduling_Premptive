"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 166.335991, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.9, "seed": 1084, "set": 84, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.90"}
"""

_SPEC = '{"B": 166.335991, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.9, "seed": 1084, "set": 84, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.484964, 'e_o_k': [0.201972, 0.161578, 0.129262, 0.103410, 0.082728], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.736640, 'e_o_k': [0.422662, 0.338130, 0.270504], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 4.567615, 'e_o_k': [2.166213, 1.732971, 1.386376, 1.109101], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 2.590483, 'e_o_k': [2.014820, 1.611856], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 1.196360, 'e_o_k': [0.567380, 0.453904, 0.363123, 0.290498], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 5.644234, 'e_o_k': [2.141862, 1.713489, 1.370792, 1.096633, 0.877307, 0.701845], 'p_i': 40, 'u_i': 3.8755},
        {'id': 6, 'e_m': 25.995886, 'e_o_k': [14.915672, 11.932538, 9.546030], 'p_i': 80, 'u_i': 3.4836},
        {'id': 7, 'e_m': 3.483648, 'e_o_k': [1.998814, 1.599052, 1.279241], 'p_i': 40, 'u_i': 4.1699},
    ]
    B_BUDGET = 166.335991
    return processors, tasks, B_BUDGET
