"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.425961, 'e_o_k': [0.161643, 0.129314, 0.103451, 0.082761, 0.066209, 0.052967], 'p_i': 10, 'u_i': 3.7793},
        {'id': 1, 'e_m': 0.436083, 'e_o_k': [0.206815, 0.165452, 0.132361, 0.105889], 'p_i': 20, 'u_i': 1.9533},
        {'id': 2, 'e_m': 7.001336, 'e_o_k': [3.320417, 2.656334, 2.125067, 1.700054], 'p_i': 40, 'u_i': 2.6246},
        {'id': 3, 'e_m': 21.840159, 'e_o_k': [8.287856, 6.630285, 5.304228, 4.243382, 3.394706, 2.715765], 'p_i': 80, 'u_i': 2.3478},
        {'id': 4, 'e_m': 21.347346, 'e_o_k': [12.248477, 9.798782, 7.839025], 'p_i': 80, 'u_i': 2.5491},
        {'id': 5, 'e_m': 0.207225, 'e_o_k': [0.086303, 0.069042, 0.055234, 0.044187, 0.035350], 'p_i': 10, 'u_i': 2.9783},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
