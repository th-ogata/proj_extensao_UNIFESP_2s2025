# Bibliotecas e definição de constantes
import math

pi = 3.141592653589793
e = 2.71828

# Função para interpolar as propriedades da água
def interpolar(x, X, Y):
    # Procura intervalo [X[i], X[i+1]] onde x está
        n = len(X)
        for i in range(n - 1):
            if X[i] <= x <= X[i+1]:
                x0, x1 = X[i], X[i+1]
                y0, y1 = Y[i], Y[i+1]
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

# Prompt para inserção dos parâmetros do TC bitubular
print("\nInsira os parâmetros do TC bitubular...")
De = float(input("Diametro Externo (m): "))
Di = float(input("Diametro Interno (m): "))
L = float(input("Comprimento do TC (m): "))
#Km = float(input("Coeficiente condutivo do tubo interno (W/m): "))
Qf = float(input("Vazão da corrente fria (m3/s): "))

# Prompt para inserção das temperaturas de entrada e saídas das correntes fria e quente
print("\nInsira as temperaturas das correntes...")
Tfe = float(input("Temp. de entrada da corrente fria (°C): "))
Tfs = float(input("Temp. de saída da corrente fria (°C): "))
Tqe = float(input("Temp. de entrada da corrente quente (°C): "))
Tqs = float(input("Temp. de saída da corrente quente (°C): "))

# Cálculo das temperaturas médias das correntes e diferença média logarítmica de temperatura
Tf_med = (Tfe + Tfs)/2
Tq_med = (Tqe + Tqs)/2
DelTML = ((Tqs - Tfs) - (Tqe - Tfe))/math.log((Tqs - Tfs)/(Tqe - Tfe))
#DelTML_K = DelTML + 273.15
DelT_q = Tqs - Tqe 
DelT_f = Tfs - Tfe

# Prompt seleção do modo de inserção das propriedades da água, manual (qualquer fluido) ou interpolado (apenas água de 0 a 100 °C)
print("\nSelecione uma opção:")
print("1 - Interpolar propriedades água (0 a 100 °C)")
print("2 - Inserir propriedades manualmente")
op = input("Opção: ")

if op == "1":
    Temp = [0, 20, 40, 60, 80, 100]
    rho = [999, 998, 992, 983, 972, 958]
    cp = [4.22e3, 4.18e3, 4.18e3, 4.19e3, 4.20e3, 4.22e3]
    mi = [1.79e-3, 1.00e-3, 6.53e-4, 4.68e-4, 3.55e-4, 2.82e-4]
    k = [0.561, 0.598, 0.630, 0.652, 0.670, 0.679]
    # O grande valor do intervalo de temperatura dos dados impacta um poquinho na precisão dos resultados da interpolação, por não serem lineares.

    # Chama a função, interpola em função da temperatura e retorna os valores interpolados
    rho_q = interpolar(Tq_med, Temp, rho)
    mi_q  = interpolar(Tq_med, Temp, mi)
    k_q   = interpolar(Tq_med, Temp, k)
    cp_q  = interpolar(Tq_med, Temp, cp)

    rho_f = interpolar(Tf_med, Temp, rho)
    mi_f  = interpolar(Tf_med, Temp, mi)
    k_f   = interpolar(Tf_med, Temp, k)
    cp_f  = interpolar(Tf_med, Temp, cp)

    # Plotar tabela com as propriedades para ambos os fluidos
    nomes = ["rho", "mu", "k", "cp"]
    prop_q = [rho_q, mi_q, k_q, cp_q]
    prop_f = [rho_f, mi_f, k_f, cp_f]
    unid = ["kg/m3", "Pa.s", "W/m.K", "J/kg.K"]

    print("\nPropriedades da água interpoladas para as temperaturas:")
    print(f"{'':12s}{Tq_med:10.3g} °C   {Tf_med:4.3g} °C")
    print(f"{'Propriedade':14s}{'Quente':>10s}{'Fria':>10s}")
    for nome, vq, vf, un in zip(nomes, prop_q, prop_f, unid):
        print(f"{nome:10s}  {vq:10.4g}  {vf:10.4g}  {un:}")

