import streamlit as st
import os
from PIL import Image
import pandas as pd

#st.set_page_config(layout="wide")
 
menu = st.sidebar.radio('***',
    ("Фрагменты кода", 
    "Визуализации решений",       
    "Расчет циркуляции",
    )
)

if menu == "Фрагменты кода":
    r"""
    ##### Фрагменты кода 
    
    **Параметры профиля из командной строки**

    """
    
    code = """  
    # python3 joukowsky_fenics.py 15.0 1.0 0.1 0.05 196 - пример запуска
    # Название профиля и число разбиений div указаны в названиях xml файлов (и geo, и msh файлов)
    # Список профилей и параметров
    # profile*номер* = [угол атаки, c, h, d]
    # profile1 = [0.0, 1.0, 0.0, 0.1]
    # profile2 = [0.0, 1.0, 0.1, 0.05]
    # profile2 = [15.0, 1.0, 0.1, 0.05] 
    # profile3 = [20.0, 1.0, 0.2, 0.1]
    
    alpha = float(sys.argv[1])*np.pi/180 # Перевод градусов в радианы
    c = float(sys.argv[2])
    h = float(sys.argv[3])
    d = float(sys.argv[4])
    meshsize = int(sys.argv[5])
    ju.airfoil(c, h, d, alpha, meshsize) # Отрисовка профиля Жуковского 
    """ 
    st.code(code, language="python") 
    
    r"""   
    
    **Сетка**

    """
    
    code = """  
    # Загрузка сетки из файла .xml
    mesh = Mesh("jouk_geo_profile3_div196_angle20.0.xml")
    boundaries = MeshFunction("size_t", mesh, "jouk_geo_profile3_div196_angle20.0_facet_region.xml")

    ds = Measure("ds", subdomain_data=boundaries)
    deg = 3 # Степень аппроксимирующих полиномов
    """ 
    st.code(code, language="python") 
    
    r"""   
    
    **Информации о сетке и числе искомых величин**

    """
    
    code = """  
    n_c = mesh.num_cells()
    n_v = mesh.num_vertices()
    n_d = V.dim()
    n = FacetNormal(mesh)  

    print(f"Число ячеек сетки: {n_c}")
    print(f"Число узлов сетки: {n_v}")
    print(f"Число искомых дискретных значений: {n_d}")

    gamma1_0 = 0.00 # профиль 1 угол атаки 0
    gamma2_0 = -0.232 #профиль 2 угол атаки 0
    gamma2_15 = -0.962 #профиль 2 угол атаки 15
    gamma3_20 = -1.431 #профиль 3 угол атаки 20

    gamma = gamma3_20 # Выбираем нужную константу в зависимости от профиля
    """ 
    st.code(code, language="python")  
      
    r"""
    
    **Конечные элементы**

    """
    
    code = """  
    # Определение функционального пространства
    V = FunctionSpace(mesh, "CG", deg)
    """ 
    st.code(code, language="python")  
      
    r"""
    
    **Граничные условия**
    
    """   
    code = """     
    # Условия на входе в канал
    u_l = Expression("x[1]", degree=deg)
    u_r = Expression("x[1]", degree=deg)

    # Граничные условия
    bcs1 = [DirichletBC(V, u_l, boundaries, 1),
        DirichletBC(V, u_r, boundaries, 2),
        DirichletBC(V, gamma, boundaries, 3)] # Константа gamma на границе профиля

    """    
    st.code(code, language="python") 
    
    r"""
    
    **Формулировка задачи**
    
    """  
    code = """   
    # Пробная и тестовая функции
    u = TrialFunction(V)
    v = TestFunction(V)
    f = Constant(0.0)    
    # Вариационная задача
    a = dot(grad(u), grad(v)) * dx
    L = f * v * dx # rhs = 0 i.e. f = 0
    """ 
    st.code(code, language="python")    
         
    r"""
    
    **Решение**
    
    """   
    code = """     
    # Решение задачи
    u1 = Function(V)
    solve(a == L, u1, bcs1)
    """ 
    st.code(code, language="python") 
       
    r"""
    
    **Циркуляция и вычисление скорости**
    
    """   
    code = """     
    #  Циркуляция 
    u_n = dot(grad(u1), n)  
    circ1 = assemble(u_n * ds(subdomain_data=boundaries, subdomain_id=3)) #Циркуляция по контуру профиля
    print(f"Циркуляция поля u1: {circ1:.5e}")
    # Вычисление скорости
    ksi = grad(u1)[0] # x-компонента скорости
    eta = -1*grad(u1)[1] # y-компонента скорости
    mag = sqrt(ksi**2+eta**2) # Модуль скорости 
    mag_project = project(mag, V) # Проекция на функциональное пространство 

    """ 
    st.code(code, language="python")    
    
    r"""
    
    **График**
    
    """   
    code = """     

    # Значения решений в узлах сетки
    u_values = u1.compute_vertex_values(mesh)

    plt.figure(1, figsize=(12, 12))

    velfield = plot(mag_project) #Поле скоростей
    plt.colorbar(velfield)
    isolines = plt.tricontour(x, y, triangles, u_values, levels=np.linspace(-10, 10, 500), colors='black', linestyles='solid', linewidths=0.5) #Линии тока

    # Отображение графика
    #plt.savefig('1.png', format="png", dpi=600)
    plt.show()
    """ 
    st.code(code, language="python") 
       

    

