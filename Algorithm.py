import random
import numpy as np
import math
from matplotlib import pyplot as plt

class vec2:#Класс для вектора
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def leng(self, vec):#Расчет длинны от одного вектора до другого
        return ((self.x - vec.x) ** 2 + (self.y - vec.y) ** 2) ** 0.5

def NearestValue(Lengs, Target):#Функция возвращающяя ближайшее значение по растаянию от точки
    diff = 10000
    ID = 0
    for i in range(0, len(Lengs)):
        if (math.fabs(Lengs[i] - Target) < diff):
            diff = math.fabs(Lengs[i] - Target)
            ID = i
    return ID

def NotReplyId(Path, Leng2):# Функция возращаюшя ближайший ID точки, которой еше нет в пути
    step = 0
    idNotFind = True
    while (idNotFind == True):
        step += 0.1
        idOfNear = NearestValue(Leng2, step)
        b = np.in1d(idOfNear, Path)
        if (b[0] == False):
            idNotFind = False
        if step > 1000:
            con = 1
            for val in range(0, 20):
                idOfNear = val
                b = np.in1d(idOfNear, Path2)
                if (b[0] == False):
                    idNotFind = False
                if (con >=20):
                    idNotFind = False
                    print(idNotFind)
                con += 1
    return  idOfNear

NumberOfDots = 20 #Кол-во точек
MassOfDots = np.zeros(20, dtype=vec2)
for i in range (0, NumberOfDots):#Генерация точек
    NewVec = vec2(random.randint(1, 100), random.randint(1,100))
    MassOfDots[i] = NewVec
Base = vec2(0,0)#Точка начала
NumberOfInd = 20 #Кол-во особей
Path = np.zeros((NumberOfInd, NumberOfDots), dtype=int)
ArrOfDots = range(0, NumberOfDots)
for i in range(0, NumberOfInd):#Генерация пути
    for j in range(0, NumberOfDots):
        Path[i] = random.sample(ArrOfDots, NumberOfDots)
print(Path)

SummLeng = np.zeros(NumberOfInd)
for j in range(0, NumberOfInd):
    NewMassOfDots = MassOfDots

    for i in range(0, NumberOfDots):
        Leng = np.zeros(len(NewMassOfDots))
        for n in range(0, len(NewMassOfDots)):
            if i == 0:
                Leng[n] = (vec2.leng(Base, NewMassOfDots[n]))
            else:
                Leng[n] = vec2.leng(MassOfDots[idOfMove], NewMassOfDots[n])
        idOfMove = Path[j][i]
        SummLeng[j] += Leng[idOfMove]

BestInd = 0
BestIndPath = 10000
x = np.zeros(21)
y = np.zeros(21)
for i in range(0, NumberOfInd): #Вывод лучшей особи в сгенирированном поколении
    if SummLeng[i] < BestIndPath:
        BestIndPath = SummLeng[i]
        BestInd = i
print("Лучшая особь: ", BestInd, "Длинна", BestIndPath)
for i in range(0,21):
    if i == 0:
        x[i] = Base.x
        y[i] = Base.y
    else:
        x[i] = MassOfDots[Path[BestInd][i-1]].x
        y[i] = MassOfDots[Path[BestInd][i-1]].y
print(x,y)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
BestLeng = 2000
BestsInd = 0
BestPoc = 0
BestPath = []
int_exit = 0

