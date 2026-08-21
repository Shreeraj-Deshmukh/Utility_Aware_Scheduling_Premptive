"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200018, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200018, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.358023, 'e_o_k': [0.029113, 0.023291, 0.018632, 0.014906, 0.011925, 0.009540], 'p_i': 10, 'u_i': 4.6948},
        {'id': 1, 'e_m': 6.725082, 'e_o_k': [0.546861, 0.437489, 0.349991, 0.279993, 0.223994, 0.179196], 'p_i': 20, 'u_i': 1.5554},
        {'id': 2, 'e_m': 7.224913, 'e_o_k': [1.204152, 0.963322], 'p_i': 40, 'u_i': 4.1277},
        {'id': 3, 'e_m': 12.726585, 'e_o_k': [1.135761, 0.908609, 0.726887, 0.581510, 0.465208], 'p_i': 80, 'u_i': 1.1747},
        {'id': 4, 'e_m': 13.264882, 'e_o_k': [1.630928, 1.304743, 1.043794], 'p_i': 40, 'u_i': 2.4278},
        {'id': 5, 'e_m': 1.627580, 'e_o_k': [0.200112, 0.160090, 0.128072], 'p_i': 10, 'u_i': 2.1744},
        {'id': 6, 'e_m': 4.444310, 'e_o_k': [0.396625, 0.317300, 0.253840, 0.203072, 0.162457], 'p_i': 10, 'u_i': 4.1867},
        {'id': 7, 'e_m': 6.988549, 'e_o_k': [0.623681, 0.498945, 0.399156, 0.319324, 0.255460], 'p_i': 20, 'u_i': 3.6278},
    ]
    B_BUDGET = 239.200018
    return processors, tasks, B_BUDGET
