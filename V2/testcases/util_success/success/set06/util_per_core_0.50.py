"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599992, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599992, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.404626, 'e_o_k': [0.234104, 0.187283], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 3.748028, 'e_o_k': [0.380897, 0.304718, 0.243774, 0.195019], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 15.712983, 'e_o_k': [1.596848, 1.277478, 1.021983, 0.817586], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.396864, 'e_o_k': [0.066144, 0.052915], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 3.448288, 'e_o_k': [0.350436, 0.280349, 0.224279, 0.179423], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 3.663636, 'e_o_k': [0.610606, 0.488485], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.039211, 'e_o_k': [0.003499, 0.002799, 0.002240, 0.001792, 0.001433], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.083243, 'e_o_k': [0.007429, 0.005943, 0.004754, 0.003804, 0.003043], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 119.599992
    return processors, tasks, B_BUDGET
