"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.852501, 'e_o_k': [0.275539, 0.220431, 0.176345, 0.141076, 0.112861], 'p_i': 10, 'u_i': 2.6037},
        {'id': 1, 'e_m': 4.518293, 'e_o_k': [1.255081, 1.004065], 'p_i': 20, 'u_i': 2.6419},
        {'id': 2, 'e_m': 0.127131, 'e_o_k': [0.018909, 0.015127, 0.012102, 0.009682, 0.007745], 'p_i': 40, 'u_i': 1.5138},
        {'id': 3, 'e_m': 5.821494, 'e_o_k': [1.192929, 0.954343, 0.763475], 'p_i': 80, 'u_i': 4.9479},
        {'id': 4, 'e_m': 17.580744, 'e_o_k': [3.602612, 2.882089, 2.305671], 'p_i': 80, 'u_i': 2.1346},
        {'id': 5, 'e_m': 0.931290, 'e_o_k': [0.258692, 0.206953], 'p_i': 10, 'u_i': 1.3827},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET
