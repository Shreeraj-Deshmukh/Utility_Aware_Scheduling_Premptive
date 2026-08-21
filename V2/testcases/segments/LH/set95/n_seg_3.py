"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.791911, 'e_o_k': [0.454375, 0.363500, 0.290800], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 1.455094, 'e_o_k': [0.834890, 0.667912, 0.534329], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 3.411616, 'e_o_k': [1.957484, 1.565988, 1.252790], 'p_i': 40, 'u_i': 4.3076},
        {'id': 3, 'e_m': 1.509835, 'e_o_k': [0.866299, 0.693039, 0.554431], 'p_i': 80, 'u_i': 2.0651},
        {'id': 4, 'e_m': 1.958205, 'e_o_k': [1.123560, 0.898848, 0.719079], 'p_i': 80, 'u_i': 2.7475},
        {'id': 5, 'e_m': 1.353233, 'e_o_k': [0.776445, 0.621156, 0.496925], 'p_i': 40, 'u_i': 2.9584},
        {'id': 6, 'e_m': 4.115647, 'e_o_k': [2.361437, 1.889150, 1.511320], 'p_i': 80, 'u_i': 3.8181},
        {'id': 7, 'e_m': 0.682738, 'e_o_k': [0.391735, 0.313388, 0.250710], 'p_i': 20, 'u_i': 3.4213},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
