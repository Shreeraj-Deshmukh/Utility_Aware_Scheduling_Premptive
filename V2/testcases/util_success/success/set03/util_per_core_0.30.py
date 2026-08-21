"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76001, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76001, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.569795, 'e_o_k': [0.057906, 0.046325, 0.037060, 0.029648], 'p_i': 10, 'u_i': 3.3255},
        {'id': 1, 'e_m': 1.700426, 'e_o_k': [0.138273, 0.110618, 0.088495, 0.070796, 0.056637, 0.045309], 'p_i': 20, 'u_i': 3.8694},
        {'id': 2, 'e_m': 1.155135, 'e_o_k': [0.192523, 0.154018], 'p_i': 40, 'u_i': 3.5739},
        {'id': 3, 'e_m': 6.263781, 'e_o_k': [0.509350, 0.407480, 0.325984, 0.260787, 0.208630, 0.166904], 'p_i': 80, 'u_i': 3.1864},
        {'id': 4, 'e_m': 6.505341, 'e_o_k': [0.661112, 0.528890, 0.423112, 0.338489], 'p_i': 80, 'u_i': 1.9174},
        {'id': 5, 'e_m': 18.088981, 'e_o_k': [1.470936, 1.176749, 0.941399, 0.753119, 0.602495, 0.481996], 'p_i': 80, 'u_i': 3.2100},
        {'id': 6, 'e_m': 0.288616, 'e_o_k': [0.035486, 0.028389, 0.022711], 'p_i': 10, 'u_i': 2.5681},
        {'id': 7, 'e_m': 0.581314, 'e_o_k': [0.096886, 0.077509], 'p_i': 40, 'u_i': 3.1630},
    ]
    B_BUDGET = 71.760010
    return processors, tasks, B_BUDGET
