"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599985, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599985, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.949659, 'e_o_k': [0.096510, 0.077208, 0.061766, 0.049413], 'p_i': 10, 'u_i': 3.3255},
        {'id': 1, 'e_m': 2.834043, 'e_o_k': [0.230455, 0.184364, 0.147491, 0.117993, 0.094394, 0.075515], 'p_i': 20, 'u_i': 3.8694},
        {'id': 2, 'e_m': 1.925225, 'e_o_k': [0.320871, 0.256697], 'p_i': 40, 'u_i': 3.5739},
        {'id': 3, 'e_m': 10.439635, 'e_o_k': [0.848916, 0.679133, 0.543307, 0.434645, 0.347716, 0.278173], 'p_i': 80, 'u_i': 3.1864},
        {'id': 4, 'e_m': 10.842236, 'e_o_k': [1.101853, 0.881483, 0.705186, 0.564149], 'p_i': 80, 'u_i': 1.9174},
        {'id': 5, 'e_m': 30.148302, 'e_o_k': [2.451560, 1.961248, 1.568998, 1.255199, 1.004159, 0.803327], 'p_i': 80, 'u_i': 3.2100},
        {'id': 6, 'e_m': 0.481027, 'e_o_k': [0.059143, 0.047314, 0.037851], 'p_i': 10, 'u_i': 2.5681},
        {'id': 7, 'e_m': 0.968857, 'e_o_k': [0.161476, 0.129181], 'p_i': 40, 'u_i': 3.1630},
    ]
    B_BUDGET = 119.599985
    return processors, tasks, B_BUDGET
