"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.778125, 'e_o_k': [0.178797, 0.107278, 0.064367, 0.038620], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 1.791279, 'e_o_k': [0.375789, 0.225473, 0.135284, 0.081170, 0.048702, 0.029221], 'p_i': 20, 'u_i': 2.0660},
        {'id': 2, 'e_m': 0.021926, 'e_o_k': [0.006852, 0.004111], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 9.810039, 'e_o_k': [2.502561, 1.501537, 0.900922], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 17.706132, 'e_o_k': [4.516870, 2.710122, 1.626073], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.074098, 'e_o_k': [0.017026, 0.010216, 0.006129, 0.003678], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 3.015455, 'e_o_k': [0.653942, 0.392365, 0.235419, 0.141251, 0.084751], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 2.180081, 'e_o_k': [0.500938, 0.300563, 0.180338, 0.108203], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
