"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199986, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199986, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.177798, 'e_o_k': [0.026445, 0.021156, 0.016925, 0.013540, 0.010832], 'p_i': 10, 'u_i': 3.8879},
        {'id': 1, 'e_m': 3.882856, 'e_o_k': [0.526235, 0.420988, 0.336790, 0.269432, 0.215546, 0.172437], 'p_i': 20, 'u_i': 3.5961},
        {'id': 2, 'e_m': 0.656943, 'e_o_k': [0.097713, 0.078170, 0.062536, 0.050029, 0.040023], 'p_i': 40, 'u_i': 4.1247},
        {'id': 3, 'e_m': 0.977487, 'e_o_k': [0.200305, 0.160244, 0.128195], 'p_i': 80, 'u_i': 3.4312},
        {'id': 4, 'e_m': 11.590635, 'e_o_k': [3.219621, 2.575697], 'p_i': 80, 'u_i': 1.1226},
        {'id': 5, 'e_m': 0.291046, 'e_o_k': [0.043290, 0.034632, 0.027705, 0.022164, 0.017731], 'p_i': 20, 'u_i': 3.8598},
    ]
    B_BUDGET = 55.199986
    return processors, tasks, B_BUDGET
