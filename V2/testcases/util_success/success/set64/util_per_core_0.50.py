"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599993, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599993, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.804186, 'e_o_k': [0.161011, 0.128809, 0.103047, 0.082438, 0.065950], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 6.240347, 'e_o_k': [1.040058, 0.832046], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 2.216251, 'e_o_k': [0.272490, 0.217992, 0.174394], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 6.026152, 'e_o_k': [0.612414, 0.489931, 0.391945, 0.313556], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 7.370905, 'e_o_k': [0.657803, 0.526243, 0.420994, 0.336795, 0.269436], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 11.492218, 'e_o_k': [1.915370, 1.532296], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.011898, 'e_o_k': [0.001209, 0.000967, 0.000774, 0.000619], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 0.972162, 'e_o_k': [0.119528, 0.095622, 0.076498], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 119.599993
    return processors, tasks, B_BUDGET
