"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.056396, 'e_o_k': [0.821642, 0.657313], 'p_i': 10, 'u_i': 3.4799},
        {'id': 1, 'e_m': 0.992646, 'e_o_k': [0.413406, 0.330725, 0.264580, 0.211664, 0.169331], 'p_i': 20, 'u_i': 2.9893},
        {'id': 2, 'e_m': 0.801879, 'e_o_k': [0.333957, 0.267166, 0.213733, 0.170986, 0.136789], 'p_i': 40, 'u_i': 3.6030},
        {'id': 3, 'e_m': 9.625935, 'e_o_k': [7.486839, 5.989471], 'p_i': 80, 'u_i': 4.7122},
        {'id': 4, 'e_m': 6.603643, 'e_o_k': [5.136167, 4.108933], 'p_i': 80, 'u_i': 2.7870},
        {'id': 5, 'e_m': 0.872453, 'e_o_k': [0.500588, 0.400470, 0.320376], 'p_i': 40, 'u_i': 1.7506},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
