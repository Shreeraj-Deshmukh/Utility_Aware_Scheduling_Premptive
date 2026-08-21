"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 31, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 31, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.030035, 0.024028, 0.019222, 0.015378, 0.012302, 0.009842], 'p_i': 10, 'u_i': 3.1944},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.028635, 0.022908, 0.018326, 0.014661, 0.011729], 'p_i': 20, 'u_i': 2.9776},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [0.608651, 0.486921, 0.389537, 0.311629], 'p_i': 40, 'u_i': 3.0186},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [2.863988, 2.291190], 'p_i': 80, 'u_i': 3.0275},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.098362, 0.078690, 0.062952, 0.050361, 0.040289, 0.032231], 'p_i': 20, 'u_i': 3.2436},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.137941, 0.110352, 0.088282], 'p_i': 10, 'u_i': 2.6439},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.211879, 0.169503, 0.135602], 'p_i': 40, 'u_i': 3.4985},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.222709, 0.178167], 'p_i': 40, 'u_i': 2.6908},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
