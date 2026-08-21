"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.778125, 'e_o_k': [0.500632, 0.300379, 0.180227, 0.108136], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 1.791279, 'e_o_k': [1.052208, 0.631325, 0.378795, 0.227277, 0.136366, 0.081820], 'p_i': 20, 'u_i': 2.0660},
        {'id': 2, 'e_m': 0.021926, 'e_o_k': [0.019185, 0.011511], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 9.810039, 'e_o_k': [7.007171, 4.204302, 2.522581], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 17.706132, 'e_o_k': [12.647237, 7.588342, 4.553005], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.074098, 'e_o_k': [0.047673, 0.028604, 0.017162, 0.010297], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 3.015455, 'e_o_k': [1.831036, 1.098622, 0.659173, 0.395504, 0.237302], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 2.180081, 'e_o_k': [1.402625, 0.841575, 0.504945, 0.302967], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
