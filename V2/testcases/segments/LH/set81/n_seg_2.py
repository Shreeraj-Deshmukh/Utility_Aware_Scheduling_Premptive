"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.404009, 'e_o_k': [0.314229, 0.251384], 'p_i': 10, 'u_i': 4.1044},
        {'id': 1, 'e_m': 1.312342, 'e_o_k': [1.020711, 0.816569], 'p_i': 20, 'u_i': 3.5158},
        {'id': 2, 'e_m': 1.516961, 'e_o_k': [1.179858, 0.943887], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 10.070496, 'e_o_k': [7.832608, 6.266086], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 1.082847, 'e_o_k': [0.842214, 0.673771], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.068047, 'e_o_k': [0.052925, 0.042340], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 1.937905, 'e_o_k': [1.507259, 1.205807], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.241844, 'e_o_k': [0.188101, 0.150481], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET
