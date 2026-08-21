"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.249202, 'e_o_k': [0.347001, 0.277601], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 1.221788, 'e_o_k': [0.339386, 0.271508], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 6.176629, 'e_o_k': [1.715730, 1.372584], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 8.093637, 'e_o_k': [2.248232, 1.798586], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 0.742083, 'e_o_k': [0.206134, 0.164907], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 6.497443, 'e_o_k': [1.804845, 1.443876], 'p_i': 40, 'u_i': 2.6468},
        {'id': 6, 'e_m': 0.756149, 'e_o_k': [0.210041, 0.168033], 'p_i': 20, 'u_i': 2.0597},
        {'id': 7, 'e_m': 11.168684, 'e_o_k': [3.102412, 2.481930], 'p_i': 80, 'u_i': 3.8347},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
