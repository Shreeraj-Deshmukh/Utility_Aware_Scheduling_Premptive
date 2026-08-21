"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.765093, 'e_o_k': [0.224848, 0.179879, 0.143903, 0.115122, 0.092098, 0.073678], 'p_i': 10, 'u_i': 4.6267},
        {'id': 1, 'e_m': 2.624560, 'e_o_k': [0.437427, 0.349941], 'p_i': 20, 'u_i': 4.4310},
        {'id': 2, 'e_m': 0.319377, 'e_o_k': [0.028502, 0.022802, 0.018241, 0.014593, 0.011675], 'p_i': 40, 'u_i': 4.5357},
        {'id': 3, 'e_m': 7.702766, 'e_o_k': [0.626363, 0.501091, 0.400873, 0.320698, 0.256558, 0.205247], 'p_i': 80, 'u_i': 2.3203},
        {'id': 4, 'e_m': 4.071569, 'e_o_k': [0.500603, 0.400482, 0.320386], 'p_i': 80, 'u_i': 3.8723},
        {'id': 5, 'e_m': 2.240875, 'e_o_k': [0.227731, 0.182185, 0.145748, 0.116598], 'p_i': 40, 'u_i': 1.1816},
        {'id': 6, 'e_m': 18.246764, 'e_o_k': [1.483766, 1.187013, 0.949610, 0.759688, 0.607751, 0.486201], 'p_i': 80, 'u_i': 4.5942},
        {'id': 7, 'e_m': 1.529927, 'e_o_k': [0.136536, 0.109228, 0.087383, 0.069906, 0.055925], 'p_i': 10, 'u_i': 3.3631},
    ]
    B_BUDGET = 119.600003
    return processors, tasks, B_BUDGET
