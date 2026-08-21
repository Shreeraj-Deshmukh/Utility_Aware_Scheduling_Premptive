"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760003, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760003, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.172830, 'e_o_k': [0.014054, 0.011243, 0.008995, 0.007196, 0.005756, 0.004605], 'p_i': 10, 'u_i': 2.8095},
        {'id': 1, 'e_m': 1.290528, 'e_o_k': [0.158671, 0.126937, 0.101550], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 3.560367, 'e_o_k': [0.317739, 0.254191, 0.203353, 0.162682, 0.130146], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 4.116745, 'e_o_k': [0.506157, 0.404926, 0.323941], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 1.970951, 'e_o_k': [0.175894, 0.140715, 0.112572, 0.090058, 0.072046], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 1.520104, 'e_o_k': [0.135659, 0.108527, 0.086822, 0.069457, 0.055566], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 9.244228, 'e_o_k': [0.824985, 0.659988, 0.527990, 0.422392, 0.337914], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 0.928909, 'e_o_k': [0.114210, 0.091368, 0.073094], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 71.760003
    return processors, tasks, B_BUDGET
