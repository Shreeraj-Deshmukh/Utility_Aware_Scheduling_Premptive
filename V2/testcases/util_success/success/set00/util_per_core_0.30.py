"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760007, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760007, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.212039, 'e_o_k': [0.018923, 0.015138, 0.012111, 0.009689, 0.007751], 'p_i': 10, 'u_i': 4.9222},
        {'id': 1, 'e_m': 0.747898, 'e_o_k': [0.076006, 0.060805, 0.048644, 0.038915], 'p_i': 20, 'u_i': 1.9107},
        {'id': 2, 'e_m': 8.015600, 'e_o_k': [0.715338, 0.572270, 0.457816, 0.366253, 0.293002], 'p_i': 40, 'u_i': 1.7322},
        {'id': 3, 'e_m': 6.253125, 'e_o_k': [0.558049, 0.446439, 0.357151, 0.285721, 0.228577], 'p_i': 80, 'u_i': 1.5709},
        {'id': 4, 'e_m': 1.175754, 'e_o_k': [0.104928, 0.083942, 0.067154, 0.053723, 0.042979], 'p_i': 20, 'u_i': 3.7661},
        {'id': 5, 'e_m': 1.096939, 'e_o_k': [0.134870, 0.107896, 0.086317], 'p_i': 20, 'u_i': 1.0932},
        {'id': 6, 'e_m': 0.064731, 'e_o_k': [0.005264, 0.004211, 0.003369, 0.002695, 0.002156, 0.001725], 'p_i': 20, 'u_i': 2.8740},
        {'id': 7, 'e_m': 5.839037, 'e_o_k': [0.717914, 0.574331, 0.459465], 'p_i': 40, 'u_i': 4.9324},
    ]
    B_BUDGET = 71.760007
    return processors, tasks, B_BUDGET
