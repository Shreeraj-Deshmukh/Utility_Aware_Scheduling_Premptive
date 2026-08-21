"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127821, 'e_o_k': [0.026193, 0.020954, 0.016763], 'p_i': 10, 'u_i': 1.1226},
        {'id': 1, 'e_m': 2.917468, 'e_o_k': [0.597842, 0.478273, 0.382619], 'p_i': 20, 'u_i': 3.8598},
        {'id': 2, 'e_m': 0.515015, 'e_o_k': [0.105536, 0.084429, 0.067543], 'p_i': 40, 'u_i': 4.6365},
        {'id': 3, 'e_m': 0.662519, 'e_o_k': [0.135762, 0.108610, 0.086888], 'p_i': 80, 'u_i': 1.0760},
        {'id': 4, 'e_m': 9.683938, 'e_o_k': [1.984413, 1.587531, 1.270025], 'p_i': 80, 'u_i': 3.5452},
        {'id': 5, 'e_m': 0.198293, 'e_o_k': [0.040634, 0.032507, 0.026006], 'p_i': 40, 'u_i': 3.7479},
        {'id': 6, 'e_m': 1.613164, 'e_o_k': [0.330566, 0.264453, 0.211562], 'p_i': 80, 'u_i': 4.4508},
        {'id': 7, 'e_m': 1.480331, 'e_o_k': [0.303347, 0.242677, 0.194142], 'p_i': 20, 'u_i': 2.7382},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
