"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.068547, 'e_o_k': [0.019041, 0.015233], 'p_i': 10, 'u_i': 2.7951},
        {'id': 1, 'e_m': 3.049223, 'e_o_k': [0.624841, 0.499873, 0.399898], 'p_i': 20, 'u_i': 4.2173},
        {'id': 2, 'e_m': 4.038573, 'e_o_k': [1.121826, 0.897461], 'p_i': 40, 'u_i': 4.5788},
        {'id': 3, 'e_m': 8.227761, 'e_o_k': [1.686017, 1.348813, 1.079051], 'p_i': 80, 'u_i': 1.6533},
        {'id': 4, 'e_m': 28.357108, 'e_o_k': [4.803033, 3.842427, 3.073941, 2.459153], 'p_i': 80, 'u_i': 4.3793},
        {'id': 5, 'e_m': 6.592717, 'e_o_k': [1.116653, 0.893322, 0.714658, 0.571726], 'p_i': 80, 'u_i': 2.7000},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
