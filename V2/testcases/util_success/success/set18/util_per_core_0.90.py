"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280011, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280011, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.835535, 'e_o_k': [0.639256, 0.511405], 'p_i': 10, 'u_i': 3.3304},
        {'id': 1, 'e_m': 2.871055, 'e_o_k': [0.256222, 0.204978, 0.163982, 0.131186, 0.104949], 'p_i': 20, 'u_i': 4.8515},
        {'id': 2, 'e_m': 2.914447, 'e_o_k': [0.236993, 0.189595, 0.151676, 0.121340, 0.097072, 0.077658], 'p_i': 40, 'u_i': 3.3809},
        {'id': 3, 'e_m': 30.520283, 'e_o_k': [3.101655, 2.481324, 1.985059, 1.588047], 'p_i': 80, 'u_i': 4.9290},
        {'id': 4, 'e_m': 5.935054, 'e_o_k': [0.989176, 0.791341], 'p_i': 80, 'u_i': 1.8035},
        {'id': 5, 'e_m': 9.876464, 'e_o_k': [1.003706, 0.802965, 0.642372, 0.513897], 'p_i': 20, 'u_i': 3.4846},
        {'id': 6, 'e_m': 1.445405, 'e_o_k': [0.146891, 0.117513, 0.094010, 0.075208], 'p_i': 20, 'u_i': 2.9402},
        {'id': 7, 'e_m': 14.259791, 'e_o_k': [1.449166, 1.159333, 0.927466, 0.741973], 'p_i': 80, 'u_i': 1.0599},
    ]
    B_BUDGET = 215.280011
    return processors, tasks, B_BUDGET
