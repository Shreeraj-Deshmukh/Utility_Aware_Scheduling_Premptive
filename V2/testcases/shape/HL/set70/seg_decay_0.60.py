"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.121191, 'e_o_k': [0.350372, 0.210223], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 4.546458, 'e_o_k': [0.953792, 0.572275, 0.343365, 0.206019, 0.123611, 0.074167], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 10.573229, 'e_o_k': [2.697252, 1.618351, 0.971011], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 3.680258, 'e_o_k': [1.150081, 0.690048], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 0.623936, 'e_o_k': [0.130894, 0.078537, 0.047122, 0.028273, 0.016964, 0.010178], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 3.160733, 'e_o_k': [0.685447, 0.411268, 0.246761, 0.148057, 0.088834], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 4.750875, 'e_o_k': [1.030290, 0.618174, 0.370905, 0.222543, 0.133526], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.080412, 'e_o_k': [0.025129, 0.015077], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
