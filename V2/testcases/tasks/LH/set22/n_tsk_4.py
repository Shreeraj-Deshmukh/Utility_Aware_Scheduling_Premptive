"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.961172, 'e_o_k': [0.816766, 0.653413, 0.522730, 0.418184, 0.334547], 'p_i': 10, 'u_i': 3.1771},
        {'id': 1, 'e_m': 0.145065, 'e_o_k': [0.112829, 0.090263], 'p_i': 20, 'u_i': 3.8810},
        {'id': 2, 'e_m': 5.025013, 'e_o_k': [2.383136, 1.906509, 1.525207, 1.220166], 'p_i': 40, 'u_i': 1.9496},
        {'id': 3, 'e_m': 5.680334, 'e_o_k': [4.418038, 3.534430], 'p_i': 80, 'u_i': 4.0364},
    ]
    B_BUDGET = 88.319986
    return processors, tasks, B_BUDGET
