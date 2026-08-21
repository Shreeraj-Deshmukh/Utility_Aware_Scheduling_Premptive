"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.123006, 'e_o_k': [0.383976, 0.307181, 0.245745], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 3.054470, 'e_o_k': [0.509078, 0.407263], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 15.441573, 'e_o_k': [1.569266, 1.255412, 1.004330, 0.803464], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 20.234092, 'e_o_k': [3.372349, 2.697879], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 1.855208, 'e_o_k': [0.165565, 0.132452, 0.105961, 0.084769, 0.067815], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 16.243607, 'e_o_k': [1.320876, 1.056701, 0.845361, 0.676289, 0.541031, 0.432825], 'p_i': 40, 'u_i': 3.0218},
        {'id': 6, 'e_m': 1.890373, 'e_o_k': [0.168703, 0.134962, 0.107970, 0.086376, 0.069101], 'p_i': 20, 'u_i': 2.6468},
        {'id': 7, 'e_m': 27.921710, 'e_o_k': [2.270501, 1.816401, 1.453120, 1.162496, 0.929997, 0.743998], 'p_i': 80, 'u_i': 1.1768},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET
