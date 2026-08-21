"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.282719, 'e_o_k': [0.162216, 0.129773, 0.103818], 'p_i': 10, 'u_i': 4.9222},
        {'id': 1, 'e_m': 0.997197, 'e_o_k': [0.572162, 0.457730, 0.366184], 'p_i': 20, 'u_i': 1.9107},
        {'id': 2, 'e_m': 10.687466, 'e_o_k': [6.132153, 4.905722, 3.924578], 'p_i': 40, 'u_i': 1.7322},
        {'id': 3, 'e_m': 8.337500, 'e_o_k': [4.783812, 3.827049, 3.061639], 'p_i': 80, 'u_i': 1.5709},
        {'id': 4, 'e_m': 1.567672, 'e_o_k': [0.899484, 0.719587, 0.575670], 'p_i': 20, 'u_i': 3.7661},
        {'id': 5, 'e_m': 1.462585, 'e_o_k': [0.839188, 0.671351, 0.537080], 'p_i': 20, 'u_i': 1.0932},
        {'id': 6, 'e_m': 0.086308, 'e_o_k': [0.049521, 0.039617, 0.031694], 'p_i': 20, 'u_i': 3.8665},
        {'id': 7, 'e_m': 7.785382, 'e_o_k': [4.467023, 3.573618, 2.858894], 'p_i': 40, 'u_i': 4.9324},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
