"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.160726, 'e_o_k': [0.665990, 0.532792, 0.426234], 'p_i': 10, 'u_i': 2.0997},
        {'id': 1, 'e_m': 0.933941, 'e_o_k': [0.726398, 0.581119], 'p_i': 20, 'u_i': 1.8132},
        {'id': 2, 'e_m': 5.441884, 'e_o_k': [2.065074, 1.652059, 1.321648, 1.057318, 0.845854, 0.676684], 'p_i': 40, 'u_i': 1.3118},
        {'id': 3, 'e_m': 2.243130, 'e_o_k': [0.934193, 0.747354, 0.597883, 0.478307, 0.382645], 'p_i': 80, 'u_i': 1.6432},
        {'id': 4, 'e_m': 0.117552, 'e_o_k': [0.091430, 0.073144], 'p_i': 20, 'u_i': 3.2827},
        {'id': 5, 'e_m': 1.345331, 'e_o_k': [0.560288, 0.448230, 0.358584, 0.286867, 0.229494], 'p_i': 20, 'u_i': 1.0597},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
