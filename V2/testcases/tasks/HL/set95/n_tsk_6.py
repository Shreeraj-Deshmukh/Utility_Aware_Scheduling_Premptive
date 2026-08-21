"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400011, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400011, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.125769, 'e_o_k': [0.360056, 0.288045, 0.230436, 0.184349], 'p_i': 10, 'u_i': 2.8802},
        {'id': 1, 'e_m': 3.760586, 'e_o_k': [0.636956, 0.509564, 0.407652, 0.326121], 'p_i': 20, 'u_i': 1.9313},
        {'id': 2, 'e_m': 8.060220, 'e_o_k': [2.238950, 1.791160], 'p_i': 40, 'u_i': 4.0147},
        {'id': 3, 'e_m': 3.458466, 'e_o_k': [0.468718, 0.374975, 0.299980, 0.239984, 0.191987, 0.153590], 'p_i': 80, 'u_i': 3.8759},
        {'id': 4, 'e_m': 5.300970, 'e_o_k': [1.086264, 0.869012, 0.695209], 'p_i': 80, 'u_i': 4.3076},
        {'id': 5, 'e_m': 7.071626, 'e_o_k': [0.958402, 0.766722, 0.613377, 0.490702, 0.392561, 0.314049], 'p_i': 80, 'u_i': 1.9116},
    ]
    B_BUDGET = 110.400011
    return processors, tasks, B_BUDGET
