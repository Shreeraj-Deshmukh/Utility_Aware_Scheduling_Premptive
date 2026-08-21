"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.599170, 'e_o_k': [0.099862, 0.099862, 0.099862], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 4.185659, 'e_o_k': [1.046415, 1.046415], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.147250, 'e_o_k': [0.018406, 0.018406, 0.018406, 0.018406], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 1.074448, 'e_o_k': [0.268612, 0.268612], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.209273, 'e_o_k': [0.052318, 0.052318], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.141966, 'e_o_k': [0.023661, 0.023661, 0.023661], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.313697, 'e_o_k': [0.026141, 0.026141, 0.026141, 0.026141, 0.026141, 0.026141], 'p_i': 80, 'u_i': 1.9604},
        {'id': 7, 'e_m': 1.741302, 'e_o_k': [0.217663, 0.217663, 0.217663, 0.217663], 'p_i': 20, 'u_i': 2.4961},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
