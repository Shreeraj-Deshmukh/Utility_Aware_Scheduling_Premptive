"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519991, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519991, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.212028, 'e_o_k': [0.098558, 0.078846, 0.063077, 0.050462, 0.040369, 0.032296], 'p_i': 10, 'u_i': 2.7135},
        {'id': 1, 'e_m': 3.937027, 'e_o_k': [0.320146, 0.256117, 0.204893, 0.163915, 0.131132, 0.104905], 'p_i': 20, 'u_i': 1.9259},
        {'id': 2, 'e_m': 4.550882, 'e_o_k': [0.462488, 0.369990, 0.295992, 0.236794], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 30.211487, 'e_o_k': [2.696170, 2.156936, 1.725549, 1.380439, 1.104351], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 3.248540, 'e_o_k': [0.399411, 0.319529, 0.255623], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.204141, 'e_o_k': [0.020746, 0.016597, 0.013277, 0.010622], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 5.813715, 'e_o_k': [0.590825, 0.472660, 0.378128, 0.302502], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.725533, 'e_o_k': [0.073733, 0.058986, 0.047189, 0.037751], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 143.519991
    return processors, tasks, B_BUDGET
