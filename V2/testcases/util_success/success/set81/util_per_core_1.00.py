"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200009, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200009, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.772791, 'e_o_k': [0.628799, 0.503039], 'p_i': 10, 'u_i': 4.8512},
        {'id': 1, 'e_m': 1.500645, 'e_o_k': [0.250107, 0.200086], 'p_i': 20, 'u_i': 2.1049},
        {'id': 2, 'e_m': 13.080097, 'e_o_k': [1.329278, 1.063423, 0.850738, 0.680590], 'p_i': 40, 'u_i': 2.1681},
        {'id': 3, 'e_m': 21.090742, 'e_o_k': [2.143368, 1.714694, 1.371756, 1.097404], 'p_i': 80, 'u_i': 3.4225},
        {'id': 4, 'e_m': 0.795997, 'e_o_k': [0.064728, 0.051782, 0.041426, 0.033141, 0.026513, 0.021210], 'p_i': 40, 'u_i': 4.5153},
        {'id': 5, 'e_m': 4.796561, 'e_o_k': [0.589741, 0.471793, 0.377434], 'p_i': 10, 'u_i': 3.2535},
        {'id': 6, 'e_m': 7.861728, 'e_o_k': [0.798956, 0.639165, 0.511332, 0.409066], 'p_i': 40, 'u_i': 2.8656},
        {'id': 7, 'e_m': 2.609528, 'e_o_k': [0.265196, 0.212157, 0.169725, 0.135780], 'p_i': 10, 'u_i': 3.1003},
    ]
    B_BUDGET = 239.200009
    return processors, tasks, B_BUDGET
