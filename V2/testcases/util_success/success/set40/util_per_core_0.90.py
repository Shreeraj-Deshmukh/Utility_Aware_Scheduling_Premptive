"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28001, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28001, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.810706, 'e_o_k': [0.345579, 0.276463, 0.221170], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 2.749023, 'e_o_k': [0.458170, 0.366536], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 13.897416, 'e_o_k': [1.412339, 1.129871, 0.903897, 0.723118], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 18.210683, 'e_o_k': [3.035114, 2.428091], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 1.669688, 'e_o_k': [0.149008, 0.119207, 0.095365, 0.076292, 0.061034], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 14.619246, 'e_o_k': [1.188789, 0.951031, 0.760825, 0.608660, 0.486928, 0.389542], 'p_i': 40, 'u_i': 3.0218},
        {'id': 6, 'e_m': 1.701336, 'e_o_k': [0.151833, 0.121466, 0.097173, 0.077738, 0.062191], 'p_i': 20, 'u_i': 2.6468},
        {'id': 7, 'e_m': 25.129539, 'e_o_k': [2.043451, 1.634761, 1.307808, 1.046247, 0.836997, 0.669598], 'p_i': 80, 'u_i': 1.1768},
    ]
    B_BUDGET = 215.280010
    return processors, tasks, B_BUDGET
