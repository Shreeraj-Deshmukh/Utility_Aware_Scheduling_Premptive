"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.697259, 'e_o_k': [0.118099, 0.094480, 0.075584, 0.060467], 'p_i': 10, 'u_i': 1.6266},
        {'id': 1, 'e_m': 0.828822, 'e_o_k': [0.230228, 0.184183], 'p_i': 20, 'u_i': 2.5167},
        {'id': 2, 'e_m': 15.359768, 'e_o_k': [2.081676, 1.665340, 1.332272, 1.065818, 0.852654, 0.682123], 'p_i': 40, 'u_i': 3.7793},
        {'id': 3, 'e_m': 24.387107, 'e_o_k': [4.130608, 3.304486, 2.643589, 2.114871], 'p_i': 80, 'u_i': 1.9533},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET
