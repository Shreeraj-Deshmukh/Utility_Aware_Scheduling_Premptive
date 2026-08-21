"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399987, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399987, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.686544, 'e_o_k': [0.190707, 0.152565], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 1.582739, 'e_o_k': [0.439650, 0.351720], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 5.107137, 'e_o_k': [1.418649, 1.134919], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.225789, 'e_o_k': [0.062719, 0.050175], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 10.028404, 'e_o_k': [2.785668, 2.228534], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 5.390837, 'e_o_k': [1.497455, 1.197964], 'p_i': 40, 'u_i': 3.9189},
        {'id': 6, 'e_m': 0.266387, 'e_o_k': [0.073996, 0.059197], 'p_i': 10, 'u_i': 2.1344},
        {'id': 7, 'e_m': 4.383523, 'e_o_k': [1.217645, 0.974116], 'p_i': 40, 'u_i': 2.5225},
    ]
    B_BUDGET = 110.399987
    return processors, tasks, B_BUDGET
