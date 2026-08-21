"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.771604, 'e_o_k': [0.321348, 0.257079, 0.205663, 0.164530, 0.131624], 'p_i': 10, 'u_i': 4.5167},
        {'id': 1, 'e_m': 2.288231, 'e_o_k': [1.779735, 1.423788], 'p_i': 20, 'u_i': 2.0571},
        {'id': 2, 'e_m': 8.920614, 'e_o_k': [3.715154, 2.972123, 2.377698, 1.902159, 1.521727], 'p_i': 40, 'u_i': 3.7403},
        {'id': 3, 'e_m': 19.185389, 'e_o_k': [7.280430, 5.824344, 4.659475, 3.727580, 2.982064, 2.385651], 'p_i': 80, 'u_i': 1.1622},
        {'id': 4, 'e_m': 0.020623, 'e_o_k': [0.011833, 0.009466, 0.007573], 'p_i': 40, 'u_i': 4.1752},
        {'id': 5, 'e_m': 1.450798, 'e_o_k': [0.688048, 0.550438, 0.440351, 0.352280], 'p_i': 10, 'u_i': 1.9420},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET
