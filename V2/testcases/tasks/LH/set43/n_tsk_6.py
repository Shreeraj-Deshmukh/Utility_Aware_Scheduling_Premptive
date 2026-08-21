"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.036102, 'e_o_k': [0.020714, 0.016571, 0.013257], 'p_i': 10, 'u_i': 4.0506},
        {'id': 1, 'e_m': 1.771436, 'e_o_k': [1.016398, 0.813118, 0.650495], 'p_i': 20, 'u_i': 2.8657},
        {'id': 2, 'e_m': 2.727861, 'e_o_k': [1.293701, 1.034961, 0.827969, 0.662375], 'p_i': 40, 'u_i': 2.1758},
        {'id': 3, 'e_m': 3.290322, 'e_o_k': [2.559139, 2.047311], 'p_i': 80, 'u_i': 2.5351},
        {'id': 4, 'e_m': 0.843218, 'e_o_k': [0.399900, 0.319920, 0.255936, 0.204749], 'p_i': 40, 'u_i': 3.6072},
        {'id': 5, 'e_m': 7.096482, 'e_o_k': [2.692958, 2.154366, 1.723493, 1.378794, 1.103035, 0.882428], 'p_i': 40, 'u_i': 4.5999},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
