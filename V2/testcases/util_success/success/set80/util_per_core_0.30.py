"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.192476, 'e_o_k': [0.023665, 0.018932, 0.015146], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.405057, 'e_o_k': [0.032938, 0.026350, 0.021080, 0.016864, 0.013491, 0.010793], 'p_i': 20, 'u_i': 3.1493},
        {'id': 2, 'e_m': 0.569053, 'e_o_k': [0.057831, 0.046265, 0.037012, 0.029609], 'p_i': 40, 'u_i': 4.3022},
        {'id': 3, 'e_m': 12.147454, 'e_o_k': [0.987791, 0.790232, 0.632186, 0.505749, 0.404599, 0.323679], 'p_i': 80, 'u_i': 4.8493},
        {'id': 4, 'e_m': 7.598391, 'e_o_k': [1.266399, 1.013119], 'p_i': 40, 'u_i': 1.1754},
        {'id': 5, 'e_m': 4.563707, 'e_o_k': [0.371106, 0.296884, 0.237508, 0.190006, 0.152005, 0.121604], 'p_i': 40, 'u_i': 3.0798},
        {'id': 6, 'e_m': 0.618929, 'e_o_k': [0.076098, 0.060878, 0.048703], 'p_i': 10, 'u_i': 3.4237},
        {'id': 7, 'e_m': 0.569693, 'e_o_k': [0.046326, 0.037060, 0.029648, 0.023719, 0.018975, 0.015180], 'p_i': 20, 'u_i': 3.1726},
    ]
    B_BUDGET = 71.760000
    return processors, tasks, B_BUDGET
