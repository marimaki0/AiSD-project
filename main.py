import Problem_1.Punkt_2.otoczka_wypukla_grahama as p1
import Problem_3.Part1.punkt1 as p3
import Problem_3.Part2_V1.P1 as p3_v1
import Problem_3.Part2_V2.p3 as p3_v2

otoczka = list(p1.get_result())
jasnosc = p3_v1.MakeRandomBrightness(len(otoczka))

plaszczaki_lista = p3.generate_and_find_max_plaszczaki(otoczka)

print("jasnosc: ", jasnosc)
print("otoczka: ", otoczka)
print("plaszczaki lista: ", plaszczaki_lista)

for i in range (0, len(plaszczaki_lista) - 1):
    rez=jasnosc
    print("Optimal stop: ", p3_v1.GetOptimalStops(rez, plaszczaki_lista[i]))
