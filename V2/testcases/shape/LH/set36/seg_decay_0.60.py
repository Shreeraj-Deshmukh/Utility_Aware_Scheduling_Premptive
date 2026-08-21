"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471162, 'e_o_k': [0.286098, 0.171659, 0.102995, 0.061797, 0.037078], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.359296, 'e_o_k': [0.256640, 0.153984, 0.092390], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.377372, 'e_o_k': [0.221671, 0.133002, 0.079801, 0.047881, 0.028729, 0.017237], 'p_i': 40, 'u_i': 1.5166},
        {'id': 3, 'e_m': 2.056648, 'e_o_k': [1.799567, 1.079740], 'p_i': 80, 'u_i': 1.2517},
        {'id': 4, 'e_m': 7.946467, 'e_o_k': [5.112617, 3.067570, 1.840542, 1.104325], 'p_i': 40, 'u_i': 3.8216},
        {'id': 5, 'e_m': 1.594191, 'e_o_k': [1.138708, 0.683225, 0.409935], 'p_i': 40, 'u_i': 4.3612},
        {'id': 6, 'e_m': 0.525986, 'e_o_k': [0.338410, 0.203046, 0.121828, 0.073097], 'p_i': 10, 'u_i': 2.3108},
        {'id': 7, 'e_m': 0.346460, 'e_o_k': [0.222906, 0.133744, 0.080246, 0.048148], 'p_i': 40, 'u_i': 1.0383},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
