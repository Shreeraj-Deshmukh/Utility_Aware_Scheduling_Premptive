"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 117.759998, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.2, "seed": 1029, "set": 29, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.20"}
"""

_SPEC = '{"B": 117.759998, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.2, "seed": 1029, "set": 29, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.20"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.555176, 'e_o_k': [0.094034, 0.075227, 0.060182, 0.048145], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 0.851460, 'e_o_k': [0.126645, 0.101316, 0.081053, 0.064842, 0.051874], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 3.395703, 'e_o_k': [0.505072, 0.404058, 0.323246, 0.258597, 0.206878], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 3.482314, 'e_o_k': [0.517955, 0.414364, 0.331491, 0.265193, 0.212154], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 4.033383, 'e_o_k': [1.120384, 0.896307], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 2.789347, 'e_o_k': [0.571587, 0.457270, 0.365816], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 3.567276, 'e_o_k': [0.604213, 0.483371, 0.386697, 0.309357], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 3.486046, 'e_o_k': [0.968346, 0.774677], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 117.759998
    return processors, tasks, B_BUDGET
