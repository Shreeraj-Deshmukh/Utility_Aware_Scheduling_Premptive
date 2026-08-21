"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.561755, 'e_o_k': [0.260341, 0.208273, 0.166618, 0.133295], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.111624, 'e_o_k': [0.009962, 0.007969, 0.006375, 0.005100, 0.004080], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 1.564609, 'e_o_k': [0.139631, 0.111705, 0.089364, 0.071491, 0.057193], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 0.633356, 'e_o_k': [0.105559, 0.084447], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 1.420106, 'e_o_k': [0.236684, 0.189347], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 0.817497, 'e_o_k': [0.136250, 0.109000], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 1.911711, 'e_o_k': [0.194280, 0.155424, 0.124339, 0.099471], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.021558, 'e_o_k': [0.002191, 0.001753, 0.001402, 0.001122], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 71.760010
    return processors, tasks, B_BUDGET
