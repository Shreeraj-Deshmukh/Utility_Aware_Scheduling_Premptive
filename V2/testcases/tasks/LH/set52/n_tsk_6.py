"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320012, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320012, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.050612, 'e_o_k': [0.021078, 0.016863, 0.013490, 0.010792, 0.008634], 'p_i': 10, 'u_i': 1.6984},
        {'id': 1, 'e_m': 0.842273, 'e_o_k': [0.399452, 0.319561, 0.255649, 0.204519], 'p_i': 20, 'u_i': 3.4597},
        {'id': 2, 'e_m': 7.106119, 'e_o_k': [3.370111, 2.696089, 2.156871, 1.725497], 'p_i': 40, 'u_i': 4.7133},
        {'id': 3, 'e_m': 9.044792, 'e_o_k': [3.432298, 2.745838, 2.196671, 1.757337, 1.405869, 1.124695], 'p_i': 80, 'u_i': 2.1441},
        {'id': 4, 'e_m': 1.353058, 'e_o_k': [0.563506, 0.450805, 0.360644, 0.288515, 0.230812], 'p_i': 40, 'u_i': 1.5180},
        {'id': 5, 'e_m': 0.282859, 'e_o_k': [0.134147, 0.107318, 0.085854, 0.068683], 'p_i': 10, 'u_i': 2.4726},
    ]
    B_BUDGET = 88.320012
    return processors, tasks, B_BUDGET
