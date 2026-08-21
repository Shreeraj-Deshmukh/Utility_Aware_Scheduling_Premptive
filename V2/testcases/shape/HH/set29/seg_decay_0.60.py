"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.555176, 'e_o_k': [0.357190, 0.214314, 0.128589, 0.077153], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 0.851460, 'e_o_k': [0.517021, 0.310213, 0.186128, 0.111677, 0.067006], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 3.395703, 'e_o_k': [2.061929, 1.237158, 0.742295, 0.445377, 0.267226], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 3.482314, 'e_o_k': [2.114521, 1.268712, 0.761227, 0.456736, 0.274042], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 4.033383, 'e_o_k': [3.529210, 2.117526], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 2.789347, 'e_o_k': [1.992390, 1.195434, 0.717261], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 3.567276, 'e_o_k': [2.295123, 1.377074, 0.826244, 0.495746], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 3.486046, 'e_o_k': [3.050290, 1.830174], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
