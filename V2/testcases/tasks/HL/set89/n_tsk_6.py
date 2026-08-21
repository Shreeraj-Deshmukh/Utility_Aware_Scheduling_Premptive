"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.660058, 'e_o_k': [0.461127, 0.368902], 'p_i': 10, 'u_i': 3.8713},
        {'id': 1, 'e_m': 2.227363, 'e_o_k': [0.618712, 0.494970], 'p_i': 20, 'u_i': 1.2249},
        {'id': 2, 'e_m': 3.200608, 'e_o_k': [0.889058, 0.711246], 'p_i': 40, 'u_i': 3.9801},
        {'id': 3, 'e_m': 0.045073, 'e_o_k': [0.006109, 0.004887, 0.003910, 0.003128, 0.002502, 0.002002], 'p_i': 80, 'u_i': 1.7372},
        {'id': 4, 'e_m': 2.908664, 'e_o_k': [0.394205, 0.315364, 0.252291, 0.201833, 0.161466, 0.129173], 'p_i': 10, 'u_i': 1.2016},
        {'id': 5, 'e_m': 1.511811, 'e_o_k': [0.419947, 0.335958], 'p_i': 10, 'u_i': 4.7805},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET
