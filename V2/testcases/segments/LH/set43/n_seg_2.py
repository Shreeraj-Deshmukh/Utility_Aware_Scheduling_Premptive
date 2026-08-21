"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.025820, 'e_o_k': [0.020082, 0.016066], 'p_i': 10, 'u_i': 4.0574},
        {'id': 1, 'e_m': 1.233166, 'e_o_k': [0.959129, 0.767303], 'p_i': 20, 'u_i': 2.7090},
        {'id': 2, 'e_m': 1.873854, 'e_o_k': [1.457442, 1.165953], 'p_i': 40, 'u_i': 3.6072},
        {'id': 3, 'e_m': 2.076895, 'e_o_k': [1.615363, 1.292290], 'p_i': 80, 'u_i': 4.0494},
        {'id': 4, 'e_m': 0.193184, 'e_o_k': [0.150255, 0.120204], 'p_i': 20, 'u_i': 4.5815},
        {'id': 5, 'e_m': 2.190958, 'e_o_k': [1.704078, 1.363263], 'p_i': 20, 'u_i': 1.1362},
        {'id': 6, 'e_m': 0.888908, 'e_o_k': [0.691373, 0.553098], 'p_i': 80, 'u_i': 3.3217},
        {'id': 7, 'e_m': 5.305348, 'e_o_k': [4.126381, 3.301105], 'p_i': 40, 'u_i': 1.1761},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
