"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 25, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "freq", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 25, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "freq", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.878081, 'e_o_k': [0.179935, 0.143948, 0.115158], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 1.760389, 'e_o_k': [0.238582, 0.190865, 0.152692, 0.122154, 0.097723, 0.078178], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 15.213605, 'e_o_k': [4.226002, 3.380801], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 1.221415, 'e_o_k': [0.165536, 0.132429, 0.105943, 0.084754, 0.067803, 0.054243], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 1.867670, 'e_o_k': [0.382719, 0.306175, 0.244940], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 1.951144, 'e_o_k': [0.264434, 0.211547, 0.169238, 0.135390, 0.108312, 0.086650], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 1.842208, 'e_o_k': [0.377502, 0.302001, 0.241601], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 1.167704, 'e_o_k': [0.324362, 0.259490], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
