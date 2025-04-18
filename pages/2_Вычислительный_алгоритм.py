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
    \nabla^2 \psi (\bm x) = 0,
    \quad \bm x \in \Omega
    \end{aligned}$   
     

    **Краевые условия**

    $\begin{aligned}
    \psi(\bm x) &= x_1 \quad \bm x \in \Gamma_1 \\
    \psi(\bm x) &= x_1 \quad \bm x \in \Gamma_2 \\
    \psi(\bm x) &= \gamma \quad \bm x \in \Gamma_3 \\
    \frac{\partial \psi(\bm x)}{\partial n} &= 0 \quad \bm x \in \Gamma_3, \Gamma_4
    \end{aligned}$
    
    Равномерный поток $($скорость $\bm u = \{u_\infty, 0\})$ на $\Gamma_1$, $\Gamma_2$ 

    **Условие на границе обтекаемого тела**
    
    Условие непротекания
       
    $\begin{aligned}
    \psi (\bm x) = \gamma ,
    \quad \bm x \in \Gamma_3
    \end{aligned}$    
    
    Постоянная определятся из дополнительного условия -- постулат Жуковского — Чаплыгина
    
        """
        
if menu == "Вариационная формулировка": 
    r"""
    ##### Конечно-элементная аппроксимация
    
    **Интегро-дифференциальные равенства** 
    
    Найти $\psi(\bm x) \in V$ такое, что:

    $\begin{aligned}
    \int_{\Omega} \nabla \psi \cdot \nabla v \, dx = 0  
    \quad \bm x \in \Omega
    \end{aligned}$   
    
    для всех $v(\bm x) \in V$

   **Пространство функций:**

   $\begin{aligned}
   V = \{ \psi, v \in H^1(\Omega) \ | \ \psi(\bm x), v(\bm x) = x_1, \ \bm x \in \Gamma_1 \cup \Gamma_2, \ \psi(\bm x), v(\bm x) = \gamma,  \ \bm x \in \Gamma_3 \}
   \end{aligned}$

   **Конечно-элементная реализация:**

   - Лагранжевые конечные элементы степени 1, 2, 3 
   
    (конечные элементы имеют базис Лагранжа, т.е. интерполяция на конечных элементах полиномами Лагранжа)
   - Треугольные сетки
   
   **Верификация численного решения по значению циркуляции**
    
   $\begin{aligned}
   \oint_{\gamma} \frac{\partial \psi}{\partial n}(\bm x)  d \bm x 
   \end{aligned}$  
    
   """  
