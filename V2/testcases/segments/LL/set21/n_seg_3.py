"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199986, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199986, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.345721, 'e_o_k': [0.070844, 0.056676, 0.045340], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 1.825589, 'e_o_k': [0.374096, 0.299277, 0.239421], 'p_i': 20, 'u_i': 2.2851},
        {'id': 2, 'e_m': 2.684855, 'e_o_k': [0.550175, 0.440140, 0.352112], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 4.826850, 'e_o_k': [0.989109, 0.791287, 0.633030], 'p_i': 80, 'u_i': 2.3867},
        {'id': 4, 'e_m': 0.378406, 'e_o_k': [0.077542, 0.062034, 0.049627], 'p_i': 10, 'u_i': 1.9527},
        {'id': 5, 'e_m': 0.374820, 'e_o_k': [0.076807, 0.061446, 0.049157], 'p_i': 10, 'u_i': 2.5555},
        {'id': 6, 'e_m': 3.374313, 'e_o_k': [0.691458, 0.553166, 0.442533], 'p_i': 80, 'u_i': 2.5749},
        {'id': 7, 'e_m': 1.167596, 'e_o_k': [0.239261, 0.191409, 0.153127], 'p_i': 40, 'u_i': 4.5972},
    ]
    B_BUDGET = 55.199986
    return processors, tasks, B_BUDGET
