import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ==========================
# Função para executar teste
# ==========================

def executar_teste(nome_teste, controle, temperatura_valor, umidade_valor):
    simulacao = ctrl.ControlSystemSimulation(controle)

    simulacao.input['temperatura'] = temperatura_valor
    simulacao.input['umidade'] = umidade_valor

    simulacao.compute()

    print(
        nome_teste,
        "- Velocidade do ventilador:",
        round(
            simulacao.output[
                'velocidade_ventilador'
            ],
            2
        ),
        "%"
    )


# ============================================================
# TESTE 1 - Função Triangular (trimf)
# ============================================================

# ==========================
# Variáveis de Entrada
# ==========================

temperatura = ctrl.Antecedent(
    np.arange(-5, 41, 1),
    'temperatura'
)

umidade = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'umidade'
)

# ==========================
# Variável de Saída
# ==========================

velocidade_ventilador = ctrl.Consequent(
    np.arange(0, 101, 1),
    'velocidade_ventilador'
)

# ==========================
# Funções de Pertinência
# (trimf)
# ==========================

# Temperatura
temperatura['muito_baixa'] = fuzz.trimf(
    temperatura.universe,
    [-5, 0, 10]
)

temperatura['baixa'] = fuzz.trimf(
    temperatura.universe,
    [5, 15, 20]
)

temperatura['media'] = fuzz.trimf(
    temperatura.universe,
    [15, 25, 30]
)

temperatura['alta'] = fuzz.trimf(
    temperatura.universe,
    [25, 40, 40]
)

# Umidade
umidade['baixa'] = fuzz.trimf(
    umidade.universe,
    [0, 0, 50]
)

umidade['media'] = fuzz.trimf(
    umidade.universe,
    [25, 50, 75]
)

umidade['alta'] = fuzz.trimf(
    umidade.universe,
    [50, 100, 100]
)

# Velocidade
velocidade_ventilador['baixa'] = fuzz.trimf(
    velocidade_ventilador.universe,
    [0, 0, 50]
)

velocidade_ventilador['media'] = fuzz.trimf(
    velocidade_ventilador.universe,
    [25, 50, 75]
)

velocidade_ventilador['alta'] = fuzz.trimf(
    velocidade_ventilador.universe,
    [50, 100, 100]
)

# ==========================
# Regras Fuzzy (10 regras)
# ==========================

regra0 = ctrl.Rule(
    temperatura['muito_baixa'],
    velocidade_ventilador['baixa']
)

regra1 = ctrl.Rule(
    temperatura['baixa'] &
    umidade['baixa'],
    velocidade_ventilador['baixa']
)

regra2 = ctrl.Rule(
    temperatura['baixa'] &
    umidade['media'],
    velocidade_ventilador['baixa']
)

regra3 = ctrl.Rule(
    temperatura['baixa'] &
    umidade['alta'],
    velocidade_ventilador['media']
)

regra4 = ctrl.Rule(
    temperatura['media'] &
    umidade['baixa'],
    velocidade_ventilador['media']
)

regra5 = ctrl.Rule(
    temperatura['media'] &
    umidade['media'],
    velocidade_ventilador['media']
)

regra6 = ctrl.Rule(
    temperatura['media'] &
    umidade['alta'],
    velocidade_ventilador['alta']
)

regra7 = ctrl.Rule(
    temperatura['alta'] &
    umidade['baixa'],
    velocidade_ventilador['alta']
)

regra8 = ctrl.Rule(
    temperatura['alta'] &
    umidade['media'],
    velocidade_ventilador['alta']
)

regra9 = ctrl.Rule(
    temperatura['alta'] &
    umidade['alta'],
    velocidade_ventilador['alta']
)

# ==========================
# Sistema de Controle
# ==========================

controle_trimf = ctrl.ControlSystem([
    regra0,
    regra1,
    regra2,
    regra3,
    regra4,
    regra5,
    regra6,
    regra7,
    regra8,
    regra9
])

# ==========================
# Teste de Execução
# ==========================

executar_teste(
    "Teste 1 - trimf",
    controle_trimf,
    15,
    20
)


# ============================================================
# TESTE 2 - Função Gaussiana (gaussmf)
# ============================================================

temperatura_gauss = ctrl.Antecedent(
    np.arange(-5, 41, 1),
    'temperatura'
)

umidade_gauss = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'umidade'
)

velocidade_ventilador_gauss = ctrl.Consequent(
    np.arange(0, 101, 1),
    'velocidade_ventilador'
)

# Temperatura
temperatura_gauss['muito_baixa'] = fuzz.gaussmf(
    temperatura_gauss.universe,
    0,
    5
)

temperatura_gauss['baixa'] = fuzz.gaussmf(
    temperatura_gauss.universe,
    15,
    5
)

temperatura_gauss['media'] = fuzz.gaussmf(
    temperatura_gauss.universe,
    25,
    5
)

temperatura_gauss['alta'] = fuzz.gaussmf(
    temperatura_gauss.universe,
    35,
    5
)

# Umidade
umidade_gauss['baixa'] = fuzz.gaussmf(
    umidade_gauss.universe,
    20,
    15
)

umidade_gauss['media'] = fuzz.gaussmf(
    umidade_gauss.universe,
    50,
    15
)

umidade_gauss['alta'] = fuzz.gaussmf(
    umidade_gauss.universe,
    80,
    15
)

# Velocidade
velocidade_ventilador_gauss['baixa'] = fuzz.gaussmf(
    velocidade_ventilador_gauss.universe,
    20,
    15
)

velocidade_ventilador_gauss['media'] = fuzz.gaussmf(
    velocidade_ventilador_gauss.universe,
    50,
    15
)

velocidade_ventilador_gauss['alta'] = fuzz.gaussmf(
    velocidade_ventilador_gauss.universe,
    80,
    15
)

# Regras Fuzzy
regra0_gauss = ctrl.Rule(
    temperatura_gauss['muito_baixa'],
    velocidade_ventilador_gauss['baixa']
)

regra1_gauss = ctrl.Rule(
    temperatura_gauss['baixa'] &
    umidade_gauss['baixa'],
    velocidade_ventilador_gauss['baixa']
)

regra2_gauss = ctrl.Rule(
    temperatura_gauss['baixa'] &
    umidade_gauss['media'],
    velocidade_ventilador_gauss['baixa']
)

regra3_gauss = ctrl.Rule(
    temperatura_gauss['baixa'] &
    umidade_gauss['alta'],
    velocidade_ventilador_gauss['media']
)

regra4_gauss = ctrl.Rule(
    temperatura_gauss['media'] &
    umidade_gauss['baixa'],
    velocidade_ventilador_gauss['media']
)

regra5_gauss = ctrl.Rule(
    temperatura_gauss['media'] &
    umidade_gauss['media'],
    velocidade_ventilador_gauss['media']
)

regra6_gauss = ctrl.Rule(
    temperatura_gauss['media'] &
    umidade_gauss['alta'],
    velocidade_ventilador_gauss['alta']
)

regra7_gauss = ctrl.Rule(
    temperatura_gauss['alta'] &
    umidade_gauss['baixa'],
    velocidade_ventilador_gauss['alta']
)

regra8_gauss = ctrl.Rule(
    temperatura_gauss['alta'] &
    umidade_gauss['media'],
    velocidade_ventilador_gauss['alta']
)

regra9_gauss = ctrl.Rule(
    temperatura_gauss['alta'] &
    umidade_gauss['alta'],
    velocidade_ventilador_gauss['alta']
)

controle_gauss = ctrl.ControlSystem([
    regra0_gauss,
    regra1_gauss,
    regra2_gauss,
    regra3_gauss,
    regra4_gauss,
    regra5_gauss,
    regra6_gauss,
    regra7_gauss,
    regra8_gauss,
    regra9_gauss
])

executar_teste(
    "Teste 2 - gaussmf",
    controle_gauss,
    15,
    20
)


# ============================================================
# TESTE 3 - Função Trapezoidal (trapmf)
# ============================================================

temperatura_trap = ctrl.Antecedent(
    np.arange(-5, 41, 1),
    'temperatura'
)

umidade_trap = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'umidade'
)

velocidade_ventilador_trap = ctrl.Consequent(
    np.arange(0, 101, 1),
    'velocidade_ventilador'
)

# Temperatura
temperatura_trap['muito_baixa'] = fuzz.trapmf(
    temperatura_trap.universe,
    [-5, -5, 0, 10]
)

temperatura_trap['baixa'] = fuzz.trapmf(
    temperatura_trap.universe,
    [5, 10, 15, 20]
)

temperatura_trap['media'] = fuzz.trapmf(
    temperatura_trap.universe,
    [15, 20, 25, 30]
)

temperatura_trap['alta'] = fuzz.trapmf(
    temperatura_trap.universe,
    [25, 35, 40, 40]
)

# Umidade
umidade_trap['baixa'] = fuzz.trapmf(
    umidade_trap.universe,
    [0, 0, 25, 50]
)

umidade_trap['media'] = fuzz.trapmf(
    umidade_trap.universe,
    [25, 40, 60, 75]
)

umidade_trap['alta'] = fuzz.trapmf(
    umidade_trap.universe,
    [50, 75, 100, 100]
)

# Velocidade
velocidade_ventilador_trap['baixa'] = fuzz.trapmf(
    velocidade_ventilador_trap.universe,
    [0, 0, 25, 50]
)

velocidade_ventilador_trap['media'] = fuzz.trapmf(
    velocidade_ventilador_trap.universe,
    [25, 40, 60, 75]
)

velocidade_ventilador_trap['alta'] = fuzz.trapmf(
    velocidade_ventilador_trap.universe,
    [50, 75, 100, 100]
)

# Regras Fuzzy
regra0_trap = ctrl.Rule(
    temperatura_trap['muito_baixa'],
    velocidade_ventilador_trap['baixa']
)

regra1_trap = ctrl.Rule(
    temperatura_trap['baixa'] &
    umidade_trap['baixa'],
    velocidade_ventilador_trap['baixa']
)

regra2_trap = ctrl.Rule(
    temperatura_trap['baixa'] &
    umidade_trap['media'],
    velocidade_ventilador_trap['baixa']
)

regra3_trap = ctrl.Rule(
    temperatura_trap['baixa'] &
    umidade_trap['alta'],
    velocidade_ventilador_trap['media']
)

regra4_trap = ctrl.Rule(
    temperatura_trap['media'] &
    umidade_trap['baixa'],
    velocidade_ventilador_trap['media']
)

regra5_trap = ctrl.Rule(
    temperatura_trap['media'] &
    umidade_trap['media'],
    velocidade_ventilador_trap['media']
)

regra6_trap = ctrl.Rule(
    temperatura_trap['media'] &
    umidade_trap['alta'],
    velocidade_ventilador_trap['alta']
)

regra7_trap = ctrl.Rule(
    temperatura_trap['alta'] &
    umidade_trap['baixa'],
    velocidade_ventilador_trap['alta']
)

regra8_trap = ctrl.Rule(
    temperatura_trap['alta'] &
    umidade_trap['media'],
    velocidade_ventilador_trap['alta']
)

regra9_trap = ctrl.Rule(
    temperatura_trap['alta'] &
    umidade_trap['alta'],
    velocidade_ventilador_trap['alta']
)

controle_trap = ctrl.ControlSystem([
    regra0_trap,
    regra1_trap,
    regra2_trap,
    regra3_trap,
    regra4_trap,
    regra5_trap,
    regra6_trap,
    regra7_trap,
    regra8_trap,
    regra9_trap
])

executar_teste(
    "Teste 3 - trapmf",
    controle_trap,
    15,
    20
)
