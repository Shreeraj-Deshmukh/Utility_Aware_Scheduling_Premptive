"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.680163, 'e_o_k': [0.139378, 0.111502, 0.089202], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 1.689853, 'e_o_k': [0.346281, 0.277025, 0.221620], 'p_i': 20, 'u_i': 2.4171},
        {'id': 2, 'e_m': 0.519615, 'e_o_k': [0.106479, 0.085183, 0.068146], 'p_i': 40, 'u_i': 4.5639},
        {'id': 3, 'e_m': 18.094462, 'e_o_k': [3.707881, 2.966305, 2.373044], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 5.009794, 'e_o_k': [1.026597, 0.821278, 0.657022], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 1.955931, 'e_o_k': [0.400806, 0.320644, 0.256516], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 10.750512, 'e_o_k': [2.202974, 1.762379, 1.409903], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 4.198837, 'e_o_k': [0.860417, 0.688334, 0.550667], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET
