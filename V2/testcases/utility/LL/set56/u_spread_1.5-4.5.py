"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199985, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 55.199985, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.075032, 'e_o_k': [0.145697, 0.116557, 0.093246, 0.074597, 0.059677, 0.047742], 'p_i': 10, 'u_i': 3.6443},
        {'id': 1, 'e_m': 0.138443, 'e_o_k': [0.020592, 0.016473, 0.013179, 0.010543, 0.008434], 'p_i': 20, 'u_i': 3.5237},
        {'id': 2, 'e_m': 0.518452, 'e_o_k': [0.077114, 0.061691, 0.049353, 0.039482, 0.031586], 'p_i': 40, 'u_i': 3.0503},
        {'id': 3, 'e_m': 0.130830, 'e_o_k': [0.036342, 0.029073], 'p_i': 80, 'u_i': 2.4410},
        {'id': 4, 'e_m': 6.327178, 'e_o_k': [1.757549, 1.406040], 'p_i': 80, 'u_i': 3.2721},
        {'id': 5, 'e_m': 0.084400, 'e_o_k': [0.023444, 0.018755], 'p_i': 10, 'u_i': 2.2073},
        {'id': 6, 'e_m': 1.306253, 'e_o_k': [0.194290, 0.155432, 0.124346, 0.099477, 0.079581], 'p_i': 80, 'u_i': 3.9286},
        {'id': 7, 'e_m': 1.671201, 'e_o_k': [0.342459, 0.273967, 0.219174], 'p_i': 10, 'u_i': 1.9262},
    ]
    B_BUDGET = 55.199985
    return processors, tasks, B_BUDGET
