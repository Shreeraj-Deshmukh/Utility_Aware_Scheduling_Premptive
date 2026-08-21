"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.153313, 'e_o_k': [0.042587, 0.034070], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.148369, 'e_o_k': [0.041214, 0.032971], 'p_i': 20, 'u_i': 1.9533},
        {'id': 2, 'e_m': 2.270223, 'e_o_k': [0.630618, 0.504494], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 7.275677, 'e_o_k': [2.021021, 1.616817], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 2.680502, 'e_o_k': [0.744584, 0.595667], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 1.468106, 'e_o_k': [0.407807, 0.326246], 'p_i': 40, 'u_i': 1.1221},
        {'id': 6, 'e_m': 0.569881, 'e_o_k': [0.158300, 0.126640], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.303269, 'e_o_k': [0.084241, 0.067393], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
