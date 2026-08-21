"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.151116, 'e_o_k': [0.013486, 0.010789, 0.008631, 0.006905, 0.005524], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.081372, 'e_o_k': [0.087934, 0.070347, 0.056278, 0.045022, 0.036018, 0.028814], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 6.496418, 'e_o_k': [1.082736, 0.866189], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 6.676629, 'e_o_k': [1.112772, 0.890217], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 4.495219, 'e_o_k': [0.749203, 0.599363], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 3.256810, 'e_o_k': [0.264833, 0.211866, 0.169493, 0.135594, 0.108476, 0.086780], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 0.976015, 'e_o_k': [0.162669, 0.130135], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 2.740749, 'e_o_k': [0.336977, 0.269582, 0.215665], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 71.759999
    return processors, tasks, B_BUDGET
