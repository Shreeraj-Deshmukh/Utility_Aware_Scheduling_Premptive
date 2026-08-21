"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 30, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 30, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127543, 'e_o_k': [0.053118, 0.042494, 0.033995, 0.027196, 0.021757], 'p_i': 10, 'u_i': 1.8069},
        {'id': 1, 'e_m': 0.883465, 'e_o_k': [0.506906, 0.405525, 0.324420], 'p_i': 20, 'u_i': 2.8086},
        {'id': 2, 'e_m': 2.358898, 'e_o_k': [0.982406, 0.785925, 0.628740, 0.502992, 0.402394], 'p_i': 40, 'u_i': 3.7043},
        {'id': 3, 'e_m': 1.038301, 'e_o_k': [0.492419, 0.393935, 0.315148, 0.252119], 'p_i': 80, 'u_i': 3.3496},
        {'id': 4, 'e_m': 0.490201, 'e_o_k': [0.186020, 0.148816, 0.119053, 0.095242, 0.076194, 0.060955], 'p_i': 40, 'u_i': 1.7648},
        {'id': 5, 'e_m': 14.146212, 'e_o_k': [11.002610, 8.802088], 'p_i': 80, 'u_i': 3.4093},
        {'id': 6, 'e_m': 0.399627, 'e_o_k': [0.310821, 0.248657], 'p_i': 10, 'u_i': 1.8072},
        {'id': 7, 'e_m': 0.841518, 'e_o_k': [0.399094, 0.319275, 0.255420, 0.204336], 'p_i': 20, 'u_i': 4.3991},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
