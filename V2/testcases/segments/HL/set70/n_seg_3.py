"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.121191, 'e_o_k': [0.229752, 0.183802, 0.147041], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 4.546458, 'e_o_k': [0.931651, 0.745321, 0.596257], 'p_i': 20, 'u_i': 4.6519},
        {'id': 2, 'e_m': 10.573229, 'e_o_k': [2.166645, 1.733316, 1.386653], 'p_i': 40, 'u_i': 4.9020},
        {'id': 3, 'e_m': 3.680258, 'e_o_k': [0.754151, 0.603321, 0.482657], 'p_i': 80, 'u_i': 4.4826},
        {'id': 4, 'e_m': 0.623936, 'e_o_k': [0.127856, 0.102285, 0.081828], 'p_i': 80, 'u_i': 1.3844},
        {'id': 5, 'e_m': 3.160733, 'e_o_k': [0.647691, 0.518153, 0.414522], 'p_i': 40, 'u_i': 3.8571},
        {'id': 6, 'e_m': 4.750875, 'e_o_k': [0.973540, 0.778832, 0.623066], 'p_i': 80, 'u_i': 3.6185},
        {'id': 7, 'e_m': 0.080412, 'e_o_k': [0.016478, 0.013182, 0.010546], 'p_i': 20, 'u_i': 1.1495},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
