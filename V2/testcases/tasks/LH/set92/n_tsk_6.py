"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.385802, 'e_o_k': [0.160674, 0.128539, 0.102832, 0.082265, 0.065812], 'p_i': 10, 'u_i': 4.5167},
        {'id': 1, 'e_m': 1.144116, 'e_o_k': [0.889868, 0.711894], 'p_i': 20, 'u_i': 2.0571},
        {'id': 2, 'e_m': 4.460307, 'e_o_k': [1.857577, 1.486061, 1.188849, 0.951079, 0.760863], 'p_i': 40, 'u_i': 3.7403},
        {'id': 3, 'e_m': 9.592694, 'e_o_k': [3.640215, 2.912172, 2.329738, 1.863790, 1.491032, 1.192826], 'p_i': 80, 'u_i': 1.1622},
        {'id': 4, 'e_m': 0.010312, 'e_o_k': [0.005917, 0.004733, 0.003787], 'p_i': 40, 'u_i': 4.1752},
        {'id': 5, 'e_m': 0.725399, 'e_o_k': [0.344024, 0.275219, 0.220175, 0.176140], 'p_i': 10, 'u_i': 1.9420},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
