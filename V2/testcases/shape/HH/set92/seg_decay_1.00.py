"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640011, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.640011, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.559072, 'e_o_k': [0.156540, 0.156540, 0.156540, 0.156540, 0.156540], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 1.614981, 'e_o_k': [0.376829, 0.376829, 0.376829, 0.376829, 0.376829, 0.376829], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 6.358045, 'e_o_k': [2.967088, 2.967088, 2.967088], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 15.550394, 'e_o_k': [5.442638, 5.442638, 5.442638, 5.442638], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.003664, 'e_o_k': [0.002565, 0.002565], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 3.875294, 'e_o_k': [1.808470, 1.808470, 1.808470], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 0.722639, 'e_o_k': [0.252924, 0.252924, 0.252924, 0.252924], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 7.557649, 'e_o_k': [2.645177, 2.645177, 2.645177, 2.645177], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 176.640011
    return processors, tasks, B_BUDGET
