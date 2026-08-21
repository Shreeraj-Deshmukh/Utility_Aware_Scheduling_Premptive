"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.318061, 'e_o_k': [0.088350, 0.070680], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 2.437651, 'e_o_k': [0.677125, 0.541700], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 1.991584, 'e_o_k': [0.553218, 0.442574], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 10.739727, 'e_o_k': [2.983257, 2.386606], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 1.836977, 'e_o_k': [0.510271, 0.408217], 'p_i': 40, 'u_i': 4.0720},
        {'id': 5, 'e_m': 1.702926, 'e_o_k': [0.473035, 0.378428], 'p_i': 10, 'u_i': 3.0767},
        {'id': 6, 'e_m': 2.860437, 'e_o_k': [0.794566, 0.635653], 'p_i': 20, 'u_i': 2.4479},
        {'id': 7, 'e_m': 8.242902, 'e_o_k': [2.289695, 1.831756], 'p_i': 80, 'u_i': 3.0328},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET
