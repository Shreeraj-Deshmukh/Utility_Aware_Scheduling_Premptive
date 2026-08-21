"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520009, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520009, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.873804, 'e_o_k': [0.230386, 0.184309, 0.147447], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 1.832682, 'e_o_k': [0.305447, 0.244358], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 9.264944, 'e_o_k': [0.941559, 0.753247, 0.602598, 0.482078], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 12.140455, 'e_o_k': [2.023409, 1.618727], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 1.113125, 'e_o_k': [0.099339, 0.079471, 0.063577, 0.050861, 0.040689], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 9.746164, 'e_o_k': [0.792526, 0.634021, 0.507216, 0.405773, 0.324619, 0.259695], 'p_i': 40, 'u_i': 3.0218},
        {'id': 6, 'e_m': 1.134224, 'e_o_k': [0.101222, 0.080977, 0.064782, 0.051826, 0.041460], 'p_i': 20, 'u_i': 2.6468},
        {'id': 7, 'e_m': 16.753026, 'e_o_k': [1.362300, 1.089840, 0.871872, 0.697498, 0.557998, 0.446399], 'p_i': 80, 'u_i': 1.1768},
    ]
    B_BUDGET = 143.520009
    return processors, tasks, B_BUDGET
