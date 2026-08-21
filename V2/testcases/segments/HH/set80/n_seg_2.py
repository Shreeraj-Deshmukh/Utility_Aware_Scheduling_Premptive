"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.256635, 'e_o_k': [0.199605, 0.159684], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.540076, 'e_o_k': [0.420059, 0.336047], 'p_i': 20, 'u_i': 2.1078},
        {'id': 2, 'e_m': 0.758738, 'e_o_k': [0.590130, 0.472104], 'p_i': 40, 'u_i': 4.2406},
        {'id': 3, 'e_m': 16.196605, 'e_o_k': [12.597360, 10.077888], 'p_i': 80, 'u_i': 1.1754},
        {'id': 4, 'e_m': 10.131188, 'e_o_k': [7.879813, 6.303850], 'p_i': 40, 'u_i': 3.4237},
        {'id': 5, 'e_m': 6.084943, 'e_o_k': [4.732734, 3.786187], 'p_i': 40, 'u_i': 1.7653},
        {'id': 6, 'e_m': 0.825239, 'e_o_k': [0.641853, 0.513482], 'p_i': 10, 'u_i': 3.9977},
        {'id': 7, 'e_m': 0.759590, 'e_o_k': [0.590792, 0.472634], 'p_i': 20, 'u_i': 1.6134},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
