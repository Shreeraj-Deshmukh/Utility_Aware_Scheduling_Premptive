"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.178484, 'e_o_k': [0.084647, 0.067718, 0.054174, 0.043339], 'p_i': 10, 'u_i': 4.6156},
        {'id': 1, 'e_m': 0.396303, 'e_o_k': [0.187948, 0.150359, 0.120287, 0.096230], 'p_i': 20, 'u_i': 1.3815},
        {'id': 2, 'e_m': 0.607908, 'e_o_k': [0.348800, 0.279040, 0.223232], 'p_i': 40, 'u_i': 2.2542},
        {'id': 3, 'e_m': 13.292945, 'e_o_k': [5.044378, 4.035502, 3.228402, 2.582721, 2.066177, 1.652942], 'p_i': 80, 'u_i': 3.1493},
        {'id': 4, 'e_m': 3.115303, 'e_o_k': [1.477447, 1.181958, 0.945566, 0.756453], 'p_i': 20, 'u_i': 4.3022},
        {'id': 5, 'e_m': 2.016943, 'e_o_k': [0.765385, 0.612308, 0.489847, 0.391877, 0.313502, 0.250801], 'p_i': 80, 'u_i': 4.8493},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
