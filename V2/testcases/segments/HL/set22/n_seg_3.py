"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.006839, 'e_o_k': [0.411238, 0.328990, 0.263192], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.143860, 'e_o_k': [0.029480, 0.023584, 0.018867], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 4.365284, 'e_o_k': [0.894525, 0.715620, 0.572496], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 1.921148, 'e_o_k': [0.393678, 0.314942, 0.251954], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 3.369376, 'e_o_k': [0.690446, 0.552357, 0.441885], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 1.402420, 'e_o_k': [0.287381, 0.229905, 0.183924], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 6.817126, 'e_o_k': [1.396952, 1.117562, 0.894049], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 2.194072, 'e_o_k': [0.449605, 0.359684, 0.287747], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET
