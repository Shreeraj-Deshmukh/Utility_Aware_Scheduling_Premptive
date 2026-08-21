"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.333816, 'e_o_k': [0.214772, 0.128863, 0.077318, 0.046391], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 0.511403, 'e_o_k': [0.329027, 0.197416, 0.118450, 0.071070], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 2.476328, 'e_o_k': [2.166787, 1.300072], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 3.763800, 'e_o_k': [2.688429, 1.613057, 0.967834], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.262962, 'e_o_k': [0.187830, 0.112698, 0.067619], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 7.850730, 'e_o_k': [6.869388, 4.121633], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 3.101814, 'e_o_k': [2.714088, 1.628453], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 3.987120, 'e_o_k': [3.488730, 2.093238], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
