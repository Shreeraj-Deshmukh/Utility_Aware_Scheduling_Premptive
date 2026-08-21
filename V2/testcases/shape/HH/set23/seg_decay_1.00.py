"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.778125, 'e_o_k': [0.272344, 0.272344, 0.272344, 0.272344], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 1.791279, 'e_o_k': [0.417965, 0.417965, 0.417965, 0.417965, 0.417965, 0.417965], 'p_i': 20, 'u_i': 2.0660},
        {'id': 2, 'e_m': 0.021926, 'e_o_k': [0.015348, 0.015348], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 9.810039, 'e_o_k': [4.578018, 4.578018, 4.578018], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 17.706132, 'e_o_k': [8.262862, 8.262862, 8.262862], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.074098, 'e_o_k': [0.025934, 0.025934, 0.025934, 0.025934], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 3.015455, 'e_o_k': [0.844327, 0.844327, 0.844327, 0.844327, 0.844327], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 2.180081, 'e_o_k': [0.763028, 0.763028, 0.763028, 0.763028], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET
