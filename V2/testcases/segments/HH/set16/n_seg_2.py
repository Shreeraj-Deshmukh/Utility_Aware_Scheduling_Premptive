"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.073209, 'e_o_k': [0.834718, 0.667775], 'p_i': 10, 'u_i': 3.4396},
        {'id': 1, 'e_m': 2.009822, 'e_o_k': [1.563195, 1.250556], 'p_i': 20, 'u_i': 1.7213},
        {'id': 2, 'e_m': 4.500422, 'e_o_k': [3.500328, 2.800263], 'p_i': 40, 'u_i': 2.3007},
        {'id': 3, 'e_m': 5.174123, 'e_o_k': [4.024318, 3.219455], 'p_i': 80, 'u_i': 2.4667},
        {'id': 4, 'e_m': 4.541214, 'e_o_k': [3.532055, 2.825644], 'p_i': 80, 'u_i': 2.4016},
        {'id': 5, 'e_m': 0.685731, 'e_o_k': [0.533346, 0.426677], 'p_i': 10, 'u_i': 3.4602},
        {'id': 6, 'e_m': 15.096114, 'e_o_k': [11.741422, 9.393138], 'p_i': 80, 'u_i': 3.9709},
        {'id': 7, 'e_m': 8.076896, 'e_o_k': [6.282030, 5.025624], 'p_i': 80, 'u_i': 1.7339},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
