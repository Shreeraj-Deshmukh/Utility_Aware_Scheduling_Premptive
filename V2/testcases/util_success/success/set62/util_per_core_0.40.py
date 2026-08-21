"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680024, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680024, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.118502, 'e_o_k': [0.172270, 0.137816, 0.110253, 0.088202, 0.070562, 0.056449], 'p_i': 10, 'u_i': 2.4480},
        {'id': 1, 'e_m': 1.874501, 'e_o_k': [0.152428, 0.121943, 0.097554, 0.078043, 0.062435, 0.049948], 'p_i': 20, 'u_i': 3.0914},
        {'id': 2, 'e_m': 1.286629, 'e_o_k': [0.130755, 0.104604, 0.083683, 0.066947], 'p_i': 40, 'u_i': 2.6989},
        {'id': 3, 'e_m': 1.712942, 'e_o_k': [0.285490, 0.228392], 'p_i': 80, 'u_i': 4.1647},
        {'id': 4, 'e_m': 2.907669, 'e_o_k': [0.295495, 0.236396, 0.189117, 0.151293], 'p_i': 10, 'u_i': 1.2796},
        {'id': 5, 'e_m': 0.484065, 'e_o_k': [0.049194, 0.039355, 0.031484, 0.025187], 'p_i': 10, 'u_i': 2.4526},
        {'id': 6, 'e_m': 7.564502, 'e_o_k': [0.930062, 0.744049, 0.595240], 'p_i': 80, 'u_i': 3.7482},
        {'id': 7, 'e_m': 0.284703, 'e_o_k': [0.025408, 0.020326, 0.016261, 0.013009, 0.010407], 'p_i': 40, 'u_i': 2.1247},
    ]
    B_BUDGET = 95.680024
    return processors, tasks, B_BUDGET
