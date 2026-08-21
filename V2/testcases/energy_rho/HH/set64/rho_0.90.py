"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 166.336004, "H": 80, "J": 24, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.9, "seed": 1064, "set": 64, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.90"}
"""

_SPEC = '{"B": 166.336004, "H": 80, "J": 24, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.9, "seed": 1064, "set": 64, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.443349, 'e_o_k': [0.601109, 0.480887, 0.384710, 0.307768, 0.246214], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 4.992277, 'e_o_k': [3.882882, 3.106306], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 1.773001, 'e_o_k': [1.017296, 0.813837, 0.651069], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 4.820922, 'e_o_k': [2.286345, 1.829076, 1.463261, 1.170609], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 5.896724, 'e_o_k': [2.455799, 1.964639, 1.571711, 1.257369, 1.005895], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 9.193774, 'e_o_k': [7.150713, 5.720571], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.009519, 'e_o_k': [0.004514, 0.003611, 0.002889, 0.002311], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 0.777730, 'e_o_k': [0.446238, 0.356991, 0.285593], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 166.336004
    return processors, tasks, B_BUDGET
