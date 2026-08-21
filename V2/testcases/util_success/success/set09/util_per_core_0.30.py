"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759985, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759985, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.302921, 'e_o_k': [0.217153, 0.173723], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 1.060548, 'e_o_k': [0.086240, 0.068992, 0.055194, 0.044155, 0.035324, 0.028259], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 6.671221, 'e_o_k': [0.595361, 0.476289, 0.381031, 0.304825, 0.243860], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 2.994241, 'e_o_k': [0.499040, 0.399232], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.117016, 'e_o_k': [0.010443, 0.008354, 0.006683, 0.005347, 0.004277], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.264133, 'e_o_k': [0.032475, 0.025980, 0.020784], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 3.845316, 'e_o_k': [0.390784, 0.312627, 0.250102, 0.200081], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 0.972816, 'e_o_k': [0.119609, 0.095687, 0.076549], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 71.759985
    return processors, tasks, B_BUDGET
