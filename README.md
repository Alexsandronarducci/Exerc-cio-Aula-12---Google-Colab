Alunos: Alexsandro N., Cauan V., Claudio S., Lucas B. e Rodrigo A.  
Disciplina: IA / Sistemas Baseados em Conhecimento  
Data de entrega: 01/06/2026  

# Trabalho – Sistema de Controle Fuzzy

## Objetivo
Implementar um sistema de controle fuzzy para ajustar automaticamente a velocidade de um ventilador com base nos valores de temperatura e umidade, analisando o comportamento do sistema com diferentes funções de pertinência.

## Exercício 1 – Revisão e expansão das regras
Foi realizada a revisão da tabela de regras fuzzy e adicionadas novas regras para aumentar a cobertura do sistema e melhorar a tomada de decisão.

Total de regras:
- Regras originais: 5
- Regras finais: 10

As alterações realizadas estão implementadas no arquivo `fuzzy_controller.py`.

## Exercício 2 – Testes com diferentes funções de pertinência

### Teste 1 – trimf (Função Triangular)
Resultado:
As funções triangulares apresentaram respostas simples e rápidas, com transições lineares entre estados e baixo custo computacional.

### Teste 2 – gaussmf (Função Gaussiana)
Resultado:
As funções gaussianas produziram transições mais suaves e contínuas, reduzindo mudanças bruscas na velocidade do ventilador.

### Teste 3 – trapmf (Função Trapezoidal)
Resultado:
As funções trapezoidais apresentaram maior estabilidade nas regiões centrais, tornando o sistema menos sensível a pequenas variações.

## Conclusão
Entre os testes realizados, observou-se que:
- trimf → maior simplicidade e velocidade;
- gaussmf → comportamento mais natural;
- trapmf → maior estabilidade.

Os resultados demonstraram que diferentes funções de pertinência alteram o comportamento do controlador fuzzy e influenciam diretamente a forma como as decisões são tomadas.
