"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 43, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 43, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.834237, 'e_o_k': [0.170950, 0.136760, 0.109408], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 2.062949, 'e_o_k': [0.422735, 0.338188, 0.270551], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 2.169279, 'e_o_k': [0.444524, 0.355619, 0.284496], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 13.026985, 'e_o_k': [2.669464, 2.135571, 1.708457], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.281506, 'e_o_k': [0.057686, 0.046149, 0.036919], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 1.211718, 'e_o_k': [0.248303, 0.198642, 0.158914], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 1.184948, 'e_o_k': [0.242817, 0.194254, 0.155403], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 1.426177, 'e_o_k': [0.292249, 0.233800, 0.187040], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
