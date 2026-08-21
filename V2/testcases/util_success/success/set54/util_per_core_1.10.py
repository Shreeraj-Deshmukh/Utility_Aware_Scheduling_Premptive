"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119978, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119978, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.188440, 'e_o_k': [0.259273, 0.207419, 0.165935, 0.132748, 0.106198, 0.084959], 'p_i': 10, 'u_i': 4.3896},
        {'id': 1, 'e_m': 6.660313, 'e_o_k': [0.676861, 0.541489, 0.433191, 0.346553], 'p_i': 20, 'u_i': 4.5380},
        {'id': 2, 'e_m': 9.770621, 'e_o_k': [0.794514, 0.635612, 0.508489, 0.406791, 0.325433, 0.260346], 'p_i': 40, 'u_i': 2.5931},
        {'id': 3, 'e_m': 34.762967, 'e_o_k': [5.793828, 4.635062], 'p_i': 80, 'u_i': 2.1006},
        {'id': 4, 'e_m': 1.208796, 'e_o_k': [0.098295, 0.078636, 0.062909, 0.050327, 0.040262, 0.032209], 'p_i': 20, 'u_i': 1.6702},
        {'id': 5, 'e_m': 7.413457, 'e_o_k': [1.235576, 0.988461], 'p_i': 40, 'u_i': 4.1560},
        {'id': 6, 'e_m': 1.784214, 'e_o_k': [0.145086, 0.116069, 0.092855, 0.074284, 0.059427, 0.047542], 'p_i': 10, 'u_i': 3.0539},
        {'id': 7, 'e_m': 8.902802, 'e_o_k': [1.094607, 0.875685, 0.700548], 'p_i': 20, 'u_i': 4.7065},
    ]
    B_BUDGET = 263.119978
    return processors, tasks, B_BUDGET
