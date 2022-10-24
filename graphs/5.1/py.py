import numpy as np
def al(x):
    return 10.842 - 148.55 * x + 865.85 * x**2 - 2321.6 * x**3 + 1144.9 * x**4 + 8397.5 * x**5 - 18682 * x**6 + 12191 * x**7

def pb(x):
    return 3.697 - 6.1195 * x + 4.5804 * x**2 - 1.6394 * x**3 + 0.27906 * x**4 - 0.021153 * x**5 + 0.00064725 * x**6 - 6.0829e-06 * x**7

def fe(x):
    return 8.6489 - 38.099 * x + 75.071 * x**2 - 80.346 * x**3 + 47.978 * x**4 - 14.828 * x**5 + 1.8118 * x**6

es = np.linspace(0.5, 0.9, 100000)


al_l = 0
al_r = 0
fe_l = 0
fe_r = 0
pb_l = 0
pb_r = 0
ale = 0
fee=0
pbe=0

alu = [0.163, 0.186, 0.209]
fer = [0.506, 0.551, 0.596]
pub = [1.191, 1.262, 1.333]

E = (al(alu[1]) /( al(alu[0]) - al(alu[2])) + fe(fer[1]) /( fe(fer[0]) - fe(fer[2])) + pb(pub[1]) /( pb(pub[0]) - pb(pub[2]))) / (1 /( al(alu[0]) - al(alu[2])) + 1 /( fe(fer[0]) - fe(fer[2])) + 1 /( pb(pub[0]) - pb(pub[2])))

delta = np.sqrt(1/(1/( al(alu[0]) - al(alu[2]))**2 + 1/( pb(pub[0]) - pb(pub[2]))**2 + 1/( fe(fer[0]) - fe(fer[2]))**2))

print(E, "+-", delta)

# 0.6523
