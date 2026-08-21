"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.443224, 'e_o_k': [0.075072, 0.060057, 0.048046, 0.038437], 'p_i': 10, 'u_i': 2.5678},
        {'id': 1, 'e_m': 0.385037, 'e_o_k': [0.065216, 0.052173, 0.041738, 0.033391], 'p_i': 20, 'u_i': 3.0744},
        {'id': 2, 'e_m': 7.186952, 'e_o_k': [1.217302, 0.973842, 0.779073, 0.623259], 'p_i': 40, 'u_i': 3.1102},
        {'id': 3, 'e_m': 20.620712, 'e_o_k': [3.492668, 2.794134, 2.235308, 1.788246], 'p_i': 80, 'u_i': 3.9862},
        {'id': 4, 'e_m': 1.451540, 'e_o_k': [0.245857, 0.196686, 0.157349, 0.125879], 'p_i': 20, 'u_i': 1.5757},
        {'id': 5, 'e_m': 1.346300, 'e_o_k': [0.228032, 0.182425, 0.145940, 0.116752], 'p_i': 10, 'u_i': 4.9941},
        {'id': 6, 'e_m': 2.067937, 'e_o_k': [0.350260, 0.280208, 0.224167, 0.179333], 'p_i': 40, 'u_i': 1.7632},
        {'id': 7, 'e_m': 1.603507, 'e_o_k': [0.271597, 0.217277, 0.173822, 0.139058], 'p_i': 40, 'u_i': 1.4284},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
