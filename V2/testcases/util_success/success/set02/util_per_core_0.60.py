"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519988, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519988, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067403, 'e_o_k': [0.177900, 0.142320], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 2.934057, 'e_o_k': [0.238588, 0.190870, 0.152696, 0.122157, 0.097726, 0.078180], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 9.868362, 'e_o_k': [1.213323, 0.970659, 0.776527], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 22.347468, 'e_o_k': [2.747639, 2.198112, 1.758489], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 7.228653, 'e_o_k': [0.734619, 0.587695, 0.470156, 0.376125], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.689155, 'e_o_k': [0.056040, 0.044832, 0.035865, 0.028692, 0.022954, 0.018363], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 1.979493, 'e_o_k': [0.176656, 0.141325, 0.113060, 0.090448, 0.072358], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 3.245124, 'e_o_k': [0.540854, 0.432683], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 143.519988
    return processors, tasks, B_BUDGET