if menu == "Визуализации решений":
    r"""
    ##### Визуализации решений
    
    """
    IMAGE_DIR = "pages/figs"

    tab1, tab2, tab3 = st.tabs(["Профиль 1", "Профиль 2", "Профиль 3"])

    with tab1:
        
        div = st.selectbox("Число разбиений сетки:", [12, 48, 196], key="tab1_div")
        deg = st.selectbox("Степень аппроксимирующих полиномов:", [1, 2, 3], key="tab1_deg")
        angle = st.selectbox("Угол атаки:", [0], key="tab1_angle")
        
        img1_path = os.path.join(IMAGE_DIR, f"profile1_1_div{div}_deg{deg}.png")
        img2_path = os.path.join(IMAGE_DIR, f"profile1_2_div{div}_deg{deg}.png")
        
        st.image(Image.open(img1_path), use_container_width=True)
        st.image(Image.open(img2_path), use_container_width=True)

    with tab2:
        
        div = st.selectbox("Число разбиений сетки:", [196], key="tab2_div")
        deg = st.selectbox("Степень аппроксимирующих полиномов:", [1, 2, 3], key="tab2_deg")
        angle = st.selectbox("Угол атаки:", [0, 15], key="tab2_angle")
        
        img1_path = os.path.join(IMAGE_DIR, f"profile2_1_div{div}_deg{deg}_angle{angle}.png")
        img2_path = os.path.join(IMAGE_DIR, f"profile2_2_div{div}_deg{deg}_angle{angle}.png")
        
        st.image(Image.open(img1_path), use_container_width=True)
        st.image(Image.open(img2_path), use_container_width=True)

    with tab3:
        
        div = st.selectbox("Число разбиений сетки:", [196], key="tab3_div")
        deg = st.selectbox("Степень аппроксимирующих полиномов:", [1, 2, 3], key="tab3_deg")
        angle = st.selectbox("Угол атаки:", [20], key="tab3_angle")
        
        img1_path = os.path.join(IMAGE_DIR, f"profile3_1_deg{deg}.png")
        img2_path = os.path.join(IMAGE_DIR, f"profile3_2_deg{deg}.png")
        
        st.image(Image.open(img1_path), use_container_width=True)
        st.image(Image.open(img2_path), use_container_width=True)
        
        
if menu == "Расчет циркуляции":
    r"""
    ##### Расчет циркуляции
    
    """
    
    tab1, tab2, tab3 = st.tabs(["Профиль 1", "Профиль 2", "Профиль 3"])
    
    def format_circulation(value):
        return fr"""
        Описание таблицы:  
        Сетка (номер сетки $ - $ число узлов)  
        p $ - $ степень аппроксимирующих полиномов  
        
        Точное значение циркуляции: $\Gamma = {value:.5e}$
        """
    
    with tab1:

        data = {
            "Сетка": ["1 - 752", "2 - 1794", "3 - 4818"],
            "p = 1": ["5.44122e-04", "1.38165e-04", "1.26041e-04"],
            "p = 2": ["1.47168e-04", "8.68322e-05", "2.60052e-05"],
            "p = 3": ["8.30589e-05", "3.77206e-05", "-3.54880e-07"]      
        }
        df = pd.DataFrame(data)

        st.table(df)
        r"""
        Описание таблицы:  
        Сетка (номер сетки $ - $ число узлов)  
        p $ - $ степень аппроксимирующих полиномов  
        
        Точное значение циркуляции: $\Gamma = 0$
        """    
        
    with tab2:
        
        deg = st.selectbox("Угол атаки:", [0, 15], key="tab2_deg")
        
        if deg == 0:
            data = {
                "Сетка": ["4 - 5007"],
                "p = 1": ["-6.54220e-01"],
                "p = 2": ["-6.58311e-01"],
                "p = 3": ["-6.55881e-01"]      
            }
            gamma = -6.59579e-01
        else:  
            data = {
                "Сетка": ["5 - 5023"],
                "p = 1": ["-2.29214e+00"],
                "p = 2": ["-2.33769e+00"],
                "p = 3": ["-2.34485e+00"]      
            }
            gamma = -2.34422e+00
        
        df = pd.DataFrame(data)
        st.table(df)  
        st.markdown(format_circulation(gamma), unsafe_allow_html=True)  
        
    with tab3:
    
        data = {
            "Сетка": ["6 - 5400"],
            "p = 1": ["-3.58767e+00"],
            "p = 2": ["-3.64469e+00"],
            "p = 3": ["-3.64901e+00"]      
        }
        
        df = pd.DataFrame(data)
        st.table(df) 
        gamma = -3.65635e+00
        st.markdown(format_circulation(gamma), unsafe_allow_html=True)  
        
        
        
        
        
        
        
        
