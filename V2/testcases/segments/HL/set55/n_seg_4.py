"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.362417, 'e_o_k': [0.400138, 0.320111, 0.256089, 0.204871], 'p_i': 10, 'u_i': 4.5874},
        {'id': 1, 'e_m': 1.818372, 'e_o_k': [0.307990, 0.246392, 0.197113, 0.157691], 'p_i': 20, 'u_i': 2.7347},
        {'id': 2, 'e_m': 2.018400, 'e_o_k': [0.341870, 0.273496, 0.218797, 0.175037], 'p_i': 40, 'u_i': 4.9671},
        {'id': 3, 'e_m': 10.977605, 'e_o_k': [1.859350, 1.487480, 1.189984, 0.951987], 'p_i': 80, 'u_i': 4.8761},
        {'id': 4, 'e_m': 5.439997, 'e_o_k': [0.921409, 0.737127, 0.589702, 0.471761], 'p_i': 80, 'u_i': 2.5248},
        {'id': 5, 'e_m': 0.284101, 'e_o_k': [0.048120, 0.038496, 0.030797, 0.024638], 'p_i': 10, 'u_i': 4.9532},
        {'id': 6, 'e_m': 1.455737, 'e_o_k': [0.246568, 0.197254, 0.157804, 0.126243], 'p_i': 40, 'u_i': 2.2979},
        {'id': 7, 'e_m': 6.094243, 'e_o_k': [1.032223, 0.825778, 0.660623, 0.528498], 'p_i': 40, 'u_i': 4.0423},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
