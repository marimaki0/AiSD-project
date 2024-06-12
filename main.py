import Problem_1.Punkt_2.otoczka_wypukla_grahama as p1
import Problem_3.Part1.punkt1 as p3
import Problem_3.Part2_V1.P1 as p3_v1
import Problem_3.Part2_V2.p3 as p3_v2


otoczka = list(p1.GetResult())
jasnosc = p3_v1.MakeRandomBrightness(len(otoczka))

plaszczaki_lista = p3.GenerateAndFindMaxPlaszczaki(otoczka)

print("jasnosc: ", jasnosc)
print("otoczka: ", otoczka)
print("plaszczaki lista: ", plaszczaki_lista)

for i in range (0, len(plaszczaki_lista) - 1):
    jasnosc_copy = jasnosc.copy()
    en = plaszczaki_lista[i]

    r = p3_v1.GetOptimalStops(jasnosc_copy, en)
    print("Optimal stop v1: ", r)

    jasnosc_copy = jasnosc.copy()
    r2 = p3_v2.GetOptimalStops(jasnosc_copy, en)
    print("Optimal stop v2: ", r2)
