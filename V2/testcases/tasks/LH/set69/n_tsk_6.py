"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.040333, 'e_o_k': [0.015306, 0.012244, 0.009796, 0.007836, 0.006269, 0.005015], 'p_i': 10, 'u_i': 1.7448},
        {'id': 1, 'e_m': 0.627139, 'e_o_k': [0.261184, 0.208947, 0.167158, 0.133726, 0.106981], 'p_i': 20, 'u_i': 2.9486},
        {'id': 2, 'e_m': 0.595631, 'e_o_k': [0.248062, 0.198449, 0.158759, 0.127008, 0.101606], 'p_i': 40, 'u_i': 1.5908},
        {'id': 3, 'e_m': 6.445710, 'e_o_k': [2.684434, 2.147548, 1.718038, 1.374430, 1.099544], 'p_i': 80, 'u_i': 1.2188},
        {'id': 4, 'e_m': 1.367973, 'e_o_k': [0.784903, 0.627922, 0.502338], 'p_i': 10, 'u_i': 2.5958},
        {'id': 5, 'e_m': 1.323503, 'e_o_k': [0.759387, 0.607509, 0.486007], 'p_i': 10, 'u_i': 3.0557},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
