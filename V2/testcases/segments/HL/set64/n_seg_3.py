"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400014, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400014, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.443349, 'e_o_k': [0.295768, 0.236615, 0.189292], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 4.992277, 'e_o_k': [1.023008, 0.818406, 0.654725], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 1.773001, 'e_o_k': [0.363320, 0.290656, 0.232525], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 4.820922, 'e_o_k': [0.987894, 0.790315, 0.632252], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 5.896724, 'e_o_k': [1.208345, 0.966676, 0.773341], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 9.193774, 'e_o_k': [1.883970, 1.507176, 1.205741], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.009519, 'e_o_k': [0.001951, 0.001560, 0.001248], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 0.777730, 'e_o_k': [0.159371, 0.127497, 0.101997], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 110.400014
    return processors, tasks, B_BUDGET
