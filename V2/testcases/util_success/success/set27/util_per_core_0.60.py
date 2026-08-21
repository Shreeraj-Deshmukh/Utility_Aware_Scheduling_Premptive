"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.51999, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.51999, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.927552, 'e_o_k': [0.075425, 0.060340, 0.048272, 0.038618, 0.030894, 0.024715], 'p_i': 10, 'u_i': 1.3112},
        {'id': 1, 'e_m': 1.932760, 'e_o_k': [0.157166, 0.125733, 0.100586, 0.080469, 0.064375, 0.051500], 'p_i': 20, 'u_i': 2.1246},
        {'id': 2, 'e_m': 1.834738, 'e_o_k': [0.149195, 0.119356, 0.095485, 0.076388, 0.061110, 0.048888], 'p_i': 40, 'u_i': 2.2214},
        {'id': 3, 'e_m': 7.604954, 'e_o_k': [0.678691, 0.542952, 0.434362, 0.347490, 0.277992], 'p_i': 80, 'u_i': 3.1164},
        {'id': 4, 'e_m': 2.492494, 'e_o_k': [0.222438, 0.177951, 0.142360, 0.113888, 0.091111], 'p_i': 10, 'u_i': 2.9383},
        {'id': 5, 'e_m': 23.619682, 'e_o_k': [2.107896, 1.686317, 1.349054, 1.079243, 0.863394], 'p_i': 80, 'u_i': 2.8468},
        {'id': 6, 'e_m': 1.688423, 'e_o_k': [0.281404, 0.225123], 'p_i': 10, 'u_i': 4.6487},
        {'id': 7, 'e_m': 1.563387, 'e_o_k': [0.260564, 0.208452], 'p_i': 10, 'u_i': 3.0837},
    ]
    B_BUDGET = 143.519990
    return processors, tasks, B_BUDGET