Half = int(NumberOfDots * 0.5)
for g in range(0,200):
    SummLeng = np.zeros(NumberOfInd)
    for j in range(0, NumberOfInd):
        NewMassOfDots = MassOfDots

        for i in range(0, NumberOfDots): #Расчет суммы длинны
            Leng = np.zeros(len(NewMassOfDots))
            for n in range(0, len(NewMassOfDots)):
                if i == 0:
                    Leng[n] = (vec2.leng(Base, NewMassOfDots[n]))
                else:
                    Leng[n] = vec2.leng(MassOfDots[idOfMove], NewMassOfDots[n])
            idOfMove = Path[j][i]
            SummLeng[j] += Leng[idOfMove]

    for j in range(0,NumberOfInd):# Лучшая особь
        if SummLeng[j] < BestLeng:
            BestLeng = SummLeng[j]
            BestsInd = j
            BestPoc = g
            int_exit = 0
            BestPath = Path[j]
    int_exit += 1
    if int_exit > 20: #Выход если больше 10 поколений нет улучшений
        break

    SummLengVer = np.zeros(NumberOfInd) #Скрещивание
    MaxSummLengVer = 0
    for j in range(0, NumberOfInd):#Полоса значений
        SummLengVer[j] = 1/SummLeng[j]
        MaxSummLengVer += 1/SummLeng[j]

    Path2 = np.full((NumberOfInd, NumberOfDots),40, dtype=int)
    for j in range(0, NumberOfInd):

        Ver = random.uniform(0, MaxSummLengVer)
        Ver2 = random.uniform(0, MaxSummLengVer)
        SummVerLeft = 0
        SummVerRight = SummLengVer[0]
        for s in range(0, NumberOfInd):  # выбор значения в интервале
            if (Ver > SummVerLeft) & (Ver <= SummVerRight):
                IndexLeft = s
            if (Ver2 > SummVerLeft) & (Ver2 <= SummVerRight):
                IndexRight = s
            if (s != NumberOfInd - 1):
                SummVerLeft += SummLengVer[s]
                SummVerRight += SummLengVer[s + 1]

        Leng2 = np.zeros(len(MassOfDots))
        IndexRandom = 45
        RanDotNotPlase = False
        if (random.randrange(0,100,1) < 20):#Вероятность мутации 10%
            IndexRandom = random.randrange(0,NumberOfDots-1,1)
            DotRandom = random.randrange(0,NumberOfDots-1,1)
            RanDotNotPlase = True
        for n in range (0, NumberOfDots):#Скрещивание
            a = np.in1d(Path[IndexRight][n], Path2[j])
            if a[0] == False:#Если такого айди нет в пути
                if n != IndexRandom:
                    if n > Half:
                        Path2[j][n] = Path[IndexRight][n]
                    else:
                        Path2[j][n] = Path[IndexLeft][n]
                if (IndexRandom < 20) & (IndexRandom >= 1) & (RanDotNotPlase == True):#Мутация
                    for k in range(0, NumberOfDots):
                        if Path[IndexRight][n] != k:
                            Leng2[k] = vec2.leng(MassOfDots[Path[IndexRight][n]], MassOfDots[k])
                        else:
                            Leng2[k] = 10000
                    idOfNear = NotReplyId(Path2[j], Leng2)
                    Path2[j][IndexRandom] = idOfNear
                    RanDotNotPlase = False
                elif (IndexRandom == 0)&(RanDotNotPlase == True):
                    RanDotNotPlase = False
                    Path2[j][IndexRandom] = DotRandom

            else:#Если такой айди точки уже есть то замена на ближайшую не использованную
                for k in range(0, NumberOfDots):
                    if Path[IndexRight][n] != k:
                        Leng2[k] = vec2.leng(MassOfDots[Path[IndexRight][n]], MassOfDots[k])
                    else:
                        Leng2[k] = 10000
                idOfNear = NotReplyId(Path2[j],Leng2)
                Path2[j][n] = idOfNear
    Path = Path2
    print(Path2)

    print("Поколение:", g, "\nПуть:", SummLeng)
x = np.zeros(21)
y = np.zeros(21)
print("Лучшая особь: ", BestsInd, "В поколении: ", BestPoc, "С длиной:", BestLeng)
for i in range(0,21):#Построение пути
    if i == 0:
        x[i] = Base.x
        y[i] = Base.y
    else:
        x[i] = MassOfDots[BestPath[i-1]].x
        y[i] = MassOfDots[BestPath[i-1]].y
print(x,y)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()