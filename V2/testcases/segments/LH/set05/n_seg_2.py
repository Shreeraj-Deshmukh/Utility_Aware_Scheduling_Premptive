"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.394847, 'e_o_k': [0.307103, 0.245682], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.122647, 'e_o_k': [0.095392, 0.076314], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 1.655397, 'e_o_k': [1.287531, 1.030025], 'p_i': 40, 'u_i': 2.1879},
        {'id': 3, 'e_m': 0.814260, 'e_o_k': [0.633313, 0.506650], 'p_i': 80, 'u_i': 2.3607},
        {'id': 4, 'e_m': 1.025576, 'e_o_k': [0.797670, 0.638136], 'p_i': 20, 'u_i': 2.0600},
        {'id': 5, 'e_m': 0.055175, 'e_o_k': [0.042914, 0.034331], 'p_i': 80, 'u_i': 2.1803},
        {'id': 6, 'e_m': 1.611854, 'e_o_k': [1.253664, 1.002931], 'p_i': 10, 'u_i': 4.5157},
        {'id': 7, 'e_m': 3.586638, 'e_o_k': [2.789607, 2.231686], 'p_i': 40, 'u_i': 4.4957},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
