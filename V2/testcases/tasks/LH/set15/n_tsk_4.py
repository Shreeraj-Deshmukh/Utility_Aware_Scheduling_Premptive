"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.120379, 'e_o_k': [0.883071, 0.706457, 0.565165, 0.452132, 0.361706], 'p_i': 10, 'u_i': 3.0940},
        {'id': 1, 'e_m': 1.696977, 'e_o_k': [0.706737, 0.565390, 0.452312, 0.361849, 0.289479], 'p_i': 20, 'u_i': 2.1175},
        {'id': 2, 'e_m': 0.270623, 'e_o_k': [0.102695, 0.082156, 0.065725, 0.052580, 0.042064, 0.033651], 'p_i': 40, 'u_i': 3.6512},
        {'id': 3, 'e_m': 7.707815, 'e_o_k': [3.655468, 2.924374, 2.339499, 1.871600], 'p_i': 80, 'u_i': 2.9125},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
