"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200021, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200021, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.868614, 'e_o_k': [0.177995, 0.142396, 0.113917], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 0.707032, 'e_o_k': [0.144884, 0.115907, 0.092726], 'p_i': 20, 'u_i': 3.6949},
        {'id': 2, 'e_m': 4.447481, 'e_o_k': [0.911369, 0.729095, 0.583276], 'p_i': 40, 'u_i': 3.0423},
        {'id': 3, 'e_m': 1.996160, 'e_o_k': [0.409049, 0.327239, 0.261792], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.078011, 'e_o_k': [0.015986, 0.012789, 0.010231], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.176089, 'e_o_k': [0.036084, 0.028867, 0.023094], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 2.563544, 'e_o_k': [0.525316, 0.420253, 0.336203], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 0.648544, 'e_o_k': [0.132898, 0.106319, 0.085055], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 55.200021
    return processors, tasks, B_BUDGET
