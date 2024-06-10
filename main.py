import Problem_1.Punkt_2.otoczka_wypukla_grahama as p1
import Problem_3.Part1.punkt1 as p3
import Problem_3.Part2_V1.P1 as p3_v1
import Problem_3.Part2_V2.p3 as p3_v2

otoczka = dict(p1.get_result())
jasnosc = p3_v1.MakeRandomBrightness(len(otoczka))

plaszczaki_lista = p3.generate_and_find_max_plaszczaki(otoczka)


for i in range (len(otoczka)):
    p3_v1.GetOptimalStops(jasnosc, plaszczaki_lista[i])
