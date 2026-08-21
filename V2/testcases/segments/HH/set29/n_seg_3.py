"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.555176, 'e_o_k': [0.318544, 0.254835, 0.203868], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 0.851460, 'e_o_k': [0.488543, 0.390834, 0.312667], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 3.395703, 'e_o_k': [1.948354, 1.558683, 1.246947], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 3.482314, 'e_o_k': [1.998049, 1.598439, 1.278751], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 4.033383, 'e_o_k': [2.314236, 1.851389, 1.481111], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 2.789347, 'e_o_k': [1.600445, 1.280356, 1.024285], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 3.567276, 'e_o_k': [2.046798, 1.637438, 1.309951], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 3.486046, 'e_o_k': [2.000190, 1.600152, 1.280122], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
