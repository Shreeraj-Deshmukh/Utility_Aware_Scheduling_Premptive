"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760014, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760014, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.606014, 'e_o_k': [0.049279, 0.039423, 0.031539, 0.025231, 0.020185, 0.016148], 'p_i': 10, 'u_i': 2.7135},
        {'id': 1, 'e_m': 1.968514, 'e_o_k': [0.160073, 0.128058, 0.102447, 0.081957, 0.065566, 0.052453], 'p_i': 20, 'u_i': 1.9259},
        {'id': 2, 'e_m': 2.275441, 'e_o_k': [0.231244, 0.184995, 0.147996, 0.118397], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 15.105743, 'e_o_k': [1.348085, 1.078468, 0.862774, 0.690220, 0.552176], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 1.624270, 'e_o_k': [0.199705, 0.159764, 0.127811], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.102070, 'e_o_k': [0.010373, 0.008298, 0.006639, 0.005311], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 2.906857, 'e_o_k': [0.295412, 0.236330, 0.189064, 0.151251], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.362767, 'e_o_k': [0.036867, 0.029493, 0.023595, 0.018876], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 71.760014
    return processors, tasks, B_BUDGET
