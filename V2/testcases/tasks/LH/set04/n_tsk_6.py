"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319986, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319986, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.635332, 'e_o_k': [0.301309, 0.241047, 0.192838, 0.154270], 'p_i': 10, 'u_i': 3.6021},
        {'id': 1, 'e_m': 0.040561, 'e_o_k': [0.023273, 0.018618, 0.014894], 'p_i': 20, 'u_i': 4.3808},
        {'id': 2, 'e_m': 2.011850, 'e_o_k': [0.954129, 0.763303, 0.610643, 0.488514], 'p_i': 40, 'u_i': 1.2748},
        {'id': 3, 'e_m': 3.807699, 'e_o_k': [2.184746, 1.747796, 1.398237], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 2.323533, 'e_o_k': [1.333175, 1.066540, 0.853232], 'p_i': 20, 'u_i': 3.8582},
        {'id': 5, 'e_m': 2.407392, 'e_o_k': [1.381290, 1.105032, 0.884026], 'p_i': 20, 'u_i': 1.6137},
    ]
    B_BUDGET = 88.319986
    return processors, tasks, B_BUDGET
