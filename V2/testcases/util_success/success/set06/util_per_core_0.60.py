"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.51999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.51999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.685551, 'e_o_k': [0.280925, 0.224740], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 4.497634, 'e_o_k': [0.457077, 0.365661, 0.292529, 0.234023], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 18.855579, 'e_o_k': [1.916217, 1.532974, 1.226379, 0.981103], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.476237, 'e_o_k': [0.079373, 0.063498], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 4.137946, 'e_o_k': [0.420523, 0.336418, 0.269135, 0.215308], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 4.396364, 'e_o_k': [0.732727, 0.586182], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.047053, 'e_o_k': [0.004199, 0.003359, 0.002687, 0.002150, 0.001720], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.099892, 'e_o_k': [0.008915, 0.007132, 0.005705, 0.004564, 0.003651], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 143.519990
    return processors, tasks, B_BUDGET
