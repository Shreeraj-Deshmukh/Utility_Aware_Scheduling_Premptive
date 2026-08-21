"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.647287, 'e_o_k': [0.345581, 0.207348, 0.124409, 0.074645, 0.044787, 0.026872], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.034300, 'e_o_k': [0.007882, 0.004729, 0.002837, 0.001702], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 2.925892, 'e_o_k': [0.914341, 0.548605], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 1.655242, 'e_o_k': [0.422255, 0.253353, 0.152012], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 0.978124, 'e_o_k': [0.212119, 0.127272, 0.076363, 0.045818, 0.027491], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 1.868312, 'e_o_k': [0.429300, 0.257580, 0.154548, 0.092729], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 15.433016, 'e_o_k': [3.546189, 2.127714, 1.276628, 0.765977], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 10.047671, 'e_o_k': [2.563181, 1.537909, 0.922745], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
