"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360006, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360006, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.498405, 'e_o_k': [0.307181, 0.245745, 0.196596], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 2.443576, 'e_o_k': [0.407263, 0.325810], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 12.353259, 'e_o_k': [1.255412, 1.004330, 0.803464, 0.642771], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 16.187273, 'e_o_k': [2.697879, 2.158303], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 1.484167, 'e_o_k': [0.132452, 0.105961, 0.084769, 0.067815, 0.054252], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 12.994885, 'e_o_k': [1.056701, 0.845361, 0.676289, 0.541031, 0.432825, 0.346260], 'p_i': 40, 'u_i': 3.0218},
        {'id': 6, 'e_m': 1.512298, 'e_o_k': [0.134962, 0.107970, 0.086376, 0.069101, 0.055281], 'p_i': 20, 'u_i': 2.6468},
        {'id': 7, 'e_m': 22.337368, 'e_o_k': [1.816401, 1.453120, 1.162496, 0.929997, 0.743998, 0.595198], 'p_i': 80, 'u_i': 1.1768},
    ]
    B_BUDGET = 191.360006
    return processors, tasks, B_BUDGET
