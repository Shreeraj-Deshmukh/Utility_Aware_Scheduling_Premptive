"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120006, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120006, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.303985, 'e_o_k': [0.132519, 0.106015, 0.084812, 0.067850], 'p_i': 10, 'u_i': 1.3669},
        {'id': 1, 'e_m': 1.112911, 'e_o_k': [0.185485, 0.148388], 'p_i': 20, 'u_i': 2.1946},
        {'id': 2, 'e_m': 16.397456, 'e_o_k': [1.666408, 1.333126, 1.066501, 0.853201], 'p_i': 40, 'u_i': 4.4370},
        {'id': 3, 'e_m': 20.477454, 'e_o_k': [2.517720, 2.014176, 1.611341], 'p_i': 80, 'u_i': 1.3292},
        {'id': 4, 'e_m': 14.601519, 'e_o_k': [1.187347, 0.949878, 0.759902, 0.607922, 0.486337, 0.389070], 'p_i': 40, 'u_i': 2.0008},
        {'id': 5, 'e_m': 9.621666, 'e_o_k': [1.182992, 0.946393, 0.757115], 'p_i': 20, 'u_i': 3.5253},
        {'id': 6, 'e_m': 4.077959, 'e_o_k': [0.331606, 0.265285, 0.212228, 0.169782, 0.135826, 0.108661], 'p_i': 20, 'u_i': 3.2983},
        {'id': 7, 'e_m': 23.842572, 'e_o_k': [2.931464, 2.345171, 1.876137], 'p_i': 80, 'u_i': 3.1773},
    ]
    B_BUDGET = 263.120006
    return processors, tasks, B_BUDGET
