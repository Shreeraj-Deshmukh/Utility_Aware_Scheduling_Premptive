"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.713852, 'e_o_k': [0.555218, 0.444174], 'p_i': 10, 'u_i': 2.0315},
        {'id': 1, 'e_m': 0.102835, 'e_o_k': [0.079982, 0.063986], 'p_i': 20, 'u_i': 1.5871},
        {'id': 2, 'e_m': 5.612205, 'e_o_k': [4.365049, 3.492039], 'p_i': 40, 'u_i': 1.8711},
        {'id': 3, 'e_m': 3.855748, 'e_o_k': [2.998915, 2.399132], 'p_i': 80, 'u_i': 4.9538},
        {'id': 4, 'e_m': 0.273644, 'e_o_k': [0.212834, 0.170267], 'p_i': 20, 'u_i': 2.3994},
        {'id': 5, 'e_m': 4.043450, 'e_o_k': [3.144906, 2.515925], 'p_i': 10, 'u_i': 1.5904},
        {'id': 6, 'e_m': 1.584227, 'e_o_k': [1.232177, 0.985741], 'p_i': 40, 'u_i': 2.4893},
        {'id': 7, 'e_m': 0.773382, 'e_o_k': [0.601520, 0.481216], 'p_i': 10, 'u_i': 4.7173},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
