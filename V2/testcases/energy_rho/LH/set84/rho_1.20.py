"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 98.624, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.2, "seed": 1084, "set": 84, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.20"}
"""

_SPEC = '{"B": 98.624, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.2, "seed": 1084, "set": 84, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.20"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.242482, 'e_o_k': [0.100986, 0.080789, 0.064631, 0.051705, 0.041364], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.368320, 'e_o_k': [0.211331, 0.169065, 0.135252], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 2.283808, 'e_o_k': [1.083107, 0.866485, 0.693188, 0.554551], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 1.295241, 'e_o_k': [1.007410, 0.805928], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 0.598180, 'e_o_k': [0.283690, 0.226952, 0.181561, 0.145249], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 2.822117, 'e_o_k': [1.070931, 0.856745, 0.685396, 0.548317, 0.438653, 0.350923], 'p_i': 40, 'u_i': 3.8755},
        {'id': 6, 'e_m': 12.997943, 'e_o_k': [7.457836, 5.966269, 4.773015], 'p_i': 80, 'u_i': 3.4836},
        {'id': 7, 'e_m': 1.741824, 'e_o_k': [0.999407, 0.799526, 0.639621], 'p_i': 40, 'u_i': 4.1699},
    ]
    B_BUDGET = 98.624000
    return processors, tasks, B_BUDGET
