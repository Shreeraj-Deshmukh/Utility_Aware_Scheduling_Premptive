"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319992, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319992, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.536605, 'e_o_k': [0.417359, 0.333887], 'p_i': 10, 'u_i': 3.4396},
        {'id': 1, 'e_m': 1.004911, 'e_o_k': [0.781598, 0.625278], 'p_i': 20, 'u_i': 1.7213},
        {'id': 2, 'e_m': 2.250211, 'e_o_k': [1.750164, 1.400131], 'p_i': 40, 'u_i': 2.3007},
        {'id': 3, 'e_m': 2.587062, 'e_o_k': [2.012159, 1.609727], 'p_i': 80, 'u_i': 2.4667},
        {'id': 4, 'e_m': 2.270607, 'e_o_k': [1.766028, 1.412822], 'p_i': 80, 'u_i': 2.4016},
        {'id': 5, 'e_m': 0.342865, 'e_o_k': [0.266673, 0.213338], 'p_i': 10, 'u_i': 3.4602},
        {'id': 6, 'e_m': 7.548057, 'e_o_k': [5.870711, 4.696569], 'p_i': 80, 'u_i': 3.9709},
        {'id': 7, 'e_m': 4.038448, 'e_o_k': [3.141015, 2.512812], 'p_i': 80, 'u_i': 1.7339},
    ]
    B_BUDGET = 88.319992
    return processors, tasks, B_BUDGET
