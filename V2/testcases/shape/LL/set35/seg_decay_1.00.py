"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199983, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.199983, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.153313, 'e_o_k': [0.019164, 0.019164, 0.019164, 0.019164], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.148369, 'e_o_k': [0.012364, 0.012364, 0.012364, 0.012364, 0.012364, 0.012364], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 2.270223, 'e_o_k': [0.378371, 0.378371, 0.378371], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 7.275677, 'e_o_k': [0.727568, 0.727568, 0.727568, 0.727568, 0.727568], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 2.680502, 'e_o_k': [0.670125, 0.670125], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 1.468106, 'e_o_k': [0.122342, 0.122342, 0.122342, 0.122342, 0.122342, 0.122342], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 0.569881, 'e_o_k': [0.094980, 0.094980, 0.094980], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.303269, 'e_o_k': [0.075817, 0.075817], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 55.199983
    return processors, tasks, B_BUDGET
