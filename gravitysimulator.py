pi = 3.14159265
G = 6.67408*(10**(-11))

#some fundamental operations:

def factorial(n):
	if n == 0:
		return 1
	if n != 0:
		return n*factorial(n-1)

def module(a):
	d = 0
	for i in a:
		d = d + i**2
	e = d**0.5
	return e

def dotprod(a,b):
	d = 0
	for i in a:
		c = i * b[a.index(i)]
		d = d + c
	return d

def cosine(a,b):
	return dotprod(a,b)/(module(a)*module(b))

def sine(a,b):
	return (1-(cosine(a,b))**2)**0.5

def sin(angle):
	while angle>(2*pi):
		angle = angle - (2*pi)
	while angle<0:
		angle = angle + (2*pi)
	if 0<=angle<=(2*pi):
		return angle-((angle**3)/factorial(3))+((angle**5)/factorial(5))-((angle**7)/factorial(7))+((angle**9)/factorial(9))-((angle**11)/factorial(11))+((angle**13)/factorial(13))-((angle**15)/factorial(15))+((angle**17)/factorial(17))-((angle**19)/factorial(19))+((angle**21)/factorial(21))

def cos(angle):
	while angle>(2*pi):
		angle = angle - (2*pi)
	while angle<0:
		angle = angle + (2*pi)
	if 0<=angle<=(2*pi):
		return 1-((angle**2)/factorial(2))+((angle**4)/factorial(4))-((angle**6)/factorial(6))+((angle**8)/factorial(8))-((angle**10)/factorial(10))+((angle**12)/factorial(12))-((angle**14)/factorial(14))+((angle**16)/factorial(16))-((angle**18)/factorial(18))+((angle**20)/factorial(20))-((angle**22)/factorial(22))

def mod(a):
	if a>=0:
		return a
	if a<0:
		return -a

#finally, the orbit:
def find_orbit():
	print("Welcome to our program! All units on S.I. and please give us the initial conditions! We take the origin to be the center of mass, our coordinates are orthonormal")
	#initial conditions:
	m_1 = eval(input("Mass of the first object (kg): ", ))
	m_2 = eval(input("Mass of the second object (kg): ", ))

	t = eval(input("Time (s): ", ))

	x_1 = eval(input("X coordinate of first object (m): ", ))
	y_1 = eval(input("Y coordinate of first object (m): ", ))
	z_1 = eval(input("Z coordinate of first object (m): ", ))
	r_1 = [x_1,y_1,z_1]

	x_2 = -(m_1/m_2)*x_1
	y_2 = -(m_1/m_2)*y_1
	z_2 = -(m_1/m_2)*z_1
	r_2 = [x_2,y_2,z_2]

	vx_1 = eval(input("X velocity of first object (m/s): ", ))
	vy_1 = eval(input("Y velocity of first object (m/s): ", ))
	vz_1 = eval(input("Z velocity of first object (m/s): ", ))
	v_1 = [vx_1,vy_1,vz_1]

	vx_2 = -(m_1/m_2)*vx_1
	vy_2 = -(m_1/m_2)*vy_1
	vz_2 = -(m_1/m_2)*vz_1
	v_2 = [vx_2,vy_2,vz_2]

	#fundamental and definitional derivations:
	m_red = (m_1 * m_2)/(m_1 + m_2)

	#trial: loop for variation of quantities
	timepass = 0
	dt = t/200000
	while t>=timepass and t!=0:
		x_2 = x_2 + vx_2*dt
		vx_2 = vx_2 - (G*m_1*(x_1-x_2)/((mod(x_1-x_2))**3))*dt
		x_1 = x_1 + vx_1*dt
		vx_1 = vx_1 + (G*m_2*(x_1-x_2)/((mod(x_1-x_2))**3))*dt

		y_2 = y_2 + vy_2*dt
		vy_2 = vy_2 - (G*m_1*(y_1-y_2)/((mod(y_1-y_2))**3))*dt
		y_1 = y_1 + vy_1*dt
		vy_1 = vy_1 + (G*m_2*(y_1-y_2)/((mod(y_1-y_2))**3))*dt

		z_2 = z_2 + vz_2*dt
		vz_2 = vz_2 - (G*m_1*(z_1-z_2)/((mod(z_1-z_2))**3))*dt
		z_1 = z_1 + vz_1*dt
		vz_1 = vz_1 + (G*m_2*(z_1-z_2)/((mod(z_1-z_2))**3))*dt

		timepass = timepass + dt

	L_1 = m_1*module(r_1)*module(v_1)*sine(r_1,v_1)
	L_2 = m_2*module(r_2)*module(v_2)*sine(r_2,v_2)

	return(print(
		"\nObject 1: ",
		"\n X: ",x_1,"m",
		"\n Y: ",y_1,"m",
		"\n Z: ",z_1,"m",
		"\n Vel. X: ",vx_1,"m/s",
		"\n Vel. Y: ",vy_1,"m/s",
		"\n Vel. Z: ",vz_1,"m/s",
		"\n Angular Momentum: ",L_1,"kg*m^2*s^−1",
		"\n\n Radius of the orbit:",module(r_1),"m",
		"\nObject 2: ",
		"\n X: ",x_2,"m",
		"\n Y: ",y_2,"m",
		"\n Z: ",z_2,"m"
		"\n Vel. X: ",vx_2,"m/s",
		"\n Vel. Y: ",vy_2,"m/s",
		"\n Vel. Z: ",vz_2,"m/s",
		"\n Angular Momentum: ",L_2,"kg*m^2*s^−1"
		"\n\n Radius of the orbit:", module(r_2),"m"))

find_orbit()
