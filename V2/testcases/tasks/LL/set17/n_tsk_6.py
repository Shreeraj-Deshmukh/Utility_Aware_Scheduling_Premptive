"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.544221, 'e_o_k': [0.151172, 0.120938], 'p_i': 10, 'u_i': 3.6581},
        {'id': 1, 'e_m': 0.741296, 'e_o_k': [0.110259, 0.088207, 0.070566, 0.056453, 0.045162], 'p_i': 20, 'u_i': 4.4037},
        {'id': 2, 'e_m': 5.236422, 'e_o_k': [0.709681, 0.567745, 0.454196, 0.363357, 0.290685, 0.232548], 'p_i': 40, 'u_i': 3.5196},
        {'id': 3, 'e_m': 9.849953, 'e_o_k': [1.334942, 1.067954, 0.854363, 0.683491, 0.546792, 0.437434], 'p_i': 80, 'u_i': 2.9192},
        {'id': 4, 'e_m': 1.498345, 'e_o_k': [0.253785, 0.203028, 0.162422, 0.129938], 'p_i': 40, 'u_i': 2.0454},
        {'id': 5, 'e_m': 0.680783, 'e_o_k': [0.092265, 0.073812, 0.059050, 0.047240, 0.037792, 0.030233], 'p_i': 40, 'u_i': 2.8602},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
