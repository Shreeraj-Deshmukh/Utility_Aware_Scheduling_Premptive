"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360002, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360002, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.351843, 'e_o_k': [0.725307, 0.580246], 'p_i': 10, 'u_i': 2.8688},
        {'id': 1, 'e_m': 2.116582, 'e_o_k': [0.352764, 0.282211], 'p_i': 20, 'u_i': 1.9991},
        {'id': 2, 'e_m': 5.936144, 'e_o_k': [0.603267, 0.482613, 0.386091, 0.308873], 'p_i': 40, 'u_i': 2.9592},
        {'id': 3, 'e_m': 6.018350, 'e_o_k': [0.489392, 0.391514, 0.313211, 0.250569, 0.200455, 0.160364], 'p_i': 80, 'u_i': 1.9155},
        {'id': 4, 'e_m': 4.280662, 'e_o_k': [0.435027, 0.348021, 0.278417, 0.222734], 'p_i': 20, 'u_i': 1.4935},
        {'id': 5, 'e_m': 10.154828, 'e_o_k': [1.248544, 0.998836, 0.799068], 'p_i': 40, 'u_i': 1.7848},
        {'id': 6, 'e_m': 9.980284, 'e_o_k': [0.890673, 0.712538, 0.570030, 0.456024, 0.364820], 'p_i': 80, 'u_i': 3.9231},
        {'id': 7, 'e_m': 9.707850, 'e_o_k': [0.986570, 0.789256, 0.631405, 0.505124], 'p_i': 40, 'u_i': 3.8764},
    ]
    B_BUDGET = 191.360002
    return processors, tasks, B_BUDGET
