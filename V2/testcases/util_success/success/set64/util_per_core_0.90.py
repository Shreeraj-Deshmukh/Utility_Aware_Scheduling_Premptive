"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279997, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279997, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.676074, 'e_o_k': [0.112679, 0.090143], 'p_i': 10, 'u_i': 2.7179},
        {'id': 1, 'e_m': 4.197256, 'e_o_k': [0.426550, 0.341240, 0.272992, 0.218394], 'p_i': 20, 'u_i': 2.6898},
        {'id': 2, 'e_m': 18.439252, 'e_o_k': [2.267121, 1.813697, 1.450958], 'p_i': 40, 'u_i': 4.5690},
        {'id': 3, 'e_m': 17.866493, 'e_o_k': [1.452844, 1.162275, 0.929820, 0.743856, 0.595085, 0.476068], 'p_i': 80, 'u_i': 4.7094},
        {'id': 4, 'e_m': 3.508895, 'e_o_k': [0.313145, 0.250516, 0.200413, 0.160330, 0.128264], 'p_i': 40, 'u_i': 1.5008},
        {'id': 5, 'e_m': 16.310677, 'e_o_k': [1.657589, 1.326071, 1.060857, 0.848686], 'p_i': 40, 'u_i': 3.0691},
        {'id': 6, 'e_m': 7.113128, 'e_o_k': [0.578416, 0.462733, 0.370186, 0.296149, 0.236919, 0.189535], 'p_i': 80, 'u_i': 2.7765},
        {'id': 7, 'e_m': 5.076279, 'e_o_k': [0.412786, 0.330229, 0.264183, 0.211347, 0.169077, 0.135262], 'p_i': 20, 'u_i': 1.2824},
    ]
    B_BUDGET = 215.279997
    return processors, tasks, B_BUDGET
