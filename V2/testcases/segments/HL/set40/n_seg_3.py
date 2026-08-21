"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.249202, 'e_o_k': [0.255984, 0.204787, 0.163830], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 1.221788, 'e_o_k': [0.250366, 0.200293, 0.160234], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 6.176629, 'e_o_k': [1.265703, 1.012562, 0.810050], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 8.093637, 'e_o_k': [1.658532, 1.326826, 1.061461], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 0.742083, 'e_o_k': [0.152066, 0.121653, 0.097322], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 6.497443, 'e_o_k': [1.331443, 1.065155, 0.852124], 'p_i': 40, 'u_i': 2.6468},
        {'id': 6, 'e_m': 0.756149, 'e_o_k': [0.154949, 0.123959, 0.099167], 'p_i': 20, 'u_i': 2.0597},
        {'id': 7, 'e_m': 11.168684, 'e_o_k': [2.288665, 1.830932, 1.464745], 'p_i': 80, 'u_i': 3.8347},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
