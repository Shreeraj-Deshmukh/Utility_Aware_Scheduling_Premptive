"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.647287, 'e_o_k': [0.337559, 0.270047, 0.216038], 'p_i': 10, 'u_i': 2.3752},
        {'id': 1, 'e_m': 0.034300, 'e_o_k': [0.007029, 0.005623, 0.004498], 'p_i': 20, 'u_i': 4.5040},
        {'id': 2, 'e_m': 2.925892, 'e_o_k': [0.599568, 0.479654, 0.383723], 'p_i': 40, 'u_i': 4.7123},
        {'id': 3, 'e_m': 1.655242, 'e_o_k': [0.339189, 0.271351, 0.217081], 'p_i': 80, 'u_i': 4.3702},
        {'id': 4, 'e_m': 0.978124, 'e_o_k': [0.200435, 0.160348, 0.128279], 'p_i': 20, 'u_i': 3.7678},
        {'id': 5, 'e_m': 1.868312, 'e_o_k': [0.382851, 0.306281, 0.245025], 'p_i': 40, 'u_i': 3.2312},
        {'id': 6, 'e_m': 15.433016, 'e_o_k': [3.162503, 2.530003, 2.024002], 'p_i': 80, 'u_i': 3.7207},
        {'id': 7, 'e_m': 10.047671, 'e_o_k': [2.058949, 1.647159, 1.317727], 'p_i': 40, 'u_i': 2.0745},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
