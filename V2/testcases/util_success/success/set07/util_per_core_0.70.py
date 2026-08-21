"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440006, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440006, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.564413, 'e_o_k': [0.192346, 0.153877, 0.123101], 'p_i': 10, 'u_i': 3.5354},
        {'id': 1, 'e_m': 6.038119, 'e_o_k': [0.613630, 0.490904, 0.392723, 0.314179], 'p_i': 20, 'u_i': 3.2835},
        {'id': 2, 'e_m': 0.582674, 'e_o_k': [0.097112, 0.077690], 'p_i': 40, 'u_i': 1.9722},
        {'id': 3, 'e_m': 1.903292, 'e_o_k': [0.317215, 0.253772], 'p_i': 80, 'u_i': 1.1966},
        {'id': 4, 'e_m': 18.256477, 'e_o_k': [1.629267, 1.303413, 1.042731, 0.834185, 0.667348], 'p_i': 40, 'u_i': 1.4854},
        {'id': 5, 'e_m': 1.508290, 'e_o_k': [0.134605, 0.107684, 0.086147, 0.068918, 0.055134], 'p_i': 80, 'u_i': 2.1351},
        {'id': 6, 'e_m': 6.273133, 'e_o_k': [0.559835, 0.447868, 0.358294, 0.286635, 0.229308], 'p_i': 40, 'u_i': 2.0679},
        {'id': 7, 'e_m': 10.848035, 'e_o_k': [1.808006, 1.446405], 'p_i': 40, 'u_i': 2.5055},
    ]
    B_BUDGET = 167.440006
    return processors, tasks, B_BUDGET
