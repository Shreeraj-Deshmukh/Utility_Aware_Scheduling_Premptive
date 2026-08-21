"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.345721, 'e_o_k': [0.198365, 0.158692, 0.126953], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 1.825589, 'e_o_k': [1.047469, 0.837975, 0.670380], 'p_i': 20, 'u_i': 2.2851},
        {'id': 2, 'e_m': 2.684855, 'e_o_k': [1.540491, 1.232392, 0.985914], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 4.826850, 'e_o_k': [2.769504, 2.215603, 1.772483], 'p_i': 80, 'u_i': 2.3867},
        {'id': 4, 'e_m': 0.378406, 'e_o_k': [0.217118, 0.173695, 0.138956], 'p_i': 10, 'u_i': 1.9527},
        {'id': 5, 'e_m': 0.374820, 'e_o_k': [0.215061, 0.172049, 0.137639], 'p_i': 10, 'u_i': 2.5555},
        {'id': 6, 'e_m': 3.374313, 'e_o_k': [1.936081, 1.548865, 1.239092], 'p_i': 80, 'u_i': 2.5749},
        {'id': 7, 'e_m': 1.167596, 'e_o_k': [0.669932, 0.535946, 0.428757], 'p_i': 40, 'u_i': 4.5972},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
