"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640012, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640012, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.944372, 'e_o_k': [0.447873, 0.358298, 0.286639, 0.229311], 'p_i': 10, 'u_i': 3.1874},
        {'id': 1, 'e_m': 2.227287, 'e_o_k': [1.732334, 1.385867], 'p_i': 20, 'u_i': 2.4550},
        {'id': 2, 'e_m': 7.236978, 'e_o_k': [4.152364, 3.321891, 2.657513], 'p_i': 40, 'u_i': 4.1368},
        {'id': 3, 'e_m': 0.354839, 'e_o_k': [0.275986, 0.220789], 'p_i': 80, 'u_i': 2.0023},
        {'id': 4, 'e_m': 14.061479, 'e_o_k': [5.856161, 4.684929, 3.747943, 2.998354, 2.398684], 'p_i': 40, 'u_i': 1.7941},
        {'id': 5, 'e_m': 2.292064, 'e_o_k': [0.954572, 0.763658, 0.610926, 0.488741, 0.390993], 'p_i': 40, 'u_i': 1.7354},
    ]
    B_BUDGET = 176.640012
    return processors, tasks, B_BUDGET
