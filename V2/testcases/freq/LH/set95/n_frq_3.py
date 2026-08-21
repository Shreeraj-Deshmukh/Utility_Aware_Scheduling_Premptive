"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 23, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "freq", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 23, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "freq", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.791911, 'e_o_k': [0.375567, 0.300454, 0.240363, 0.192291], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 1.455094, 'e_o_k': [1.131740, 0.905392], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 3.411616, 'e_o_k': [1.294633, 1.035706, 0.828565, 0.662852, 0.530282, 0.424225], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 1.509835, 'e_o_k': [0.866299, 0.693039, 0.554431], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 1.958205, 'e_o_k': [0.743096, 0.594476, 0.475581, 0.380465, 0.304372, 0.243498], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 1.353233, 'e_o_k': [0.776445, 0.621156, 0.496925], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 4.115647, 'e_o_k': [1.714037, 1.371230, 1.096984, 0.877587, 0.702070], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 0.682738, 'e_o_k': [0.323792, 0.259033, 0.207227, 0.165781], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
