"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 28, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "freq", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 28, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "freq", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 1.0]},
        {'id': 1, 'frequencies': [0.4, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.181209, 'e_o_k': [0.448243, 0.358594, 0.286875, 0.229500, 0.183600, 0.146880], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 0.909186, 'e_o_k': [0.521664, 0.417331, 0.333865], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 1.009200, 'e_o_k': [0.579049, 0.463239, 0.370591], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 5.488802, 'e_o_k': [3.149313, 2.519450, 2.015560], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 2.719998, 'e_o_k': [1.132793, 0.906235, 0.724988, 0.579990, 0.463992], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.142051, 'e_o_k': [0.067368, 0.053895, 0.043116, 0.034493], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 0.727869, 'e_o_k': [0.566120, 0.452896], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 3.047121, 'e_o_k': [1.445112, 1.156089, 0.924872, 0.739897], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
