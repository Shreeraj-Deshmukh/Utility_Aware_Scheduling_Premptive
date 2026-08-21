"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.799720, 'e_o_k': [0.249913, 0.149948], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 2.592762, 'e_o_k': [0.661419, 0.396851, 0.238111], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 1.461112, 'e_o_k': [0.335733, 0.201440, 0.120864, 0.072518], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 3.792245, 'e_o_k': [1.185077, 0.711046], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 0.519494, 'e_o_k': [0.108983, 0.065390, 0.039234, 0.023540, 0.014124, 0.008475], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 0.710845, 'e_o_k': [0.149127, 0.089476, 0.053686, 0.032211, 0.019327, 0.011596], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 1.584893, 'e_o_k': [0.495279, 0.297167], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.183071, 'e_o_k': [0.046702, 0.028021, 0.016813], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET
