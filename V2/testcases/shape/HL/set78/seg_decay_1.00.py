"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 26, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 26, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.286440, 'e_o_k': [0.285805, 0.285805, 0.285805, 0.285805], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 1.443240, 'e_o_k': [0.144324, 0.144324, 0.144324, 0.144324, 0.144324], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 1.122430, 'e_o_k': [0.280608, 0.280608], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 19.814276, 'e_o_k': [2.476785, 2.476785, 2.476785, 2.476785], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 1.849800, 'e_o_k': [0.462450, 0.462450], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 2.622764, 'e_o_k': [0.655691, 0.655691], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.305518, 'e_o_k': [0.076380, 0.076380], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 2.463653, 'e_o_k': [0.307957, 0.307957, 0.307957, 0.307957], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
