"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680005, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680005, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.237773, 'e_o_k': [0.021220, 0.016976, 0.013581, 0.010864, 0.008692], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 2.303196, 'e_o_k': [0.283180, 0.226544, 0.181235], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 7.567437, 'e_o_k': [0.675342, 0.540274, 0.432219, 0.345775, 0.276620], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 20.093036, 'e_o_k': [1.793167, 1.434534, 1.147627, 0.918102, 0.734481], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.219572, 'e_o_k': [0.026997, 0.021597, 0.017278], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 9.972517, 'e_o_k': [0.810932, 0.648746, 0.518996, 0.415197, 0.332158, 0.265726], 'p_i': 80, 'u_i': 3.4160},
        {'id': 6, 'e_m': 3.107005, 'e_o_k': [0.382009, 0.305607, 0.244486], 'p_i': 80, 'u_i': 3.4712},
        {'id': 7, 'e_m': 0.705255, 'e_o_k': [0.062939, 0.050351, 0.040281, 0.032225, 0.025780], 'p_i': 20, 'u_i': 4.3322},
    ]
    B_BUDGET = 95.680005
    return processors, tasks, B_BUDGET
