"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.533877, 'e_o_k': [0.253194, 0.202555, 0.162044, 0.129635], 'p_i': 10, 'u_i': 2.4700},
        {'id': 1, 'e_m': 1.248730, 'e_o_k': [0.520057, 0.416045, 0.332836, 0.266269, 0.213015], 'p_i': 20, 'u_i': 2.1021},
        {'id': 2, 'e_m': 0.016411, 'e_o_k': [0.006227, 0.004982, 0.003986, 0.003188, 0.002551, 0.002041], 'p_i': 40, 'u_i': 2.0660},
        {'id': 3, 'e_m': 7.953863, 'e_o_k': [6.186338, 4.949070], 'p_i': 80, 'u_i': 3.5059},
        {'id': 4, 'e_m': 14.714138, 'e_o_k': [8.442538, 6.754031, 5.403224], 'p_i': 80, 'u_i': 1.7742},
        {'id': 5, 'e_m': 0.016621, 'e_o_k': [0.009536, 0.007629, 0.006103], 'p_i': 40, 'u_i': 1.4108},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