elif op == "2":
    print("\nInserir propriedades manualmente...")
    cp_f = float(input(f"Capacidade calorífica do fluido Frio a T = {Tf_med:.2f} °C (J/kg.K): "))
    rho_f = float(input(f"Massa específica do fluido Frio a T = {Tf_med:.2f} °C (kg/m³): "))
    mi_f = float(input(f"Visc. do fluido Frio a T = {Tf_med:.2f} °C (Pa.s): "))
    k_f = float(input(f"Cond. térmica do fluido Frio a T = {Tf_med:.2f} °C (W/m.K): "))

    cp_q = float(input(f"\nCapacidade calorífica do fluido Quente a T = {Tq_med:.2f} °C (J/kg.K): "))
    rho_q = float(input(f"Massa específica do fluido Quente a T = {Tq_med:.2f} °C (kg/m³): "))
    mi_q = float(input(f"Visc. do fluido Quente a T = {Tq_med:.2f} °C (Pa.s): "))
    k_q = float(input(f"Cond. térmica do fluido Quente a T = {Tq_med:.2f} °C (W/m.K): "))

else:
    print("Opção inválida.")

# Cálculo das dimensções do TC
Dh = De - Di    #Diametro hidraulico
Atr_e = pi * (Dh**2)/4
Atr_i = pi * (Di**2)/4
Asi = pi * Di * L

#Número de Prandt
Pr_f = (cp_f * mi_f)/k_f 
Pr_q = (cp_q * mi_q)/k_q 

# Vazão mássica das correntes
mf = Qf * rho_f
mq = (mf * cp_f * (Tfs - Tfe))/(cp_q * (Tqe - Tqs))

# Velocidades
Vf = (mf/rho_f)/Atr_e
Vq = (mq/rho_q)/Atr_i

# Adiensionais, Número de Reynolds e Nusselt
Re_f = (rho_f * Vf * Dh)/mi_f
Re_q = (rho_q * Vq * Di)/mi_q

Nu_f = 1.86 * ((Re_f * Pr_f * (Dh/L))**(1/3)) * ((mi_f/mi_f)**0.14)
Nu_q =1.86 * ((Re_q * Pr_q * (Di/L))**(1/3)) * ((mi_q/mi_q)**0.14)

# Coef. Convectivo e Taxas de TC
h_e = (Nu_f * k_f)/Dh
h_i = (Nu_q * k_q)/Di

q_e = mf * cp_f * (Tfs - Tfe)
q_i = mq * cp_q * (Tqs - Tqe)

print("\nCoef. de TC por Convecção")
print(f"h_e = {h_e:.3g} W/m2.K   e   h_i = {h_i:.3g} W/m2.K\n")

print("Taxa de TC")
print(f"q_e = {q_e:} W  e  q_i = {q_i:} W")

# Resistências globais
U_exp = q_e/(Asi * DelTML)
U_teo = 1/((1/h_e)+(1/h_i))

print(f"U_exp = {U_exp:} W/m2.K  e  U_teo = {U_teo:} W/m2.K")

ER = (abs(U_exp - U_teo)/U_exp) * 100
print(f"ER = {ER:} %")

# Método da Efetividade
print("\nSelecione uma opção:")
print("1 - Calcular pelo método da efetividade")
print("2 - Não calcular")
op3 = input("Opção: ")

if op3 == "1":
    #Cálculos do C/C
    Cf = cp_f * mf
    Cq = cp_q * mq
    CC = Cq/Cf
    
    if Cf > Cq:
        Cmin = Cq
    else:
        Cmin = Cf

    #Calculo da efetividade-NUT
    NUT = Asi * U_exp/Cmin 

    print("\nSelecione uma opção:")
    print("1 - Paralelo")
    print("2 - Contra-corrente")
    op4 = input("Opção: ")
    if op4 == "1":
        #Paralelo
        print("\nParalelo:")
        epi = ((1 - e**(-NUT * (1 + CC)))/(1 + CC)) #Efetividade em f(NUT)

    elif "2":
        #Contra-corrente
        print("\nContra-corrente:")
        epi = ((1 - e**(-NUT * (1 - CC))) / (1 - CC * e**(-NUT * (1 - CC))))

    else:
        pass
else:
    pass
    
# Tqs = Tfe
if Cf > Cq:
    TT = Tfe
else:
    TT = Tqe

q_max = Cmin * (Tqe - TT)
q_efi = q_max * epi

efi_Tfs = q_efi/Cf + Tfe
efi_Tqs = Tqe - q_efi/Cq

ER_Tfs = abs((Tfs - efi_Tfs)/Tfs) * 100
ER_Tqs = abs((Tqs - efi_Tqs)/Tqs) * 100

epiperc = epi * 100
print(f"Efetividade  = {epiperc:.2f}%\n")

print(f"q_efi = {q_efi:.2f} W")

print(f"Tfs = {efi_Tfs:.2f} °C, Tqs = {efi_Tqs:.2f} °C pelo método da efetividade")
print(f"ER, Tfs  = {ER_Tfs:.5f}%")
print(f"ER, Tqs  = {ER_Tqs:.5f}%")


input("Pressione Enter para sair...")
