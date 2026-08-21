"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680001, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680001, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.689807, 'e_o_k': [0.150804, 0.120643, 0.096514, 0.077212, 0.061769], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.355169, 'e_o_k': [0.059195, 0.047356], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 2.867086, 'e_o_k': [0.291371, 0.233096, 0.186477, 0.149182], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 3.497724, 'e_o_k': [0.582954, 0.466363], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 13.830064, 'e_o_k': [1.124615, 0.899692, 0.719754, 0.575803, 0.460642, 0.368514], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 3.101531, 'e_o_k': [0.315196, 0.252157, 0.201726, 0.161380], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.222281, 'e_o_k': [0.037047, 0.029637], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 2.953634, 'e_o_k': [0.240180, 0.192144, 0.153715, 0.122972, 0.098378, 0.078702], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 95.680001
    return processors, tasks, B_BUDGET
