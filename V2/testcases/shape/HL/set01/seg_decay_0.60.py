"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255642, 'e_o_k': [0.053631, 0.032178, 0.019307, 0.011584, 0.006951, 0.004170], 'p_i': 10, 'u_i': 4.5169},
        {'id': 1, 'e_m': 5.834936, 'e_o_k': [1.823417, 1.094050], 'p_i': 20, 'u_i': 3.9484},
        {'id': 2, 'e_m': 1.030030, 'e_o_k': [0.223376, 0.134025, 0.080415, 0.048249, 0.028949], 'p_i': 40, 'u_i': 3.8598},
        {'id': 3, 'e_m': 1.325038, 'e_o_k': [0.277977, 0.166786, 0.100072, 0.060043, 0.036026, 0.021615], 'p_i': 80, 'u_i': 3.9484},
        {'id': 4, 'e_m': 19.367876, 'e_o_k': [4.940785, 2.964471, 1.778682], 'p_i': 80, 'u_i': 4.6365},
        {'id': 5, 'e_m': 0.396585, 'e_o_k': [0.083199, 0.049919, 0.029952, 0.017971, 0.010783, 0.006470], 'p_i': 40, 'u_i': 4.7054},
        {'id': 6, 'e_m': 3.226328, 'e_o_k': [1.008227, 0.604936], 'p_i': 80, 'u_i': 3.2554},
        {'id': 7, 'e_m': 2.960663, 'e_o_k': [0.925207, 0.555124], 'p_i': 20, 'u_i': 3.5452},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
