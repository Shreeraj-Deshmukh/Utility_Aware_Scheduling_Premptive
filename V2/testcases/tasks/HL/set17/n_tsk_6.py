"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.088441, 'e_o_k': [0.302345, 0.241876], 'p_i': 10, 'u_i': 3.6581},
        {'id': 1, 'e_m': 1.482591, 'e_o_k': [0.220519, 0.176415, 0.141132, 0.112906, 0.090324], 'p_i': 20, 'u_i': 4.4037},
        {'id': 2, 'e_m': 10.472843, 'e_o_k': [1.419361, 1.135489, 0.908391, 0.726713, 0.581370, 0.465096], 'p_i': 40, 'u_i': 3.5196},
        {'id': 3, 'e_m': 19.699905, 'e_o_k': [2.669885, 2.135908, 1.708726, 1.366981, 1.093585, 0.874868], 'p_i': 80, 'u_i': 2.9192},
        {'id': 4, 'e_m': 2.996690, 'e_o_k': [0.507570, 0.406056, 0.324844, 0.259876], 'p_i': 40, 'u_i': 2.0454},
        {'id': 5, 'e_m': 1.361566, 'e_o_k': [0.184530, 0.147624, 0.118099, 0.094479, 0.075584, 0.060467], 'p_i': 40, 'u_i': 2.8602},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
