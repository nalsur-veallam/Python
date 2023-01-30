import numpy as np

# ------------------------------ИТЕРАЦИИ-----------------------------------
# кол-во итераций ( поколений )
age = 2000
# кол-во муравьев в поколении
countage = 10
# кол-во городов

line = input().split()
N = int(line[0])
M = int(line[1])
K = int(line[2])
S = int(line[3])
F = int(line[4])

n = N# Количество городов, которое посещает муравей (Равно количеству городов)

# ------------------------------ПАРМЕТРЫ-----------------------------------
# альфа - коэффициент запаха, при 0 будем ориентироваться только на
# кратчайший путь 
a = 1 
# бета - коэффициент расстояния, при 0 будем
# ориентироваться только на оставляемый запах
b = 2
# коэффициент обновления, глобальное
e = 0.1
# коэффициент обновления, локальное
p = 0.1
# количество выпускаемых феромонов 
Q = 1
# баланс между лучшим городом и как в AS
q = 0.9
# начальный феромон
ph = Q/(n*2000)

# -------------------------------ПАМЯТЬ------------------------------------
# матрица расстояний
dist = np.zeros((N,N)) 
# матрица обратных расстояний
invdist = np.zeros((N,N)) 
# матрица маршрута муравьев в одном поколении
ROUTEant = np.zeros((countage,N))
# вектор расстояний муравьев в одном поколении
DISTant = np.zeros(countage)
# вектор лучших дистанций на каждой итерации
bestDistVec = np.zeros(age)
# лучший начальный маршрут
bestDIST = 1e7
# оптимальные маршруты
ROUTE = np.zeros(n+1)
ROUTE[-1] = F-1
# перестановка городов без повторений ( для выхода муравьев )
RANDperm = np.random.shuffle(np.arange(N))
# матрица вероятностей
P = np.zeros(N)
# максимальное значение вероятности
val = 0
# присваем номер города
getcity = 0
# индекс максимального значения вероятности
indexP = 0
# максимальное
minDISTiterration = 0

# -------------------------------------------------------------------------


# матрица начальных феромонов
tao = ph*np.ones((n,n)) - ph*np.eye(n)

for i in range(M):
    line = input().split()
    dist[int(line[0])-1][int(line[1])-1] = float(line[2])
    dist[int(line[1])-1][int(line[0])-1] = float(line[2])
    
    invdist[int(line[0])-1][int(line[1])-1] = 1/float(line[2])
    invdist[int(line[1])-1][int(line[0])-1] = 1/float(line[2])

# матрица городов, которые надо посетить
cities = np.array(input().split(), dtype='int')
cities = cities - np.ones(cities.shape)

# итерации
for it in range(age):
    # муравьи ( одно поколение)
    for k in range(countage):
    # ****************** НАЧАЛЬНОЕ РАСПОЛОЖЕНИЕ МУРАВЬЕВ ******************
        ROUTEant[k,0] = S-1
    
    # *********************************************************************
    
        # путь каждого муравья, начиная со второго, так как первый выбран
        for s in range(1, N):

            # полуаем индекс выбранного города
            ir = ROUTEant[k, s-1]
    
            # вероятность посещения городов ( числитель ) , в числителе у нас
            # следующее: tao^a*(1/S)^b 
            # 1/S -это returndist. 
            
            # поскольку данное значение будет повторяться (кол-во муравьев * на
            # колонию * кол-во городов) раз, то еще один цикл писать не выгодно,
            # скорость работы при таких вычислениях падает. Поэтому написал в 
            # этом моменте векторно. На обычном языке будет так: 
            
    #         for c = 1:n             
    #             P(1,c) = tao(ir,c).^a * returndist(ir,c).^b          
    #         end

            P = tao[int(ir), :]**a * invdist[int(ir), :]**b
            # получили числители (в формуле вероятности перехода к k-ому городу)
            # для n городов, однако в некоторых мы уже побывали, нужно исключить
            # их
            
            # проставляем нули в числитель туда, где уже были, чтобы
            # вероятность перехода была 0, следовательно в сумме знаменателя
            # формулы данный город учитываться не будет    
            P[np.array(ROUTEant[k, :s-1], dtype='int')] = 0
            
            # смотрим в какой город осуществляется переход
            RANDOME = np.random.rand()
            
            if RANDOME <= q:
                val = P.max()
                getcity = int(np.argwhere(P == val)[0])
            else:
                # получаем вероятности перехода ( сумма строк должна быть = 1 )
                P = P/np.sum(P)
                getcity = int((P > RANDOME)[0])
        
            # присваем s-ый город в путь k-ому муравью
            ROUTEant[k,s] = getcity
        
        # получаем маршрут k-ого муравья
        ROUTE[:-1] = ROUTEant[k, :]
        
        # сброс длины
        Len = 0
        
        # вычисляем маршрут k-ого муравья
        for i in range(n):
            Len += dist[int(ROUTE[i]), int(ROUTE[i+1])]
        
        # путь k-ого муравья, массив дистанций k-ых муравьев age-ого поколения
        DISTant[k] = Len
        
        # присваевыем лучший маршрут и Len     
        if DISTant[k] < bestDIST:
            bestDIST = DISTant[k]
            bestROUTE = ROUTE
        
        # вектор "последних" городов k-ых муравьев ( выбирается для старта
        # муравьев нового поколения с тех городов, где закончили путь
        # предыдущее поколение)
        
        lastROUTEant = ROUTEant[:,-1]
    
        # локальное обновление феромона, после  каждого муравья
        for tL in range(n):

            xL = ROUTE[tL]
            yL = ROUTE[tL+1]

            # считаем новый феромон
            tao[int(xL),int(yL)] = (1-p)*tao[int(xL),int(yL)] + p*ph
            tao[int(yL),int(xL)] = (1-p)*tao[int(yL),int(xL)] + p*ph
# --------------------------ГЛОБАЛЬНОЕ ОБНОВЛЕНИЕ--------------------------

    # Испаряем феромоны "старого" пути е - коэффициент испарения
    
    tao[tao < 2.5e-150] = 2.50e-150
    
    # для каждого города
    for t in range(n):
        
        xG = bestROUTE[t]
        yG = bestROUTE[t+1]
        
        # считаем новый феромон
        tao[int(xG),int(yG)] = tao[int(xG),int(yG)] + e*Q/bestDIST 
        tao[int(yG),int(xG)] = tao[int(yG),int(xG)] + e*Q/bestDIST


newROUTE = []
newROUTE.append(S-1)
k = 0

for i in range(1, N):
    if int(bestROUTE[i]) not in cities:
        if dist[int(newROUTE[k]), int(bestROUTE[i+1])] < dist[int(newROUTE[k]), int(bestROUTE[i])] + dist[int(bestROUTE[i]), int(bestROUTE[i+1])]:
            pass
        else:
            newROUTE.append(bestROUTE[i])
            k+=1
    else:
        newROUTE.append(bestROUTE[i])
        
newROUTE.append(F-1)

ROUTE = np.array(newROUTE, dtype='int')
ROUTE = ROUTE + np.ones(ROUTE.shape)
    
print(Len)
print(ROUTE)
