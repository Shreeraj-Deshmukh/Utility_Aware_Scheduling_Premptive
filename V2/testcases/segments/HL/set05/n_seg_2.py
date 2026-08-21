"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399986, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399986, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.789693, 'e_o_k': [0.219359, 0.175487], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.245294, 'e_o_k': [0.068137, 0.054510], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 3.310794, 'e_o_k': [0.919665, 0.735732], 'p_i': 40, 'u_i': 2.1879},
        {'id': 3, 'e_m': 1.628519, 'e_o_k': [0.452366, 0.361893], 'p_i': 80, 'u_i': 2.3607},
        {'id': 4, 'e_m': 2.051152, 'e_o_k': [0.569764, 0.455812], 'p_i': 20, 'u_i': 2.0600},
        {'id': 5, 'e_m': 0.110349, 'e_o_k': [0.030653, 0.024522], 'p_i': 80, 'u_i': 2.1803},
        {'id': 6, 'e_m': 3.223708, 'e_o_k': [0.895474, 0.716379], 'p_i': 10, 'u_i': 4.5157},
        {'id': 7, 'e_m': 7.173276, 'e_o_k': [1.992577, 1.594061], 'p_i': 40, 'u_i': 4.4957},
    ]
    B_BUDGET = 110.399986
    return processors, tasks, B_BUDGET
