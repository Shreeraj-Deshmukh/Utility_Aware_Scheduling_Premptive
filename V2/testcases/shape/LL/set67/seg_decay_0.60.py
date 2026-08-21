"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.811128, 'e_o_k': [0.392767, 0.235660, 0.141396, 0.084838, 0.050903], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.050717, 'e_o_k': [0.011654, 0.006992, 0.004195, 0.002517], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 2.544213, 'e_o_k': [0.795067, 0.477040], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 1.179546, 'e_o_k': [0.368608, 0.221165], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 1.744117, 'e_o_k': [0.444928, 0.266957, 0.160174], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 0.579467, 'e_o_k': [0.181083, 0.108650], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 4.549467, 'e_o_k': [1.160578, 0.696347, 0.417808], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.342286, 'e_o_k': [0.087318, 0.052391, 0.031434], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
