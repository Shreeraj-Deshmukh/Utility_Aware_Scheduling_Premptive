"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319992, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319992, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.109720, 'e_o_k': [0.078371, 0.047023, 0.028214], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 0.572679, 'e_o_k': [0.336395, 0.201837, 0.121102, 0.072661, 0.043597, 0.026158], 'p_i': 20, 'u_i': 2.8306},
        {'id': 2, 'e_m': 5.630863, 'e_o_k': [4.022045, 2.413227, 1.447936], 'p_i': 40, 'u_i': 2.9234},
        {'id': 3, 'e_m': 3.715241, 'e_o_k': [2.653744, 1.592246, 0.955348], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 1.331561, 'e_o_k': [0.951115, 0.570669, 0.342401], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 1.635691, 'e_o_k': [1.431229, 0.858738], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.014189, 'e_o_k': [0.008334, 0.005001, 0.003000, 0.001800, 0.001080, 0.000648], 'p_i': 40, 'u_i': 4.5772},
        {'id': 7, 'e_m': 0.653569, 'e_o_k': [0.396859, 0.238115, 0.142869, 0.085721, 0.051433], 'p_i': 10, 'u_i': 4.4816},
    ]
    B_BUDGET = 88.319992
    return processors, tasks, B_BUDGET
