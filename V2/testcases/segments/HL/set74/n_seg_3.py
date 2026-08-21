"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399984, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399984, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.237773, 'e_o_k': [0.048724, 0.038979, 0.031183], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 2.303196, 'e_o_k': [0.471966, 0.377573, 0.302059], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 7.567437, 'e_o_k': [1.550704, 1.240563, 0.992451], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 20.093036, 'e_o_k': [4.117425, 3.293940, 2.635152], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.219572, 'e_o_k': [0.044994, 0.035995, 0.028796], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 9.972517, 'e_o_k': [2.043549, 1.634839, 1.307871], 'p_i': 80, 'u_i': 1.7696},
        {'id': 6, 'e_m': 3.107005, 'e_o_k': [0.636681, 0.509345, 0.407476], 'p_i': 80, 'u_i': 4.8086},
        {'id': 7, 'e_m': 0.705255, 'e_o_k': [0.144520, 0.115616, 0.092493], 'p_i': 20, 'u_i': 1.4894},
    ]
    B_BUDGET = 110.399984
    return processors, tasks, B_BUDGET
