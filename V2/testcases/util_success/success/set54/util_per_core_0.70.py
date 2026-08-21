"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.400060, 'e_o_k': [0.066677, 0.053341], 'p_i': 10, 'u_i': 1.0785},
        {'id': 1, 'e_m': 2.167522, 'e_o_k': [0.193437, 0.154749, 0.123799, 0.099040, 0.079232], 'p_i': 20, 'u_i': 3.4086},
        {'id': 2, 'e_m': 11.025519, 'e_o_k': [1.355597, 1.084477, 0.867582], 'p_i': 40, 'u_i': 3.2935},
        {'id': 3, 'e_m': 10.323413, 'e_o_k': [1.049127, 0.839302, 0.671441, 0.537153], 'p_i': 80, 'u_i': 4.9988},
        {'id': 4, 'e_m': 0.437497, 'e_o_k': [0.039044, 0.031235, 0.024988, 0.019990, 0.015992], 'p_i': 40, 'u_i': 2.8879},
        {'id': 5, 'e_m': 37.025532, 'e_o_k': [3.762757, 3.010206, 2.408165, 1.926532], 'p_i': 80, 'u_i': 4.7528},
        {'id': 6, 'e_m': 9.037139, 'e_o_k': [0.806503, 0.645203, 0.516162, 0.412930, 0.330344], 'p_i': 80, 'u_i': 4.9914},
        {'id': 7, 'e_m': 10.408658, 'e_o_k': [0.928902, 0.743122, 0.594497, 0.475598, 0.380478], 'p_i': 40, 'u_i': 2.2427},
    ]
    B_BUDGET = 167.440001
    return processors, tasks, B_BUDGET
