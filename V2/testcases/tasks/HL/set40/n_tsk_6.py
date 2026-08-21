"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400013, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400013, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.692444, 'e_o_k': [0.286661, 0.229328, 0.183463, 0.146770], 'p_i': 10, 'u_i': 3.4352},
        {'id': 1, 'e_m': 1.673009, 'e_o_k': [0.283369, 0.226695, 0.181356, 0.145085], 'p_i': 20, 'u_i': 3.4020},
        {'id': 2, 'e_m': 8.380439, 'e_o_k': [1.717303, 1.373842, 1.099074], 'p_i': 40, 'u_i': 3.4221},
        {'id': 3, 'e_m': 10.582022, 'e_o_k': [1.573956, 1.259165, 1.007332, 0.805866, 0.644692], 'p_i': 80, 'u_i': 3.9841},
        {'id': 4, 'e_m': 1.210474, 'e_o_k': [0.248048, 0.198438, 0.158751], 'p_i': 40, 'u_i': 2.4868},
        {'id': 5, 'e_m': 1.750571, 'e_o_k': [0.237251, 0.189801, 0.151841, 0.121473, 0.097178, 0.077742], 'p_i': 10, 'u_i': 2.1829},
    ]
    B_BUDGET = 110.400013
    return processors, tasks, B_BUDGET
