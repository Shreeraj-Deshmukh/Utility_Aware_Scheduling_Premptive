"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.625813, 'e_o_k': [0.241821, 0.193457, 0.154766, 0.123812, 0.099050], 'p_i': 10, 'u_i': 4.4263},
        {'id': 1, 'e_m': 9.707566, 'e_o_k': [1.989255, 1.591404, 1.273123], 'p_i': 20, 'u_i': 1.7162},
        {'id': 2, 'e_m': 0.282585, 'e_o_k': [0.078496, 0.062797], 'p_i': 40, 'u_i': 1.4626},
        {'id': 3, 'e_m': 2.321296, 'e_o_k': [0.644805, 0.515844], 'p_i': 80, 'u_i': 2.2690},
        {'id': 4, 'e_m': 0.529719, 'e_o_k': [0.108549, 0.086839, 0.069471], 'p_i': 10, 'u_i': 1.2408},
        {'id': 5, 'e_m': 5.039015, 'e_o_k': [1.399726, 1.119781], 'p_i': 80, 'u_i': 2.2030},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
