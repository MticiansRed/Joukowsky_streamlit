import streamlit as st

menu = st.sidebar.radio('***',
    ("Постановка задачи", 
    "Вариационная формулировка",     
    )
)
if menu == "Постановка задачи": 
    r"""
    ##### Постановка задачи
     
     
    **Уравнение для функции тока**
    
    Плоские (двумерные) течения являются потенциальными (безвихревыми)
 
    $\begin{aligned}
    {-} \nabla^2 \psi = 0,
    \quad \bm x \in \Omega
    \end{aligned}$   
     

    **Краевые условия**

    Внешняя граница

    $\begin{aligned}
    -\nabla^2 \psi &= 0 \quad \text{в области} \ \Omega \\
    \psi &= x_1 + h \quad \text{на левой границе входа} \ (\Gamma_1) \\
    \psi &= x_1 + h \quad \text{на правой границе входа} \ (\Gamma_2) \\
    \psi &= \gamma \quad \text{на границе профиля} \ (\Gamma_3) \\
    \frac{\partial \psi}{\partial n} &= 0 \quad \text{на стенках канала} \ (\Gamma_4)
    \end{aligned}$
   
    Равномерный поток $($скорость $\bm u = \{-u_\infty, 0\})$ на внешней границе

    $\begin{aligned}
    \psi(\bm x) = x_2,
    \quad \bm x \in \Gamma
    \end{aligned}$
    

    **Условие на границе обтекаемого тела**
    
    Условие непротекания
       
    $\begin{aligned}
    \psi (\bm x) = \operatorname{const} ,
    \quad \bm x \in \gamma
    \end{aligned}$    
    
    Сама постоянная определятся из дополнительных условий
    
    **Условие Жуковского — Чаплыгина (аэродинамическое условие Кутты)**
    
    Скорость на заднем острие профиля конечна $-$ функция тока непрерывна
    
    Параметрические расчеты для минимизации скорости в области задней кромки 
    
        """
        
if menu == "Вариационная формулировка": 
    r"""
    ##### Конечно-элементная аппроксимация
    
    **Интегро-дифференциальные равенства** 
    
    Найти $\psi(\bm x) \in V$ такое, что:

    $\begin{aligned}
    \int_{\Omega} \nabla \psi \cdot \nabla v \, dx = 0  
    \quad \bm x \in \gamma
    \end{aligned}$   
    
    для всех $v(\bm x) \in V$

   **Пространство функций:**

   $\begin{aligned}
   V = \{ v \in H^1(\Omega) \ | \ v = x_1 + h \ \text{на} \ \Gamma_1 \cup \Gamma_2, \ v = \gamma \ \text{на} \ \Gamma_3 \}
   \end{aligned}$

   **Конечно-элементная реализация:**

   - Лагранжевые конечные элементы степени 3 
   - Треугольные сетки
   
   **Верификация численного решения по значению циркуляции**
    
   $\begin{aligned}
   \oint_{\gamma} \frac{\partial \psi}{\partial n}(\bm x)  d \bm x 
   \end{aligned}$  
    
   """  
