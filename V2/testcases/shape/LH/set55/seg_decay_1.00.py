"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.181209, 'e_o_k': [0.275615, 0.275615, 0.275615, 0.275615, 0.275615, 0.275615], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 0.909186, 'e_o_k': [0.424287, 0.424287, 0.424287], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 1.009200, 'e_o_k': [0.470960, 0.470960, 0.470960], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 5.488802, 'e_o_k': [2.561441, 2.561441, 2.561441], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 2.719998, 'e_o_k': [0.761600, 0.761600, 0.761600, 0.761600, 0.761600], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.142051, 'e_o_k': [0.049718, 0.049718, 0.049718, 0.049718], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 0.727869, 'e_o_k': [0.509508, 0.509508], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 3.047121, 'e_o_k': [1.066492, 1.066492, 1.066492, 1.066492], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
