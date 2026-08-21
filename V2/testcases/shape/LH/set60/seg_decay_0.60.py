"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320011, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320011, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.728311, 'e_o_k': [0.468582, 0.281149, 0.168690, 0.101214], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 3.236491, 'e_o_k': [2.311779, 1.387068, 0.832241], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 0.535015, 'e_o_k': [0.382154, 0.229292, 0.137575], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 4.750488, 'e_o_k': [2.790465, 1.674279, 1.004567, 0.602740, 0.361644, 0.216987], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.182718, 'e_o_k': [0.159878, 0.095927], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.092022, 'e_o_k': [0.065730, 0.039438, 0.023663], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 2.641333, 'e_o_k': [1.699387, 1.019632, 0.611779, 0.367068], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.127844, 'e_o_k': [0.082253, 0.049352, 0.029611, 0.017767], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 88.320011
    return processors, tasks, B_BUDGET
