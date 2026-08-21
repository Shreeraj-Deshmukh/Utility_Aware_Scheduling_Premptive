"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 52.255999, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.3, "seed": 1048, "set": 48, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.30"}
"""

_SPEC = '{"B": 52.255999, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.3, "seed": 1048, "set": 48, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.686006, 'e_o_k': [0.533560, 0.426848], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 1.744166, 'e_o_k': [1.000751, 0.800601, 0.640481], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.047982, 'e_o_k': [0.027531, 0.022025, 0.017620], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 1.929764, 'e_o_k': [1.500928, 1.200742], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 5.818863, 'e_o_k': [4.525782, 3.620626], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 1.092627, 'e_o_k': [0.455044, 0.364036, 0.291228, 0.232983, 0.186386], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 0.842076, 'e_o_k': [0.350698, 0.280558, 0.224447, 0.179557, 0.143646], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 0.583581, 'e_o_k': [0.243043, 0.194435, 0.155548, 0.124438, 0.099550], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 52.255999
    return processors, tasks, B_BUDGET
