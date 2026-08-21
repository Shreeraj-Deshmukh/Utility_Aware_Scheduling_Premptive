"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20001, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}
"""

_SPEC = '{"B": 55.20001, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.547418, 'e_o_k': [0.092720, 0.074176, 0.059341, 0.047473], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 3.007680, 'e_o_k': [0.616328, 0.493062, 0.394450], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 0.682430, 'e_o_k': [0.092488, 0.073991, 0.059192, 0.047354, 0.037883, 0.030307], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 0.604649, 'e_o_k': [0.123903, 0.099123, 0.079298], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 1.249104, 'e_o_k': [0.211569, 0.169255, 0.135404, 0.108323], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.444853, 'e_o_k': [0.091158, 0.072927, 0.058341], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.188448, 'e_o_k': [0.052347, 0.041877], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 2.668510, 'e_o_k': [0.741253, 0.593002], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 55.200010
    return processors, tasks, B_BUDGET
