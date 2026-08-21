"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.764237, 'e_o_k': [2.927740, 2.342192], 'p_i': 10, 'u_i': 3.1325},
        {'id': 1, 'e_m': 1.021954, 'e_o_k': [0.794853, 0.635882], 'p_i': 20, 'u_i': 4.7073},
        {'id': 2, 'e_m': 5.644478, 'e_o_k': [2.141954, 1.713564, 1.370851, 1.096681, 0.877345, 0.701876], 'p_i': 40, 'u_i': 3.8560},
        {'id': 3, 'e_m': 0.828627, 'e_o_k': [0.475442, 0.380353, 0.304283], 'p_i': 80, 'u_i': 2.5226},
        {'id': 4, 'e_m': 5.146392, 'e_o_k': [2.440701, 1.952561, 1.562049, 1.249639], 'p_i': 40, 'u_i': 1.7775},
        {'id': 5, 'e_m': 0.923490, 'e_o_k': [0.718270, 0.574616], 'p_i': 10, 'u_i': 2.7606},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
