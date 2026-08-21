"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600048, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600048, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.648128, 'e_o_k': [0.215337, 0.172270, 0.137816, 0.110253, 0.088202, 0.070562], 'p_i': 10, 'u_i': 2.4480},
        {'id': 1, 'e_m': 2.343127, 'e_o_k': [0.190535, 0.152428, 0.121943, 0.097554, 0.078043, 0.062435], 'p_i': 20, 'u_i': 3.0914},
        {'id': 2, 'e_m': 1.608287, 'e_o_k': [0.163444, 0.130755, 0.104604, 0.083683], 'p_i': 40, 'u_i': 2.6989},
        {'id': 3, 'e_m': 2.141177, 'e_o_k': [0.356863, 0.285490], 'p_i': 80, 'u_i': 4.1647},
        {'id': 4, 'e_m': 3.634587, 'e_o_k': [0.369369, 0.295495, 0.236396, 0.189117], 'p_i': 10, 'u_i': 1.2796},
        {'id': 5, 'e_m': 0.605081, 'e_o_k': [0.061492, 0.049194, 0.039355, 0.031484], 'p_i': 10, 'u_i': 2.4526},
        {'id': 6, 'e_m': 9.455628, 'e_o_k': [1.162577, 0.930062, 0.744049], 'p_i': 80, 'u_i': 3.7482},
        {'id': 7, 'e_m': 0.355879, 'e_o_k': [0.031760, 0.025408, 0.020326, 0.016261, 0.013009], 'p_i': 40, 'u_i': 2.1247},
    ]
    B_BUDGET = 119.600048
    return processors, tasks, B_BUDGET
