"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.150064, 'e_o_k': [0.179172, 0.179172, 0.179172, 0.179172, 0.179172, 0.179172], 'p_i': 10, 'u_i': 3.8590},
        {'id': 1, 'e_m': 0.276887, 'e_o_k': [0.027689, 0.027689, 0.027689, 0.027689, 0.027689], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 1.036903, 'e_o_k': [0.103690, 0.103690, 0.103690, 0.103690, 0.103690], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.261660, 'e_o_k': [0.065415, 0.065415], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 12.654356, 'e_o_k': [3.163589, 3.163589], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.168799, 'e_o_k': [0.042200, 0.042200], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 2.612506, 'e_o_k': [0.261251, 0.261251, 0.261251, 0.261251, 0.261251], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 3.342402, 'e_o_k': [0.557067, 0.557067, 0.557067], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
