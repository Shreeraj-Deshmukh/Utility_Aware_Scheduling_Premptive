"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399987, "H": 80, "J": 22, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399987, "H": 80, "J": 22, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.057702, 'e_o_k': [0.014720, 0.008832, 0.005299], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 0.850087, 'e_o_k': [0.265652, 0.159391], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.742953, 'e_o_k': [0.161119, 0.096672, 0.058003, 0.034802, 0.020881], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 7.198095, 'e_o_k': [1.836249, 1.101749, 0.661050], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 10.841114, 'e_o_k': [2.351040, 1.410624, 0.846374, 0.507825, 0.304695], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 30.342716, 'e_o_k': [7.740489, 4.644293, 2.786576], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 1.267486, 'e_o_k': [0.291242, 0.174745, 0.104847, 0.062908], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 5.200256, 'e_o_k': [1.625080, 0.975048], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 110.399987
    return processors, tasks, B_BUDGET
