"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 44.160006, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.4, "seed": 1070, "set": 70, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.40"}
"""

_SPEC = '{"B": 44.160006, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.4, "seed": 1070, "set": 70, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.560596, 'e_o_k': [0.155721, 0.124577], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 2.273229, 'e_o_k': [0.308086, 0.246469, 0.197175, 0.157740, 0.126192, 0.100954], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 5.286614, 'e_o_k': [1.083323, 0.866658, 0.693326], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 1.840129, 'e_o_k': [0.511147, 0.408918], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 0.311968, 'e_o_k': [0.042280, 0.033824, 0.027059, 0.021648, 0.017318, 0.013854], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 1.580366, 'e_o_k': [0.235062, 0.188049, 0.150439, 0.120352, 0.096281], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 2.375437, 'e_o_k': [0.353319, 0.282656, 0.226124, 0.180900, 0.144720], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.040206, 'e_o_k': [0.011168, 0.008935], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 44.160006
    return processors, tasks, B_BUDGET
