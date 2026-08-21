"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.219440, 'e_o_k': [0.036573, 0.036573, 0.036573], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 1.145357, 'e_o_k': [0.095446, 0.095446, 0.095446, 0.095446, 0.095446, 0.095446], 'p_i': 20, 'u_i': 2.8306},
        {'id': 2, 'e_m': 11.261726, 'e_o_k': [1.876954, 1.876954, 1.876954], 'p_i': 40, 'u_i': 2.9234},
        {'id': 3, 'e_m': 7.430483, 'e_o_k': [1.238414, 1.238414, 1.238414], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 2.663123, 'e_o_k': [0.443854, 0.443854, 0.443854], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 3.271381, 'e_o_k': [0.817845, 0.817845], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.028377, 'e_o_k': [0.002365, 0.002365, 0.002365, 0.002365, 0.002365, 0.002365], 'p_i': 40, 'u_i': 4.5772},
        {'id': 7, 'e_m': 1.307139, 'e_o_k': [0.130714, 0.130714, 0.130714, 0.130714, 0.130714], 'p_i': 10, 'u_i': 4.4816},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET
