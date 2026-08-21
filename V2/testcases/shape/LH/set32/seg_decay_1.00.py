"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.507641, 'e_o_k': [0.142140, 0.142140, 0.142140, 0.142140, 0.142140], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 0.669069, 'e_o_k': [0.156116, 0.156116, 0.156116, 0.156116, 0.156116, 0.156116], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 0.607685, 'e_o_k': [0.141793, 0.141793, 0.141793, 0.141793, 0.141793, 0.141793], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 5.713737, 'e_o_k': [3.999616, 3.999616], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 2.096375, 'e_o_k': [0.733731, 0.733731, 0.733731, 0.733731], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.270524, 'e_o_k': [0.094683, 0.094683, 0.094683, 0.094683], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 2.830351, 'e_o_k': [1.981245, 1.981245], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.327572, 'e_o_k': [0.229300, 0.229300], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
