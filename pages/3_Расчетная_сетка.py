import streamlit as st
import pandas as pd
menu = st.sidebar.radio('***',
	("Сетка в Gmsh", 
	"Параметры сеток",
	"Визуализации сетки",    
	)
)

if menu == "Сетка в Gmsh":
	r"""
	##### Сетка в Gmsh
	Пример сетки для первого профиля, число разбиений = 12

	"""
	
	code = """  
	//Lower part of profile
	Point(1) = {-1.016666666666667, -3.4722222222222284e-16, 0, 1.0};
	Point(2) = {-0.8571428571428577, -0.09035079029052503, 0, 1.0};
	Point(3) = {-0.694117647058824, -0.1123051946590396, 0, 1.0};
	Point(4) = {-0.5272727272727274, -0.11876313904403246, 0, 1.0};
	Point(5) = {-0.35625000000000007, -0.11575161985907534, 0, 1.0};
	Point(6) = {-0.1806451612903225, -0.1060108175816446, 0, 1.0};
	Point(7) = {4.1666666666666744e-16, -0.09128709291752735, 0, 1.0};
	Point(8) = {0.18620689655172468, -0.07298624306385054, 0, 1.0};
	Point(9) = {0.3785714285714291, -0.052489065916782374, 0, 1.0};
	Point(10) = {0.5777777777777782, -0.03142696805273576, 0, 1.0};
	Point(11) = {0.7846153846153847, -0.012162606385263564, 0, 1.0};
	//Upper part of profile
	Point(12) = {0.9999999999999994, -4.999999999999989e-16, 0, 1.0};
	Point(13) = {0.7846153846153838, 0.012162606385263341, 0, 1.0};
	Point(14) = {0.5777777777777773, 0.03142696805273604, 0, 1.0};
	Point(15) = {0.37857142857142845, 0.052489065916783095, 0, 1.0};
	Point(16) = {0.1862068965517243, 0.07298624306385149, 0, 1.0};
	Point(17) = {4.1666666666666576e-16, 0.09128709291752829, 0, 1.0};
	Point(18) = {-0.18064516129032218, 0.10601081758164549, 0, 1.0};
	Point(19) = {-0.3562499999999995, 0.115751619859076, 0, 1.0};
	Point(20) = {-0.5272727272727268, 0.1187631390440328, 0, 1.0};
	Point(21) = {-0.6941176470588232, 0.11230519465903965, 0, 1.0};
	Point(22) = {-0.8571428571428571, 0.0903507902905247, 0, 1.0};
	//Circle
	Point(23) = {8.0, 0.0, 0, 1.0};
	Point(24) = {0.0, 8.0, 0, 1.0};
	Point(25) = {-8.0, 0.0, 0, 1.0};
	Point(26) = {0.0, -8.0, 0, 1.0};
	Point(27) = {0.0, 0.0, 0, 1.0};
	//Profile lines
	Line(1) = {1, 2};
	Line(2) = {2, 3};
	Line(3) = {3, 4};
	Line(4) = {4, 5};
	Line(5) = {5, 6};
	Line(6) = {6, 7};
	Line(7) = {7, 8};
	Line(8) = {8, 9};
	Line(9) = {9, 10};
	Line(10) = {10, 11};
	Line(11) = {11, 12};
	Line(12) = {12, 13};
	Line(13) = {13, 14};
	Line(14) = {14, 15};
	Line(15) = {15, 16};
	Line(16) = {16, 17};
	Line(17) = {17, 18};
	Line(18) = {18, 19};
	Line(19) = {19, 20};
	Line(20) = {20, 21};
	Line(21) = {21, 22};
	Line(22) = {22, 1};
	//Creating profile curve loop
	lines_ind[] = {1 : 22};
	Curve Loop(1) = lines_ind[];
	Circle(23) = {24, 27, 26};
	Circle(24) = {26, 27, 24};
	Curve Loop(2) = {23};
	Curve Loop(3) = {24};
	//Creating plane
	Plane Surface(1) = {1, 2, 3};
	//Physical groups
	Physical Curve("Left") = {23};
	Physical Curve("Right") = {24};
	Physical Curve("Profile") = lines_ind[];
	Physical Surface("Domain") = {1};
	Mesh.Algorithm = 2;
	Mesh.MshFileVersion = 2.2;

	""" 
	st.code(code, language="gmsh") 
		
if menu == "Параметры сеток":
	r"""
	##### Параметры сеток
	
	"""

	data = {
		"Сетка": [1, 2, 3, 4, 5, 6],
		"Число разбиений": [12, 48, 196, 196, 196, 196],
		"Число ячеек": [1430, 3442, 9194, 9572, 9604, 10358],
		"Число узлов": [752, 1794, 4818, 5007, 5023, 5400]        
	}
	df = pd.DataFrame(data)

	st.table(df)
	

	
if menu == "Визуализации сетки":
	r"""
	##### Визуализации сетки
	
	"""
	
	tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Профиль 1, сетка 1", "Профиль 1, сетка 2", "Профиль 1, сетка 3", "Профиль 2, сетка 4", "Профиль 2, сетка 5", "Профиль 3, сетка 6"])

	with tab1: 
		st.image("pages/figs/mesh1.png", use_container_width=True)
	with tab2: 
		st.image("pages/figs/mesh2.png", use_container_width=True)
	with tab3: 
		st.image("pages/figs/mesh3.png", use_container_width=True)
	with tab4: 
		st.image("pages/figs/mesh4.png", use_container_width=True)
	with tab5: 
		st.image("pages/figs/mesh5.png", use_container_width=True)
	with tab6: 
		st.image("pages/figs/mesh6.png", use_container_width=True)
		
	tab1c, tab2c, tab3c, tab4c, tab5c, tab6c = st.tabs(["Профиль 1, сетка 1", "Профиль 1, сетка 2", "Профиль 1, сетка 3", "Профиль 2, сетка 4", "Профиль 2, сетка 5", "Профиль 3, сетка 6"])

	with tab1c: 
		st.image("pages/figs/mesh1c.png", use_container_width=True)
	with tab2c: 
		st.image("pages/figs/mesh2c.png", use_container_width=True)
	with tab3c: 
		st.image("pages/figs/mesh3c.png", use_container_width=True)
	with tab4c: 
		st.image("pages/figs/mesh4c.png", use_container_width=True)
	with tab5c: 
		st.image("pages/figs/mesh5c.png", use_container_width=True)
	with tab6c: 
		st.image("pages/figs/mesh6c.png", use_container_width=True)
