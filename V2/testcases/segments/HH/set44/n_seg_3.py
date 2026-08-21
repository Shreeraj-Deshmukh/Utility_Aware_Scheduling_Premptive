"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.253914, 'e_o_k': [0.145689, 0.116551, 0.093241], 'p_i': 10, 'u_i': 1.1447},
        {'id': 1, 'e_m': 2.444497, 'e_o_k': [1.402580, 1.122064, 0.897651], 'p_i': 20, 'u_i': 4.1970},
        {'id': 2, 'e_m': 1.438401, 'e_o_k': [0.825312, 0.660250, 0.528200], 'p_i': 40, 'u_i': 2.1490},
        {'id': 3, 'e_m': 9.006906, 'e_o_k': [5.167897, 4.134317, 3.307454], 'p_i': 80, 'u_i': 1.5069},
        {'id': 4, 'e_m': 0.947423, 'e_o_k': [0.543603, 0.434883, 0.347906], 'p_i': 20, 'u_i': 3.9372},
        {'id': 5, 'e_m': 0.973099, 'e_o_k': [0.558336, 0.446669, 0.357335], 'p_i': 20, 'u_i': 1.6580},
        {'id': 6, 'e_m': 1.046300, 'e_o_k': [0.600336, 0.480269, 0.384215], 'p_i': 20, 'u_i': 4.1894},
        {'id': 7, 'e_m': 28.439701, 'e_o_k': [16.317862, 13.054289, 10.443431], 'p_i': 80, 'u_i': 4.9102},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
