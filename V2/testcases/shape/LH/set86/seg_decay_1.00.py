"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.050222, 'e_o_k': [0.023437, 0.023437, 0.023437], 'p_i': 10, 'u_i': 2.4144},
        {'id': 1, 'e_m': 0.206926, 'e_o_k': [0.144848, 0.144848], 'p_i': 20, 'u_i': 2.6559},
        {'id': 2, 'e_m': 1.190379, 'e_o_k': [0.333306, 0.333306, 0.333306, 0.333306, 0.333306], 'p_i': 40, 'u_i': 2.8681},
        {'id': 3, 'e_m': 6.971948, 'e_o_k': [4.880363, 4.880363], 'p_i': 80, 'u_i': 1.8896},
        {'id': 4, 'e_m': 0.550862, 'e_o_k': [0.154241, 0.154241, 0.154241, 0.154241, 0.154241], 'p_i': 20, 'u_i': 1.6645},
        {'id': 5, 'e_m': 0.291867, 'e_o_k': [0.081723, 0.081723, 0.081723, 0.081723, 0.081723], 'p_i': 40, 'u_i': 1.3774},
        {'id': 6, 'e_m': 1.611679, 'e_o_k': [1.128176, 1.128176], 'p_i': 80, 'u_i': 1.9412},
        {'id': 7, 'e_m': 17.018957, 'e_o_k': [11.913270, 11.913270], 'p_i': 80, 'u_i': 2.2237},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
