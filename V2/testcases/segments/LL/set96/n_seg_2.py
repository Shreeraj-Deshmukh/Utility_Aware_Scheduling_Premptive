"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.252893, 'e_o_k': [0.070248, 0.056199], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.097609, 'e_o_k': [0.027114, 0.021691], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 5.092114, 'e_o_k': [1.414476, 1.131581], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 3.280589, 'e_o_k': [0.911275, 0.729020], 'p_i': 80, 'u_i': 1.1592},
        {'id': 4, 'e_m': 2.269701, 'e_o_k': [0.630473, 0.504378], 'p_i': 20, 'u_i': 2.2796},
        {'id': 5, 'e_m': 3.382746, 'e_o_k': [0.939652, 0.751721], 'p_i': 80, 'u_i': 4.8637},
        {'id': 6, 'e_m': 0.542314, 'e_o_k': [0.150643, 0.120514], 'p_i': 20, 'u_i': 2.9768},
        {'id': 7, 'e_m': 0.186349, 'e_o_k': [0.051764, 0.041411], 'p_i': 10, 'u_i': 1.8410},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
