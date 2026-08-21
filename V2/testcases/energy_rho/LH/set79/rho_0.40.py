"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 57.408004, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.4, "seed": 1079, "set": 79, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.40"}
"""

_SPEC = '{"B": 57.408004, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.4, "seed": 1079, "set": 79, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.340082, 'e_o_k': [0.141633, 0.113307, 0.090645, 0.072516, 0.058013], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 0.844927, 'e_o_k': [0.320631, 0.256505, 0.205204, 0.164163, 0.131330, 0.105064], 'p_i': 20, 'u_i': 1.5555},
        {'id': 2, 'e_m': 0.259808, 'e_o_k': [0.149070, 0.119256, 0.095405], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 9.047231, 'e_o_k': [7.036735, 5.629388], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 2.504897, 'e_o_k': [1.948253, 1.558603], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 0.977966, 'e_o_k': [0.463805, 0.371044, 0.296835, 0.237468], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 5.375256, 'e_o_k': [4.180755, 3.344604], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 2.099419, 'e_o_k': [0.995659, 0.796527, 0.637222, 0.509778], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 57.408004
    return processors, tasks, B_BUDGET
