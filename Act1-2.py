import numpy as np
from scipy import  signal
import matplotlib.pyplot as plt

u = lambda t: np.piecewise(t,t>=0,[1,0])

#variable tiempo
t=np.linspace(0 , 1, 500 , endpoint=True)
t2=np.arange(-4,4,0.01)

#Onda Senoidal
senoidal=np.sin(2*np.pi*5*t)

#Onda Cuadrada
cuadrada= signal.square(2*np.pi*5*t)

#Onda Triangular
triangular= signal.sawtooth(2*np.pi*5*t,width=0.5)

#Onda Dientes de Sierra
d_sierra= signal.sawtooth(2*np.pi*5*t)

#Exponencial decreciente
exp_dec = np.exp(-t2)*(u(t2)-u(t2-1))

#Exponencial creciente
exp_crec = np.exp(t2)*(u(t2)-u(t2-1))

#Impulso
impulso=u(t2)-u(t2-0.01)

#Escalon
escalon=u(t2)

#Seno cardinal
senc=np.sinc(t2)

#========================================================================

#Graficas Actividad 1
fig, (ax_cos,ax_sqr,ax_triang ,ax_sw) = plt.subplots( 4, 1, sharex=True , constrained_layout=True) 
fig.suptitle('Actividad 1', fontsize=16)
ax_cos.plot(t,senoidal)
ax_cos.set_title('Señal Senoidal.')
ax_cos.margins(0,0.1)
ax_sqr.plot(t,cuadrada)
ax_sqr.set_title('Señal Cuadrada.')
ax_sqr.margins(0,0.1)
ax_triang.plot(t,triangular)
ax_triang.set_title('Señal Triangular')
ax_triang.margins(0,0.1)
ax_sw.plot(t,d_sierra)
ax_sw.set_title('Señal Diente de Sierra')
ax_sw.margins(0,0.1)
ax_sw.set_xlabel('Segundos')
ax_sqr.set_ylabel('Metros')
ax_triang.set_ylabel('Metros')
ax_cos.set_ylabel('Metros')
ax_sw.set_ylabel('Metros')

#========================================================================

#Graficas Actividad 2
fig, (ax_exd,ax_exc,ax_imp,ax_esc,ax_senc) = plt.subplots( 5, 1, sharex=True, constrained_layout=True)
fig.suptitle('Actividad 2', fontsize=16)
ax_exd.plot(t2,exp_dec)
ax_exd.set_title('Función Exponencial decreciente')
ax_exd.margins(0,0.1)
ax_exc.plot(t2,exp_crec)
ax_exc.set_title('Función Exponencial creciente')
ax_exc.margins(0,0.1)
ax_imp.plot(t2,impulso)
ax_imp.set_title('Función Impulso')
ax_imp.margins(0,0.1)
ax_esc.plot(t2,escalon)
ax_esc.set_title('Función Escalon')
ax_esc.margins(0,0.1)
ax_senc.plot(t2,senc)
ax_senc.set_title('Función Seno Cardinal')
ax_senc.margins(0,0.1)
ax_esc.set_xlabel('Segundos')
ax_esc.set_ylabel('Metros')
ax_senc.set_ylabel('Metros')
ax_imp.set_ylabel('Metros')
ax_exc.set_ylabel('Metros')
ax_exd.set_ylabel('Metros')
plt.show()