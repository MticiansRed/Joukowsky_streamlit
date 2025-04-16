import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d
from matplotlib.colors import Normalize
import subprocess
import sys
menu = st.sidebar.radio('***',
	(
	"Функция Жуковского",
	"Метод конформных отображений",
	"Функция тока и скорости",
	"Решение в Python"
	)
)
#st.title("Аналитическое решение")

if menu == "Функция Жуковского":
	r"""
##### Метод конформных отображений

* Функция Жуковского

$\begin{aligned}
z = \frac{1}{2}(t+\frac{c^2}{t^2})
\end{aligned}$
	"""

	st.image("pages/figs/analytic_fig1.png")

	st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
	r"""
	Источник: Маклаков Д.В.
	Аналитические методы гидродинамики. Часть 1. Крыловой профиль в
	плоскопараллельном потоке. Учебное пособие / Д.В. Маклаков. – Казань:
	Казан. ун-т, 2020. – 59 с.
	"""

if menu == "Метод конформных отображений":
	r"""
##### Метод конформных отображений
	"""
	st.image("pages/figs/analytic_fig2.png", width = 300)
	r"""

Для решения задачи потенциального обтекания профиля Жуковского достаточно решить задачу 
циркуляционного обтекания цилиндра в параметрической плоскости, выразив координаты параметрической плоскости с помощью обратного преобразования Жуковского:

$\begin{aligned}
w = u_{\infty}(e^{-i \alpha}t+\frac{e^i \alpha}{t})+\frac{\Gamma}{2 \pi i}\ln{t}
\end{aligned}$,

где $a = \sqrt{c^2+h^2}+d$ -- радиус параметрической окружности.
$t$ выражается из обратного преобразования Жуковского:
* $t = z + \sqrt{z^2-c^2} - t_0$ если $\operatorname{Re}(t)^2+\operatorname{Im}(t)^2 \geq a^2$ (верхняя полуплоскость, внешность профиля)
* $t = z - \sqrt{z^2-c^2} - t_0$ если $\operatorname{Re}(t)^2+\operatorname{Im}(t)^2 < a^2$ (нижняя полуплоскость, внутренность профиля)

$t_0$ -- центр координат параметрической плоскости в системе координат физической.

* Циркуляция $\Gamma = -2\pi a u_{\infty} \operatorname{sin}(\alpha+\sigma)$

Выражается из $\frac{\mathrm{d}w}{\mathrm{d}z} |_{t_B} = 0 $, $\hspace{2mm}$ $t_B = ae^{-i\sigma}$ -- точка схода потока
(из постулата Жуковского-Чаплыгина)


	"""
	st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
	r"""
	Источник: Маклаков Д.В.
	Аналитические методы гидродинамики. Часть 1. Крыловой профиль в
	плоскопараллельном потоке. Учебное пособие / Д.В. Маклаков. – Казань:
	Казан. ун-т, 2020. – 59 с.
	"""
	
if menu == "Функция тока и скорости":
	r"""
##### Функция тока и скорости
Используем полученный комплексный потенциал $w$:
* Функция тока $\psi = \operatorname{Im}(w)$
* Скорость по $x$: $u_x = \operatorname{Re}\left(\frac{\mathrm{d}w}{\mathrm{d}z}\right)$
* Скорость по $y$: $u_y = -\operatorname{Im}\left(\frac{\mathrm{d}w}{\mathrm{d}z}\right)$


	"""
	st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
	r"""
	Источник: Маклаков Д.В.
	Аналитические методы гидродинамики. Часть 1. Крыловой профиль в
	плоскопараллельном потоке. Учебное пособие / Д.В. Маклаков. – Казань:
	Казан. ун-т, 2020. – 59 с.
	"""
