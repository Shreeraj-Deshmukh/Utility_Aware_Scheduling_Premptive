"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600022, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600022, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.112258, 'e_o_k': [0.188505, 0.150804, 0.120643, 0.096514, 0.077212], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.443962, 'e_o_k': [0.073994, 0.059195], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 3.583858, 'e_o_k': [0.364213, 0.291371, 0.233096, 0.186477], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 4.372155, 'e_o_k': [0.728693, 0.582954], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 17.287580, 'e_o_k': [1.405769, 1.124615, 0.899692, 0.719754, 0.575803, 0.460642], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 3.876913, 'e_o_k': [0.393995, 0.315196, 0.252157, 0.201726], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.277852, 'e_o_k': [0.046309, 0.037047], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 3.692043, 'e_o_k': [0.300225, 0.240180, 0.192144, 0.153715, 0.122972, 0.098378], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 119.600022
    return processors, tasks, B_BUDGET
