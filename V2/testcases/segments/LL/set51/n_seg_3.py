"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.415588, 'e_o_k': [0.290080, 0.232064, 0.185651], 'p_i': 10, 'u_i': 2.5682},
        {'id': 1, 'e_m': 1.559525, 'e_o_k': [0.319575, 0.255660, 0.204528], 'p_i': 20, 'u_i': 2.9074},
        {'id': 2, 'e_m': 1.007726, 'e_o_k': [0.206501, 0.165201, 0.132161], 'p_i': 40, 'u_i': 4.2053},
        {'id': 3, 'e_m': 1.342241, 'e_o_k': [0.275049, 0.220040, 0.176032], 'p_i': 80, 'u_i': 2.1233},
        {'id': 4, 'e_m': 4.007853, 'e_o_k': [0.821281, 0.657025, 0.525620], 'p_i': 80, 'u_i': 2.8725},
        {'id': 5, 'e_m': 0.593098, 'e_o_k': [0.121536, 0.097229, 0.077783], 'p_i': 20, 'u_i': 1.8909},
        {'id': 6, 'e_m': 1.066826, 'e_o_k': [0.218612, 0.174890, 0.139912], 'p_i': 20, 'u_i': 4.9900},
        {'id': 7, 'e_m': 0.431948, 'e_o_k': [0.088514, 0.070811, 0.056649], 'p_i': 80, 'u_i': 1.9407},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
