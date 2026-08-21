"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440002, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440002, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.771688, 'e_o_k': [0.281676, 0.225340, 0.180272, 0.144218], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 5.092828, 'e_o_k': [0.848805, 0.679044], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 11.940655, 'e_o_k': [0.970974, 0.776780, 0.621424, 0.497139, 0.397711, 0.318169], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 5.284424, 'e_o_k': [0.649724, 0.519779, 0.415824], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 6.853719, 'e_o_k': [0.557322, 0.445857, 0.356686, 0.285349, 0.228279, 0.182623], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 4.736315, 'e_o_k': [0.582334, 0.465867, 0.372694], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 14.404766, 'e_o_k': [1.285528, 1.028422, 0.822738, 0.658190, 0.526552], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 2.389584, 'e_o_k': [0.242844, 0.194275, 0.155420, 0.124336], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 167.440002
    return processors, tasks, B_BUDGET
