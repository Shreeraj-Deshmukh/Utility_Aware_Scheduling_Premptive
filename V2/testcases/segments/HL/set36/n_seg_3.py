"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.942324, 'e_o_k': [0.193099, 0.154479, 0.123583], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.718592, 'e_o_k': [0.147252, 0.117802, 0.094242], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.754744, 'e_o_k': [0.154661, 0.123729, 0.098983], 'p_i': 40, 'u_i': 4.4037},
        {'id': 3, 'e_m': 4.113295, 'e_o_k': [0.842888, 0.674311, 0.539449], 'p_i': 80, 'u_i': 1.7011},
        {'id': 4, 'e_m': 15.892935, 'e_o_k': [3.256749, 2.605399, 2.084319], 'p_i': 40, 'u_i': 1.8442},
        {'id': 5, 'e_m': 3.188381, 'e_o_k': [0.653357, 0.522685, 0.418148], 'p_i': 40, 'u_i': 2.3108},
        {'id': 6, 'e_m': 1.051973, 'e_o_k': [0.215568, 0.172455, 0.137964], 'p_i': 10, 'u_i': 1.0383},
        {'id': 7, 'e_m': 0.692921, 'e_o_k': [0.141992, 0.113594, 0.090875], 'p_i': 40, 'u_i': 2.0614},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
