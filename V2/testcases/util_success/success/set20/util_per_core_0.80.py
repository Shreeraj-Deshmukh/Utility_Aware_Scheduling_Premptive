"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359989, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359989, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.286671, 'e_o_k': [0.382556, 0.306045, 0.244836, 0.195869, 0.156695], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 2.827908, 'e_o_k': [0.229956, 0.183965, 0.147172, 0.117738, 0.094190, 0.075352], 'p_i': 20, 'u_i': 3.9781},
        {'id': 2, 'e_m': 6.805741, 'e_o_k': [0.836771, 0.669417, 0.535534], 'p_i': 40, 'u_i': 2.6834},
        {'id': 3, 'e_m': 24.002627, 'e_o_k': [4.000438, 3.200350], 'p_i': 80, 'u_i': 1.3712},
        {'id': 4, 'e_m': 1.776299, 'e_o_k': [0.158523, 0.126818, 0.101454, 0.081164, 0.064931], 'p_i': 40, 'u_i': 4.1249},
        {'id': 5, 'e_m': 4.629421, 'e_o_k': [0.376449, 0.301159, 0.240927, 0.192742, 0.154194, 0.123355], 'p_i': 40, 'u_i': 1.3639},
        {'id': 6, 'e_m': 20.313604, 'e_o_k': [1.812851, 1.450281, 1.160225, 0.928180, 0.742544], 'p_i': 80, 'u_i': 1.0001},
        {'id': 7, 'e_m': 1.456980, 'e_o_k': [0.130026, 0.104021, 0.083216, 0.066573, 0.053258], 'p_i': 10, 'u_i': 1.8994},
    ]
    B_BUDGET = 191.359989
    return processors, tasks, B_BUDGET
