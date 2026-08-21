"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.63998, "H": 80, "J": 30, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "8"}
"""

_SPEC = '{"B": 176.63998, "H": 80, "J": 30, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "8"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067561, 'e_o_k': [0.444606, 0.355684, 0.284548, 0.227638, 0.182110], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 6.103602, 'e_o_k': [4.747246, 3.797797], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 4.537756, 'e_o_k': [3.529365, 2.823492], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 4.054946, 'e_o_k': [1.538762, 1.231010, 0.984808, 0.787846, 0.630277, 0.504222], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.349178, 'e_o_k': [0.271583, 0.217267], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.690991, 'e_o_k': [0.396470, 0.317176, 0.253741], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 5.436589, 'e_o_k': [2.578328, 2.062663, 1.650130, 1.320104], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 2.776704, 'e_o_k': [1.593191, 1.274553, 1.019642], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 176.639980
    return processors, tasks, B_BUDGET
