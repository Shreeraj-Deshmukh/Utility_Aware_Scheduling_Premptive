"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280017, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280017, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.276512, 'e_o_k': [0.212752, 0.170202], 'p_i': 10, 'u_i': 4.6027},
        {'id': 1, 'e_m': 5.296550, 'e_o_k': [0.651215, 0.520972, 0.416778], 'p_i': 20, 'u_i': 2.4414},
        {'id': 2, 'e_m': 10.902865, 'e_o_k': [1.817144, 1.453715], 'p_i': 40, 'u_i': 4.2208},
        {'id': 3, 'e_m': 36.060729, 'e_o_k': [6.010121, 4.808097], 'p_i': 80, 'u_i': 1.1145},
        {'id': 4, 'e_m': 13.300582, 'e_o_k': [1.081559, 0.865247, 0.692198, 0.553758, 0.443007, 0.354405], 'p_i': 40, 'u_i': 1.2006},
        {'id': 5, 'e_m': 7.015351, 'e_o_k': [0.712942, 0.570354, 0.456283, 0.365026], 'p_i': 40, 'u_i': 1.8700},
        {'id': 6, 'e_m': 1.610479, 'e_o_k': [0.130959, 0.104767, 0.083814, 0.067051, 0.053641, 0.042913], 'p_i': 10, 'u_i': 3.7146},
        {'id': 7, 'e_m': 0.152444, 'e_o_k': [0.015492, 0.012394, 0.009915, 0.007932], 'p_i': 10, 'u_i': 1.7471},
    ]
    B_BUDGET = 215.280017
    return processors, tasks, B_BUDGET