if menu == "Решение в Python":
	r"""
##### Решение задачи потенциального обтекания профиля Жуковского аналитически в Python
	"""
	class Joukowsky_transform:
		def __init__(self, c, a, t_0):
			print("Joukowsky_transform initialized.")
			self.c = c
			self.a = a
			self.t_0 = t_0
		def __call__(self, t):
			epsc = 1e-15+1j*1e-15
			z = 0.5*(t+self.t_0+self.c**2/(t+self.t_0+epsc)) 
			print("Joukowsky transform (t -> z) result z: ")
			print(z)
			return z
		def inverse(self, z):
			#zmc = 1j*np.sqrt(self.c-z)*np.sqrt(self.c+z) !!! Correct upper part!
			#zmc = np.sqrt(z-self.c)*np.sqrt(z+self.c) !!! Another good one!
			zmc = 1j*np.sqrt(self.c-z)*np.sqrt(self.c+z)
			t = (z + zmc - self.t_0)
			t = np.where(np.real(t)**2+np.imag(t)**2>=self.a**2,  (z + zmc - self.t_0), (z - zmc - self.t_0)) #??? why this even works???
			print("Inverse Joukowsky transform (z -> t) result t: ")
			print(t)
			return  t
	class Joukowsky_airfoil_flow_potential:
		def __init__(self, u_inf, alpha, a, Gamma):
			print("Joukowsky_airfoil_flow_potential initialized.")
			self.u_inf = u_inf
			self.alpha = alpha
			self.a = a
			self.Gamma = Gamma
		def __call__(self, t):
			epsc = 1e-15+1j*1e-15
			w = 0.5*self.u_inf*(np.exp(-1*1j*self.alpha)*t+(np.exp(1j*self.alpha)*self.a**2)/t)+( self.Gamma/(2*np.pi*1j) )*np.log(t+epsc) #calculating flow potential 
			w = np.where( np.real(t)**2+np.imag(t)**2<self.a**2, 0.0+1j*0.0, w) #zeroing inner part of parametric circle
			print("Flow potential calculation result w: ")
			print(w)
			return w

	def circle(X, Y, x_c, y_c, c, h, d): #make circle in parametric plane
		a = np.sqrt(c**2+h**2)+d
		Y_pos = np.sqrt(a**2-(X-x_c)**2)+y_c
		Y_neg = -np.sqrt(a**2-(X-x_c)**2)+y_c
		#plt.scatter(x_c,y_c, c = 'g')
		return [Y_neg, Y_pos]
	def Joukowsky(X, Y, c, attack):
		Z = X + 1j*Y #Create parametric plane
		JT = Joukowsky_transform(c, 0.0, 0.0) #Apply conformal map
		Z_J = JT(Z)
		Z_J = Z_J*np.exp(1j*attack)
		Re_Z_J = np.real(Z_J)
		Im_Z_J = np.imag(Z_J)
		return [Re_Z_J, Im_Z_J]

	def airfoil(c, h, d, attack):
		print("Plotting airfoil:")
		a = np.sqrt(c**2+h**2)+d
		sigma = np.arctan(h/c)
		x_c = c - a*np.cos(sigma)
		y_c = a*np.sin(sigma)
		X = np.linspace(x_c-a, x_c+a, 1000) #parametric plane mesh
		Y = np.linspace(y_c-a, y_c+a, 1000)
		
		Y_circle = circle(X, Y, x_c, y_c, c, h, d)
		Re_Z_J_pos = Joukowsky(X, Y_circle[1], c, attack)[0] #apply conformal map to upper part of circle
		Im_Z_J_pos = Joukowsky(X, Y_circle[1], c, attack)[1]
		
		Re_Z_J_neg = Joukowsky(X, Y_circle[0], c, attack)[0] #apply conformal map to lower part of circle
		Im_Z_J_neg = Joukowsky(X, Y_circle[0], c, attack)[1]
		
		#print("y_pos")
		#print(Y_circle[1])
		#print("y_neg")
		#print(Y_circle[0])

		#plt.axis('equal')
		#plt.plot(X, Y_circle[0], "r--", alpha = 0.5)
		#plt.plot(X, Y_circle[1], "b--", alpha = 0.5)
		plt.plot(Re_Z_J_neg, Im_Z_J_neg, color ="black")
		plt.plot(Re_Z_J_pos, Im_Z_J_pos, color ="black")

	def flow(c, h, d, u_inf, alpha):
		print("Calculating flow:")
		a = np.sqrt(c**2+h**2)+d
		sigma = np.arctan(h/c)
		Gamma = -2*np.pi*a*u_inf*np.sin(alpha+sigma)
		print("Circulation Г = ", Gamma)
		st.markdown(f"Циркуляция $\Gamma = {Gamma}$")
		x_c, y_c = (c - a*np.cos(sigma)), a*np.sin(sigma) #x_c, y_c -- coordinates of t' coord system zero in t
		
		#---Initializing parametrical plane t'--- 
		k = 2.0 #modifier for size of domain
		T1_x = np.linspace(x_c-k*a, x_c+k*a, 1000) #create parametrical plane t'
		T1_y = np.linspace(y_c-k*a, y_c+k*a, 1000)  
		T1_xmesh, T1_ymesh = np.meshgrid(T1_x, T1_y)
		T1_mesh = T1_xmesh + 1j*T1_ymesh
		t_0 = 1j*h+d*np.exp(1j*(np.pi-sigma))
		w = Joukowsky_airfoil_flow_potential(u_inf, alpha, a, Gamma) #initialize flow potential function in parametric plane t'
		J = Joukowsky_transform(c, a, t_0) # initialize Joukowsky transform t --> z
		
		#---Calculating flow potential in parametrical plane---
		#W_mesh = w(T1_mesh) #Obtain flow potential in parametric plane
		#Psi_param = np.imag(W_mesh)
		#plt.contour(T1_xmesh+np.real(t_0), T1_ymesh+np.imag(t_0), Psi_param, levels=100, cmap='viridis') #Solution in parametric plane, shifted to t plane.
		#plt.pcolormesh(T1_xmesh, T1_ymesh, Psi_param, shading='auto', cmap='viridis', vmin=-5, vmax=5)
		
		#---Calculating critical points in parametrical plane---
		z_1_param = ( -1*Gamma/(2*np.pi*1j) + np.sqrt( -1*Gamma**2/(4*np.pi**2) + u_inf**2*a**2 +1j*0.0))*np.exp(1j*alpha)*(1/u_inf)
		z_2_param = ( -1*Gamma/(2*np.pi*1j) - np.sqrt( -1*Gamma**2/(4*np.pi**2) + u_inf**2*a**2 +1j*0.0))*np.exp(1j*alpha)*(1/u_inf)
		
		#---Initilizing physical plane z---
		Z_mesh = T1_mesh
		#Z_mesh = T1_mesh+t_0 #z plane has same origin as t ??? why adding t_0 is not needed???
		Z_xmesh = np.real(Z_mesh)
		Z_ymesh = np.imag(Z_mesh)
		
		#---Calculating flow potential in physical plane---
		W_phys_mesh = w(J.inverse(Z_mesh)) #Obtain flow potential in physical plane.
		Psi_phys = np.imag(W_phys_mesh)
		plt.contour(Z_xmesh, Z_ymesh, Psi_phys, levels=100, colors = 'black', linestyles='solid', linewidths = 0.5) #Solution in parametric plane, shifted to t plane.
		#plt.pcolormesh(Z_xmesh, Z_ymesh, Psi_phys, shading='auto', cmap='viridis')
		#plt.colorbar()
		
		#---Calculating velocity field (p. 8, p. 17 Maklakov)---
		dz = 1e-10+1j*1e-10
		dW_phys_mesh = w(J.inverse(Z_mesh+dz))-W_phys_mesh #f(z+h)-f(z)
		dWdz_phys_mesh = dW_phys_mesh/dz #(f(z+h)-f(z))/h
		u_x = np.real(dWdz_phys_mesh)
		u_y = -1*np.imag(dWdz_phys_mesh)
		u_mag = np.sqrt(u_x**2+u_y**2)
		plt.pcolormesh(Z_xmesh, Z_ymesh, u_mag, shading='auto', cmap='viridis')
		plt.colorbar(label = "Скорость")
		stride = 25
		plt.quiver(Z_xmesh[::stride, ::stride], Z_ymesh[::stride, ::stride], u_x[::stride, ::stride], u_y[::stride, ::stride], width = 0.001)
		
		#---Calculating critical points in physical plane---
		if (Gamma > 4*np.pi*u_inf):
			print("Case Gamma > 4*np.pi*u_inf")
			z_1 = J(z_1_param) #Mapping to physical plane after evaluating
			z_2 = J(z_2_param) #Mapping to physical plane after evaluating
		if (Gamma == 4*np.pi*u_inf):
			print("Case Gamma == 4*np.pi*u_inf")
			z_1 = J(z_1_param)
			z_2 = z_1 #z_2 and z_1 are multiple roots
		if (Gamma < 4*np.pi*u_inf):
			print("Case Gamma < 4*np.pi*u_inf")
			z_1 = J(z_1_param) #Mapping to physical plane after evaluating
			z_2 = J(z_2_param) #Mapping to physical plane after evaluating
		
		plt.scatter(np.real(z_1), np.imag(z_1), color = "r")
		plt.scatter(np.real(z_2), np.imag(z_2), color = "b")


		return 0

	def main(args, k):
		da = {"deg":args[0], "c": args[1], "h": args[2], "d": args[3]}
		print("Arguments:\n", da)
		deg = da["deg"]
		c = da["c"]
		h = da["h"]
		d = da["d"]

		a = np.sqrt(c**2+h**2)+d
		sigma = np.arctan(h/c)
		x_c = c - a*np.cos(sigma)
		y_c = a*np.sin(sigma)
		

		angle = deg*np.pi/180
		print("Angle = ", angle, " rad.")
		fig = plt.figure()
		plt.xlim(xmin=x_c-k*a, xmax = x_c+k*a )
		plt.ylim(ymin=y_c-k*a, ymax=y_c+k*a )
		#plt.grid()
		flow(c, h, d, 1.0, angle)
		airfoil(c, h, d, 0.0)
		#c1, c2, = st.columns([5,1])
		c1.pyplot(fig) 

	#c1, c2, = st.columns([15,5])
	#degree = c2.slider("Угол атаки", -90, 90, 0)
	#c = c2.slider("c", 0.0, 2.0, 1.2)
	#h = c2.slider("h", 0.0, 1.0, 0.2)
	#d = c2.slider("d", 0.0, 1.0, 0.1)

	if 'default_values' not in st.session_state:
		st.session_state.default_values = {
			'degree': 0,
			'c': 1.0,
			'h': 0.1,
			'd': 0.05,
			'k': 2.0
		}

	for key in st.session_state.default_values:
		if key not in st.session_state:
			st.session_state[key] = st.session_state.default_values[key]

	if 'case1' not in st.session_state:
		st.session_state.case1 = {
			'degree': 0,
			'c': 1.0,
			'h': 0.0,
			'd': 0.1,
			'k': 2.0
		}

	for key in st.session_state.case1:
		if key not in st.session_state:
			st.session_state[key] = st.session_state.case1[key]


	if 'case2' not in st.session_state:
		st.session_state.case2 = {
			'degree': 0,
			'c': 1.0,
			'h': 0.1,
			'd': 0.05,
			'k': 2.0
		}

	for key in st.session_state.case2:
		if key not in st.session_state:
			st.session_state[key] = st.session_state.case2[key]

	if 'case3' not in st.session_state:
		st.session_state.case3 = {
			'degree': 15.0,
			'c': 1.0,
			'h': 0.1,
			'd': 0.05,
			'k': 2.0
		}

	for key in st.session_state.case3:
		if key not in st.session_state:
			st.session_state[key] = st.session_state.case3[key]

	if 'case4' not in st.session_state:
		st.session_state.case4 = {
			'degree': 20.0,
			'c': 1.0,
			'h': 0.2,
			'd': 0.1,
			'k': 2.0
		}

	for key in st.session_state.case4:
		if key not in st.session_state:
			st.session_state[key] = st.session_state.case4[key]


	def reset_sliders():
		for key in st.session_state.default_values:
			st.session_state[key] = st.session_state.default_values[key]
	def set_case1():
		for key in st.session_state.case1:
			st.session_state[key] = st.session_state.case1[key]
	def set_case2():
		for key in st.session_state.case2:
			st.session_state[key] = st.session_state.case2[key]
	def set_case3():
		for key in st.session_state.case3:
			st.session_state[key] = st.session_state.case3[key]
	def set_case4():
		for key in st.session_state.case4:
			st.session_state[key] = st.session_state.case4[key]

	a0, a1, a2, a3, a4 = st.columns([5,5,5,5,5])
	a1.button("Случай 1", on_click=set_case1)
	a2.button("Случай 2", on_click=set_case2)
	a3.button("Случай 3", on_click=set_case3)
	a4.button("Случай 4", on_click=set_case4)
	c1, c2 = st.columns([15, 5])

	with c2:
		#st.button("Случай 1", on_click=set_case1)
		#st.button("Случай 2", on_click=set_case2)
		#st.button("Случай 3", on_click=set_case3)
		#st.button("Случай 4", on_click=set_case4)
		degree = st.slider("Угол атаки", -45, 45, key='degree')
		c = st.slider("c", 0.0, 2.0, key='c')
		h = st.slider("h", 0.0, 1.0, key='h')
		d = st.slider("d", 0.0, 1.0, key='d')
		k = st.slider("k, множитель масштаба", 0.1, 2.0, key='k')
		st.button("Сбросить значения", on_click=reset_sliders)

	args = [float(degree), c, h, d] #default args
	if a0.button("Построить"):
		main(args, k)
