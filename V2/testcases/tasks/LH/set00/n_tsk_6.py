"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.196494, 'e_o_k': [0.112743, 0.090194, 0.072155], 'p_i': 10, 'u_i': 3.6850},
        {'id': 1, 'e_m': 0.725173, 'e_o_k': [0.343917, 0.275133, 0.220107, 0.176085], 'p_i': 20, 'u_i': 3.7169},
        {'id': 2, 'e_m': 7.393519, 'e_o_k': [4.242183, 3.393746, 2.714997], 'p_i': 40, 'u_i': 3.7239},
        {'id': 3, 'e_m': 5.171126, 'e_o_k': [2.452431, 1.961945, 1.569556, 1.255645], 'p_i': 80, 'u_i': 1.9107},
        {'id': 4, 'e_m': 4.027507, 'e_o_k': [1.677329, 1.341863, 1.073491, 0.858793, 0.687034], 'p_i': 80, 'u_i': 1.7322},
        {'id': 5, 'e_m': 0.885421, 'e_o_k': [0.368750, 0.295000, 0.236000, 0.188800, 0.151040], 'p_i': 20, 'u_i': 1.5709},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
