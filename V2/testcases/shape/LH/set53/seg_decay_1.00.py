"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.159031, 'e_o_k': [0.111321, 0.111321], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 1.218826, 'e_o_k': [0.853178, 0.853178], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 0.995792, 'e_o_k': [0.278822, 0.278822, 0.278822, 0.278822, 0.278822], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 5.369863, 'e_o_k': [3.758904, 3.758904], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 0.918489, 'e_o_k': [0.214314, 0.214314, 0.214314, 0.214314, 0.214314, 0.214314], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 0.851463, 'e_o_k': [0.298012, 0.298012, 0.298012, 0.298012], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 1.430219, 'e_o_k': [0.500576, 0.500576, 0.500576, 0.500576], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 4.121451, 'e_o_k': [0.961672, 0.961672, 0.961672, 0.961672, 0.961672, 0.961672], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
