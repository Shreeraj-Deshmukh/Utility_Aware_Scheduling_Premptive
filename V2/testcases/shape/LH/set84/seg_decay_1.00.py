"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.242482, 'e_o_k': [0.067895, 0.067895, 0.067895, 0.067895, 0.067895], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.368320, 'e_o_k': [0.171883, 0.171883, 0.171883], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 2.283808, 'e_o_k': [0.799333, 0.799333, 0.799333, 0.799333], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 1.295241, 'e_o_k': [0.906669, 0.906669], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 0.598180, 'e_o_k': [0.209363, 0.209363, 0.209363, 0.209363], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 2.822117, 'e_o_k': [0.658494, 0.658494, 0.658494, 0.658494, 0.658494, 0.658494], 'p_i': 40, 'u_i': 3.8755},
        {'id': 6, 'e_m': 12.997943, 'e_o_k': [6.065707, 6.065707, 6.065707], 'p_i': 80, 'u_i': 3.4836},
        {'id': 7, 'e_m': 1.741824, 'e_o_k': [0.812851, 0.812851, 0.812851], 'p_i': 40, 'u_i': 4.1699},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
