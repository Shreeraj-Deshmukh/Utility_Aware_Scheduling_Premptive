"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359987, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359987, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.237383, 'e_o_k': [0.275088, 0.220070, 0.176056], 'p_i': 10, 'u_i': 2.7501},
        {'id': 1, 'e_m': 5.529978, 'e_o_k': [0.493513, 0.394810, 0.315848, 0.252679, 0.202143], 'p_i': 20, 'u_i': 3.0723},
        {'id': 2, 'e_m': 16.909038, 'e_o_k': [1.374987, 1.099989, 0.879992, 0.703993, 0.563195, 0.450556], 'p_i': 40, 'u_i': 1.3696},
        {'id': 3, 'e_m': 18.401197, 'e_o_k': [2.262442, 1.809954, 1.447963], 'p_i': 80, 'u_i': 4.6022},
        {'id': 4, 'e_m': 17.031045, 'e_o_k': [1.730797, 1.384638, 1.107710, 0.886168], 'p_i': 80, 'u_i': 2.1344},
        {'id': 5, 'e_m': 3.504798, 'e_o_k': [0.584133, 0.467306], 'p_i': 20, 'u_i': 2.5225},
        {'id': 6, 'e_m': 1.765457, 'e_o_k': [0.217064, 0.173651, 0.138921], 'p_i': 40, 'u_i': 4.3404},
        {'id': 7, 'e_m': 1.180600, 'e_o_k': [0.119980, 0.095984, 0.076787, 0.061430], 'p_i': 80, 'u_i': 2.9431},
    ]
    B_BUDGET = 191.359987
    return processors, tasks, B_BUDGET
