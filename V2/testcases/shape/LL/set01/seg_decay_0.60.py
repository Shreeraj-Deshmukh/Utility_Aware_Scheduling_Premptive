"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127821, 'e_o_k': [0.026815, 0.016089, 0.009654, 0.005792, 0.003475, 0.002085], 'p_i': 10, 'u_i': 4.5169},
        {'id': 1, 'e_m': 2.917468, 'e_o_k': [0.911709, 0.547025], 'p_i': 20, 'u_i': 3.9484},
        {'id': 2, 'e_m': 0.515015, 'e_o_k': [0.111688, 0.067013, 0.040208, 0.024125, 0.014475], 'p_i': 40, 'u_i': 3.8598},
        {'id': 3, 'e_m': 0.662519, 'e_o_k': [0.138988, 0.083393, 0.050036, 0.030021, 0.018013, 0.010808], 'p_i': 80, 'u_i': 3.9484},
        {'id': 4, 'e_m': 9.683938, 'e_o_k': [2.470392, 1.482235, 0.889341], 'p_i': 80, 'u_i': 4.6365},
        {'id': 5, 'e_m': 0.198293, 'e_o_k': [0.041599, 0.024960, 0.014976, 0.008985, 0.005391, 0.003235], 'p_i': 40, 'u_i': 4.7054},
        {'id': 6, 'e_m': 1.613164, 'e_o_k': [0.504114, 0.302468], 'p_i': 80, 'u_i': 3.2554},
        {'id': 7, 'e_m': 1.480331, 'e_o_k': [0.462604, 0.277562], 'p_i': 20, 'u_i': 3.5452},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
