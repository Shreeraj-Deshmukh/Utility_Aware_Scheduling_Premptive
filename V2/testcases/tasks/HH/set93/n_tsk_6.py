"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.555997, 'e_o_k': [0.590466, 0.472373, 0.377898, 0.302319, 0.241855, 0.193484], 'p_i': 10, 'u_i': 3.2097},
        {'id': 1, 'e_m': 1.561617, 'e_o_k': [0.896010, 0.716808, 0.573446], 'p_i': 20, 'u_i': 3.3970},
        {'id': 2, 'e_m': 2.401288, 'e_o_k': [0.911235, 0.728988, 0.583191, 0.466553, 0.373242, 0.298594], 'p_i': 40, 'u_i': 4.0644},
        {'id': 3, 'e_m': 15.726898, 'e_o_k': [6.549755, 5.239804, 4.191843, 3.353475, 2.682780], 'p_i': 80, 'u_i': 4.4775},
        {'id': 4, 'e_m': 2.610152, 'e_o_k': [1.237877, 0.990301, 0.792241, 0.633793], 'p_i': 10, 'u_i': 1.6225},
        {'id': 5, 'e_m': 3.894872, 'e_o_k': [1.478018, 1.182414, 0.945931, 0.756745, 0.605396, 0.484317], 'p_i': 80, 'u_i': 1.5082},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
