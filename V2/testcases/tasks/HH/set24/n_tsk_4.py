"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.582593, 'e_o_k': [0.221081, 0.176865, 0.141492, 0.113193, 0.090555, 0.072444], 'p_i': 10, 'u_i': 1.4017},
        {'id': 1, 'e_m': 4.519562, 'e_o_k': [1.715074, 1.372059, 1.097647, 0.878118, 0.702494, 0.561995], 'p_i': 20, 'u_i': 2.4636},
        {'id': 2, 'e_m': 12.596412, 'e_o_k': [5.973908, 4.779127, 3.823301, 3.058641], 'p_i': 40, 'u_i': 2.5536},
        {'id': 3, 'e_m': 16.068185, 'e_o_k': [12.497477, 9.997982], 'p_i': 80, 'u_i': 3.8458},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
