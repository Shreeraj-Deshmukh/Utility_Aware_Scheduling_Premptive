"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.415674, 'e_o_k': [0.699933, 0.559947, 0.447957], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.148832, 'e_o_k': [0.030498, 0.024399, 0.019519], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 2.086145, 'e_o_k': [0.427489, 0.341991, 0.273593], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 0.844474, 'e_o_k': [0.173048, 0.138438, 0.110751], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 1.893474, 'e_o_k': [0.388007, 0.310406, 0.248324], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 1.089996, 'e_o_k': [0.223360, 0.178688, 0.142950], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 2.548948, 'e_o_k': [0.522325, 0.417860, 0.334288], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.028745, 'e_o_k': [0.005890, 0.004712, 0.003770], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
