"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.996752, 'e_o_k': [0.204252, 0.163402, 0.130722], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 0.594019, 'e_o_k': [0.121725, 0.097380, 0.077904], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 1.782547, 'e_o_k': [0.365276, 0.292221, 0.233777], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 4.659020, 'e_o_k': [0.954717, 0.763774, 0.611019], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 0.874227, 'e_o_k': [0.179145, 0.143316, 0.114653], 'p_i': 20, 'u_i': 2.4561},
        {'id': 5, 'e_m': 18.325230, 'e_o_k': [3.755170, 3.004136, 2.403309], 'p_i': 80, 'u_i': 1.8035},
        {'id': 6, 'e_m': 1.553215, 'e_o_k': [0.318282, 0.254625, 0.203700], 'p_i': 20, 'u_i': 3.4846},
        {'id': 7, 'e_m': 2.173850, 'e_o_k': [0.445461, 0.356369, 0.285095], 'p_i': 10, 'u_i': 2.9402},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
