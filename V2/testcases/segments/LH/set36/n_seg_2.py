"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471162, 'e_o_k': [0.366459, 0.293168], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.359296, 'e_o_k': [0.279452, 0.223562], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.377372, 'e_o_k': [0.293512, 0.234809], 'p_i': 40, 'u_i': 4.4037},
        {'id': 3, 'e_m': 2.056648, 'e_o_k': [1.599615, 1.279692], 'p_i': 80, 'u_i': 1.7011},
        {'id': 4, 'e_m': 7.946467, 'e_o_k': [6.180586, 4.944469], 'p_i': 40, 'u_i': 1.8442},
        {'id': 5, 'e_m': 1.594191, 'e_o_k': [1.239926, 0.991941], 'p_i': 40, 'u_i': 2.3108},
        {'id': 6, 'e_m': 0.525986, 'e_o_k': [0.409101, 0.327280], 'p_i': 10, 'u_i': 1.0383},
        {'id': 7, 'e_m': 0.346460, 'e_o_k': [0.269469, 0.215575], 'p_i': 40, 'u_i': 2.0614},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
