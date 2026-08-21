"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.162195, 'e_o_k': [0.094506, 0.075605, 0.060484, 0.048387, 0.038710, 0.030968], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.071097, 'e_o_k': [0.005781, 0.004625, 0.003700, 0.002960, 0.002368, 0.001894], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 3.279992, 'e_o_k': [0.546665, 0.437332], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 5.593341, 'e_o_k': [0.932223, 0.745779], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 2.937085, 'e_o_k': [0.489514, 0.391611], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 13.178735, 'e_o_k': [1.339302, 1.071442, 0.857154, 0.685723], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.428070, 'e_o_k': [0.071345, 0.057076], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 4.183589, 'e_o_k': [0.697265, 0.557812], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 119.600006
    return processors, tasks, B_BUDGET
