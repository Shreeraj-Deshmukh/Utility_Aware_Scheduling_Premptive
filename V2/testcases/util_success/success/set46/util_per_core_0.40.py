"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679992, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679992, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.837512, 'e_o_k': [0.102973, 0.082378, 0.065903], 'p_i': 10, 'u_i': 3.9687},
        {'id': 1, 'e_m': 0.500247, 'e_o_k': [0.040678, 0.032543, 0.026034, 0.020827, 0.016662, 0.013330], 'p_i': 20, 'u_i': 2.3030},
        {'id': 2, 'e_m': 10.611361, 'e_o_k': [1.304676, 1.043740, 0.834992], 'p_i': 40, 'u_i': 2.6501},
        {'id': 3, 'e_m': 7.607968, 'e_o_k': [0.678960, 0.543168, 0.434534, 0.347627, 0.278102], 'p_i': 80, 'u_i': 1.7748},
        {'id': 4, 'e_m': 2.826180, 'e_o_k': [0.347481, 0.277985, 0.222388], 'p_i': 20, 'u_i': 3.9815},
        {'id': 5, 'e_m': 0.129053, 'e_o_k': [0.010494, 0.008395, 0.006716, 0.005373, 0.004298, 0.003439], 'p_i': 10, 'u_i': 4.8257},
        {'id': 6, 'e_m': 1.188189, 'e_o_k': [0.106038, 0.084830, 0.067864, 0.054291, 0.043433], 'p_i': 40, 'u_i': 1.0600},
        {'id': 7, 'e_m': 5.877351, 'e_o_k': [0.524514, 0.419611, 0.335689, 0.268551, 0.214841], 'p_i': 40, 'u_i': 2.2764},
    ]
    B_BUDGET = 95.679992
    return processors, tasks, B_BUDGET
