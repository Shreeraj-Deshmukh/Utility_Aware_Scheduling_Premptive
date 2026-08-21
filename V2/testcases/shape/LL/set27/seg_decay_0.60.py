"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199988, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199988, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.707837, 'e_o_k': [0.392426, 0.235455, 0.141273, 0.084764], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.074416, 'e_o_k': [0.016138, 0.009683, 0.005810, 0.003486, 0.002091], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 1.043073, 'e_o_k': [0.226204, 0.135722, 0.081433, 0.048860, 0.029316], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 0.422237, 'e_o_k': [0.131949, 0.079169], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 0.946737, 'e_o_k': [0.295855, 0.177513], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 0.544998, 'e_o_k': [0.170312, 0.102187], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 1.274474, 'e_o_k': [0.292848, 0.175709, 0.105425, 0.063255], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.014372, 'e_o_k': [0.003302, 0.001981, 0.001189, 0.000713], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 55.199988
    return processors, tasks, B_BUDGET
