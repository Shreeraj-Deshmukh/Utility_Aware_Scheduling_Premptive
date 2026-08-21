"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399986, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399986, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.282719, 'e_o_k': [0.057934, 0.046347, 0.037078], 'p_i': 10, 'u_i': 4.9222},
        {'id': 1, 'e_m': 0.997197, 'e_o_k': [0.204344, 0.163475, 0.130780], 'p_i': 20, 'u_i': 1.9107},
        {'id': 2, 'e_m': 10.687466, 'e_o_k': [2.190055, 1.752044, 1.401635], 'p_i': 40, 'u_i': 1.7322},
        {'id': 3, 'e_m': 8.337500, 'e_o_k': [1.708504, 1.366803, 1.093443], 'p_i': 80, 'u_i': 1.5709},
        {'id': 4, 'e_m': 1.567672, 'e_o_k': [0.321244, 0.256995, 0.205596], 'p_i': 20, 'u_i': 3.7661},
        {'id': 5, 'e_m': 1.462585, 'e_o_k': [0.299710, 0.239768, 0.191814], 'p_i': 20, 'u_i': 1.0932},
        {'id': 6, 'e_m': 0.086308, 'e_o_k': [0.017686, 0.014149, 0.011319], 'p_i': 20, 'u_i': 3.8665},
        {'id': 7, 'e_m': 7.785382, 'e_o_k': [1.595365, 1.276292, 1.021034], 'p_i': 40, 'u_i': 4.9324},
    ]
    B_BUDGET = 110.399986
    return processors, tasks, B_BUDGET
