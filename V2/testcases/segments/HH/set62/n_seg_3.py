"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.118502, 'e_o_k': [1.215534, 0.972427, 0.777942], 'p_i': 10, 'u_i': 2.6711},
        {'id': 1, 'e_m': 1.874501, 'e_o_k': [1.075534, 0.860427, 0.688341], 'p_i': 20, 'u_i': 2.3833},
        {'id': 2, 'e_m': 1.286629, 'e_o_k': [0.738230, 0.590584, 0.472467], 'p_i': 40, 'u_i': 4.1647},
        {'id': 3, 'e_m': 1.712942, 'e_o_k': [0.982835, 0.786268, 0.629015], 'p_i': 80, 'u_i': 1.2796},
        {'id': 4, 'e_m': 2.907669, 'e_o_k': [1.668335, 1.334668, 1.067734], 'p_i': 10, 'u_i': 2.4526},
        {'id': 5, 'e_m': 0.484065, 'e_o_k': [0.277742, 0.222194, 0.177755], 'p_i': 10, 'u_i': 3.7482},
        {'id': 6, 'e_m': 7.564502, 'e_o_k': [4.340288, 3.472231, 2.777784], 'p_i': 80, 'u_i': 2.1247},
        {'id': 7, 'e_m': 0.284703, 'e_o_k': [0.163354, 0.130683, 0.104547], 'p_i': 40, 'u_i': 4.6336},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
