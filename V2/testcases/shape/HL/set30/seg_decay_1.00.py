"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.049022, 'e_o_k': [0.008170, 0.008170, 0.008170], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 2.109402, 'e_o_k': [0.175784, 0.175784, 0.175784, 0.175784, 0.175784, 0.175784], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 2.697147, 'e_o_k': [0.674287, 0.674287], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 4.992978, 'e_o_k': [0.624122, 0.624122, 0.624122, 0.624122], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 19.099547, 'e_o_k': [2.387443, 2.387443, 2.387443, 2.387443], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.082986, 'e_o_k': [0.010373, 0.010373, 0.010373, 0.010373], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 1.458740, 'e_o_k': [0.182342, 0.182342, 0.182342, 0.182342], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 5.890191, 'e_o_k': [0.981699, 0.981699, 0.981699], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
