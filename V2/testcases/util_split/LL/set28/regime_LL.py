"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200012, "H": 80, "J": 43, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}
"""

_SPEC = '{"B": 55.200012, "H": 80, "J": 43, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.417118, 'e_o_k': [0.115866, 0.092693], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 1.031475, 'e_o_k': [0.211368, 0.169094, 0.135275], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 1.084639, 'e_o_k': [0.301289, 0.241031], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 6.513493, 'e_o_k': [1.103234, 0.882587, 0.706070, 0.564856], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.140753, 'e_o_k': [0.039098, 0.031278], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 0.605859, 'e_o_k': [0.102618, 0.082095, 0.065676, 0.052541], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 0.592474, 'e_o_k': [0.121409, 0.097127, 0.077701], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 0.713089, 'e_o_k': [0.146125, 0.116900, 0.093520], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 55.200012
    return processors, tasks, B_BUDGET
