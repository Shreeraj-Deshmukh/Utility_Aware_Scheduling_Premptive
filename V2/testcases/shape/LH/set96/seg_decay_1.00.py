"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.252893, 'e_o_k': [0.177025, 0.177025], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.097609, 'e_o_k': [0.045551, 0.045551, 0.045551], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 5.092114, 'e_o_k': [3.564480, 3.564480], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 3.280589, 'e_o_k': [0.765471, 0.765471, 0.765471, 0.765471, 0.765471, 0.765471], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 2.269701, 'e_o_k': [1.588791, 1.588791], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 3.382746, 'e_o_k': [1.183961, 1.183961, 1.183961, 1.183961], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 0.542314, 'e_o_k': [0.151848, 0.151848, 0.151848, 0.151848, 0.151848], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.186349, 'e_o_k': [0.086963, 0.086963, 0.086963], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
