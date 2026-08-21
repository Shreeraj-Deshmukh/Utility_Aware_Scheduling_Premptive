"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.396763, 'e_o_k': [0.308593, 0.246875], 'p_i': 10, 'u_i': 3.3143},
        {'id': 1, 'e_m': 0.524964, 'e_o_k': [0.408306, 0.326644], 'p_i': 20, 'u_i': 3.2246},
        {'id': 2, 'e_m': 3.768792, 'e_o_k': [2.931283, 2.345026], 'p_i': 40, 'u_i': 4.6504},
        {'id': 3, 'e_m': 8.561063, 'e_o_k': [6.658604, 5.326884], 'p_i': 80, 'u_i': 4.9346},
        {'id': 4, 'e_m': 0.427036, 'e_o_k': [0.332139, 0.265711], 'p_i': 10, 'u_i': 2.0105},
        {'id': 5, 'e_m': 1.656317, 'e_o_k': [1.288246, 1.030597], 'p_i': 40, 'u_i': 3.0068},
        {'id': 6, 'e_m': 0.919393, 'e_o_k': [0.715084, 0.572067], 'p_i': 80, 'u_i': 1.6248},
        {'id': 7, 'e_m': 2.979082, 'e_o_k': [2.317064, 1.853651], 'p_i': 80, 'u_i': 2.1190},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
