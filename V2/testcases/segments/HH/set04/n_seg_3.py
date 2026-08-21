"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.929756, 'e_o_k': [0.533467, 0.426773, 0.341419], 'p_i': 10, 'u_i': 1.2748},
        {'id': 1, 'e_m': 0.056878, 'e_o_k': [0.032635, 0.026108, 0.020886], 'p_i': 20, 'u_i': 3.8825},
        {'id': 2, 'e_m': 2.623994, 'e_o_k': [1.505570, 1.204456, 0.963565], 'p_i': 40, 'u_i': 3.8582},
        {'id': 3, 'e_m': 4.474673, 'e_o_k': [2.567435, 2.053948, 1.643159], 'p_i': 80, 'u_i': 1.6137},
        {'id': 4, 'e_m': 2.349668, 'e_o_k': [1.348170, 1.078536, 0.862829], 'p_i': 20, 'u_i': 2.7253},
        {'id': 5, 'e_m': 10.542988, 'e_o_k': [6.049256, 4.839405, 3.871524], 'p_i': 40, 'u_i': 1.4714},
        {'id': 6, 'e_m': 0.342456, 'e_o_k': [0.196491, 0.157193, 0.125754], 'p_i': 10, 'u_i': 2.9160},
        {'id': 7, 'e_m': 3.346871, 'e_o_k': [1.920336, 1.536269, 1.229015], 'p_i': 20, 'u_i': 4.4871},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
