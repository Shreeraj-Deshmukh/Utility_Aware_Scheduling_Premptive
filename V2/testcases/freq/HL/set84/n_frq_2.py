"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "freq", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "freq", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 1.0]},
        {'id': 1, 'frequencies': [0.4, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.484964, 'e_o_k': [0.072133, 0.057706, 0.046165, 0.036932, 0.029546], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.736640, 'e_o_k': [0.150951, 0.120761, 0.096609], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 4.567615, 'e_o_k': [0.773648, 0.618918, 0.495134, 0.396108], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 2.590483, 'e_o_k': [0.719579, 0.575663], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 1.196360, 'e_o_k': [0.202636, 0.162108, 0.129687, 0.103749], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 5.644234, 'e_o_k': [0.764951, 0.611960, 0.489568, 0.391655, 0.313324, 0.250659], 'p_i': 40, 'u_i': 3.8755},
        {'id': 6, 'e_m': 25.995886, 'e_o_k': [5.327026, 4.261621, 3.409297], 'p_i': 80, 'u_i': 3.4836},
        {'id': 7, 'e_m': 3.483648, 'e_o_k': [0.713862, 0.571090, 0.456872], 'p_i': 40, 'u_i': 4.1699},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
