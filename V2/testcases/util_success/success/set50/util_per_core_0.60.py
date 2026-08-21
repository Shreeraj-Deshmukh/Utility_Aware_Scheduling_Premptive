"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.793466, 'e_o_k': [0.145839, 0.116671, 0.093337, 0.074669, 0.059736, 0.047788], 'p_i': 10, 'u_i': 2.5141},
        {'id': 1, 'e_m': 1.611984, 'e_o_k': [0.268664, 0.214931], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 5.561303, 'e_o_k': [0.452227, 0.361781, 0.289425, 0.231540, 0.185232, 0.148186], 'p_i': 40, 'u_i': 2.8954},
        {'id': 3, 'e_m': 14.896053, 'e_o_k': [1.329372, 1.063497, 0.850798, 0.680638, 0.544511], 'p_i': 80, 'u_i': 2.6615},
        {'id': 4, 'e_m': 0.377572, 'e_o_k': [0.038371, 0.030697, 0.024558, 0.019646], 'p_i': 10, 'u_i': 4.2574},
        {'id': 5, 'e_m': 2.960960, 'e_o_k': [0.300911, 0.240728, 0.192583, 0.154066], 'p_i': 80, 'u_i': 4.9741},
        {'id': 6, 'e_m': 35.811158, 'e_o_k': [4.403011, 3.522409, 2.817927], 'p_i': 80, 'u_i': 2.2740},
        {'id': 7, 'e_m': 3.696490, 'e_o_k': [0.329887, 0.263909, 0.211127, 0.168902, 0.135122], 'p_i': 40, 'u_i': 2.9164},
    ]
    B_BUDGET = 143.520000
    return processors, tasks, B_BUDGET
