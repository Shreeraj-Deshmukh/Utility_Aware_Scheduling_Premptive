"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 43, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 43, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.834237, 'e_o_k': [0.231732, 0.185386], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 2.062949, 'e_o_k': [0.422735, 0.338188, 0.270551], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 2.169279, 'e_o_k': [0.602577, 0.482062], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 13.026985, 'e_o_k': [2.206468, 1.765174, 1.412139, 1.129711], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.281506, 'e_o_k': [0.078196, 0.062557], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 1.211718, 'e_o_k': [0.205237, 0.164189, 0.131352, 0.105081], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 1.184948, 'e_o_k': [0.242817, 0.194254, 0.155403], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 1.426177, 'e_o_k': [0.292249, 0.233800, 0.187040], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
