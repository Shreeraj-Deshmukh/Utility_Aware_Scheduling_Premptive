"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.878081, 'e_o_k': [0.179935, 0.143948, 0.115158], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 1.760389, 'e_o_k': [0.360735, 0.288588, 0.230871], 'p_i': 20, 'u_i': 2.6488},
        {'id': 2, 'e_m': 15.213605, 'e_o_k': [3.117542, 2.494034, 1.995227], 'p_i': 40, 'u_i': 4.8206},
        {'id': 3, 'e_m': 1.221415, 'e_o_k': [0.250290, 0.200232, 0.160186], 'p_i': 80, 'u_i': 3.3334},
        {'id': 4, 'e_m': 1.867670, 'e_o_k': [0.382719, 0.306175, 0.244940], 'p_i': 20, 'u_i': 2.1081},
        {'id': 5, 'e_m': 1.951144, 'e_o_k': [0.399825, 0.319860, 0.255888], 'p_i': 20, 'u_i': 1.8691},
        {'id': 6, 'e_m': 1.842208, 'e_o_k': [0.377502, 0.302001, 0.241601], 'p_i': 80, 'u_i': 3.0834},
        {'id': 7, 'e_m': 1.167704, 'e_o_k': [0.239284, 0.191427, 0.153142], 'p_i': 80, 'u_i': 3.6806},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
