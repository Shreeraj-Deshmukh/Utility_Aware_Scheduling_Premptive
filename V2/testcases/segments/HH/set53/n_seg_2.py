"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.318061, 'e_o_k': [0.247381, 0.197905], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 2.437651, 'e_o_k': [1.895951, 1.516761], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 1.991584, 'e_o_k': [1.549010, 1.239208], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 10.739727, 'e_o_k': [8.353121, 6.682497], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 1.836977, 'e_o_k': [1.428760, 1.143008], 'p_i': 40, 'u_i': 4.0720},
        {'id': 5, 'e_m': 1.702926, 'e_o_k': [1.324498, 1.059598], 'p_i': 10, 'u_i': 3.0767},
        {'id': 6, 'e_m': 2.860437, 'e_o_k': [2.224784, 1.779827], 'p_i': 20, 'u_i': 2.4479},
        {'id': 7, 'e_m': 8.242902, 'e_o_k': [6.411146, 5.128917], 'p_i': 80, 'u_i': 3.0328},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
