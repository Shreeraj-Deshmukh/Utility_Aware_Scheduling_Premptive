"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.878081, 'e_o_k': [0.627201, 0.376321, 0.225792], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 1.760389, 'e_o_k': [1.034063, 0.620438, 0.372263, 0.223358, 0.134015, 0.080409], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 15.213605, 'e_o_k': [13.311905, 7.987143], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 1.221415, 'e_o_k': [0.717467, 0.430480, 0.258288, 0.154973, 0.092984, 0.055790], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 1.867670, 'e_o_k': [1.334050, 0.800430, 0.480258], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 1.951144, 'e_o_k': [1.146114, 0.687668, 0.412601, 0.247561, 0.148536, 0.089122], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 1.842208, 'e_o_k': [1.315863, 0.789518, 0.473711], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 1.167704, 'e_o_k': [1.021741, 0.613045], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET
