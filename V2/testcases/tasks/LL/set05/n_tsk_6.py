"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199985, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199985, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.541647, 'e_o_k': [0.073408, 0.058727, 0.046981, 0.037585, 0.030068, 0.024054], 'p_i': 10, 'u_i': 3.6469},
        {'id': 1, 'e_m': 0.175727, 'e_o_k': [0.026137, 0.020910, 0.016728, 0.013382, 0.010706], 'p_i': 20, 'u_i': 1.4903},
        {'id': 2, 'e_m': 2.520518, 'e_o_k': [0.426917, 0.341534, 0.273227, 0.218582], 'p_i': 40, 'u_i': 2.4704},
        {'id': 3, 'e_m': 1.402618, 'e_o_k': [0.287422, 0.229937, 0.183950], 'p_i': 80, 'u_i': 4.2349},
        {'id': 4, 'e_m': 4.379465, 'e_o_k': [0.593539, 0.474831, 0.379865, 0.303892, 0.243114, 0.194491], 'p_i': 40, 'u_i': 4.1771},
        {'id': 5, 'e_m': 5.880664, 'e_o_k': [0.996047, 0.796838, 0.637470, 0.509976], 'p_i': 40, 'u_i': 4.0903},
    ]
    B_BUDGET = 55.199985
    return processors, tasks, B_BUDGET
