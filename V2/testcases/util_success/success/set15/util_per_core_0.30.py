"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760008, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760008, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.659056, 'e_o_k': [0.134909, 0.107927, 0.086342, 0.069073, 0.055259, 0.044207], 'p_i': 10, 'u_i': 4.6267},
        {'id': 1, 'e_m': 1.574736, 'e_o_k': [0.262456, 0.209965], 'p_i': 20, 'u_i': 4.4310},
        {'id': 2, 'e_m': 0.191626, 'e_o_k': [0.017101, 0.013681, 0.010945, 0.008756, 0.007005], 'p_i': 40, 'u_i': 4.5357},
        {'id': 3, 'e_m': 4.621660, 'e_o_k': [0.375818, 0.300654, 0.240524, 0.192419, 0.153935, 0.123148], 'p_i': 80, 'u_i': 2.3203},
        {'id': 4, 'e_m': 2.442941, 'e_o_k': [0.300362, 0.240289, 0.192231], 'p_i': 80, 'u_i': 3.8723},
        {'id': 5, 'e_m': 1.344525, 'e_o_k': [0.136639, 0.109311, 0.087449, 0.069959], 'p_i': 40, 'u_i': 1.1816},
        {'id': 6, 'e_m': 10.948059, 'e_o_k': [0.890260, 0.712208, 0.569766, 0.455813, 0.364650, 0.291720], 'p_i': 80, 'u_i': 4.5942},
        {'id': 7, 'e_m': 0.917956, 'e_o_k': [0.081921, 0.065537, 0.052430, 0.041944, 0.033555], 'p_i': 10, 'u_i': 3.3631},
    ]
    B_BUDGET = 71.760008
    return processors, tasks, B_BUDGET
