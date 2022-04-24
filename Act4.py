import numpy as np
from scipy import  signal
import matplotlib.pyplot as plt

u = lambda t: np.piecewise(t,t>=0,[1,0])

#variables de proporcionalidad y corrimiento

corr= int(input("Ingrese el factor de corrimiento (ej:1600):"))

prop = int(input("Ingrese el factor de proporcionalidad :"))

#variable tiempo
t=np.linspace(0 , 1000 , 1000 , endpoint=True)
t2=np.arange(-10,10,0.01)

#Onda Senoidal
senoidal=np.sin((2*np.pi*5*t)+corr)

#Onda Cuadrada
cuadrada= signal.square((2*np.pi*5*t)+corr)

#Onda Triangular
triangular= signal.sawtooth((2*np.pi*5*t)+corr,width=0.5)

#Onda Dientes de Sierra
d_sierra= signal.sawtooth((2*np.pi*5*t)+corr)

#Exponencial decreciente
exp_dec = np.exp(-t2)*(u(t2)-u(t2-1))

#Exponencial creciente
exp_crec = np.exp(t2)*(u(t2)-u(t2-1))

#Impulso
impulso=(u(t2)-u(t2-0.01))

#Escalon
escalon=u(t2)

#Seno cardinal
senc=np.sinc(t2)

#Convluciones
#========================================================================

#Exponencial decreciente - cuadrada
conv11= (signal.convolve(cuadrada,exp_dec,mode='same')/sum(exp_dec))*prop

#Exponencial decreciente - senoidal
conv12= (signal.convolve(senoidal ,exp_dec,mode='same')/sum(exp_dec))*prop

#Exponencial decreciente - dientes de cierra
conv13= (signal.convolve(d_sierra,exp_dec,mode='same')/sum(exp_dec))*prop

#Exponencial decreciente - triangular
conv14= (signal.convolve(triangular,exp_dec,mode='same')/sum(exp_dec))*prop

#========================================================================

#Exponencial decreciente - cuadrada
conv21= signal.convolve(cuadrada,exp_crec,mode='same')*prop

#Exponencial decreciente - senoidal
conv22= signal.convolve(senoidal,exp_crec,mode='same')*prop

#Exponencial decreciente - dientes de cierra
conv23= signal.convolve(d_sierra,exp_crec,mode='same')*prop

#Exponencial decreciente - triangular
conv24= signal.convolve(triangular,exp_crec,mode='same')*prop

#========================================================================

#Impulso - cuadrada
conv31= signal.convolve(cuadrada,impulso,mode='same')*prop

#Impulso - senoidal
conv32= signal.convolve(senoidal ,impulso,mode='same')*prop

#Impulso - dientes de cierra
conv33= signal.convolve(d_sierra,impulso,mode='same')*prop

#Impulso - triangular
conv34= signal.convolve(triangular,impulso,mode='same')*prop

#========================================================================

#Escalon - cuadrada
conv41= signal.convolve(cuadrada,escalon,mode='same')*prop

#Escalon - senoidal
conv42= signal.convolve(senoidal ,escalon,mode='same')*prop

#Escalon - dientes de cierra
conv43= signal.convolve(d_sierra,escalon,mode='same')*prop

#Escalon - triangular
conv44= signal.convolve(triangular,escalon,mode='same')*prop

#========================================================================

#Senc - cuadrada
conv51= signal.convolve(cuadrada,senc,mode='same')*prop

#Senc - senoidal
conv52= signal.convolve(senoidal ,senc,mode='same')*prop

#Senc - dientes de cierra
conv53= signal.convolve(d_sierra,senc,mode='same')*prop

#Senc - triangular
conv54= signal.convolve(triangular,senc,mode='same')*prop

#========================================================================

#Graficas Convolucion Exponencial Decreciente
fig, (ax_exd,ax_cos,ax_sqr, ax_triang ,ax_sw) = plt.subplots( 5, 1, sharex=False , constrained_layout=True) 
fig.suptitle('Convolucion de Exponencial Decreciente', fontsize=16)
ax_exd.plot(t2,exp_dec)
ax_exd.set_title('Función Exponencial decreciente')
ax_exd.margins(0,0.1)
ax_cos.plot(conv12)
ax_cos.set_title('Señal Senoidal.')
ax_cos.margins(0,0.1)
ax_sqr.plot(conv11)
ax_sqr.set_title('Señal Cuadrada.')
ax_sqr.margins(0,0.1)
ax_triang.plot(conv13)
ax_triang.set_title('Señal Triangular')
ax_triang.margins(0,0.1)
ax_sw.plot(conv14)
ax_sw.set_title('Señal Diente de Sierra')
ax_sw.margins(0,0.1)

#========================================================================

#Graficas Convolucion Exponencial Creciente
fig, (ax_crec,ax_cos,ax_sqr, ax_triang ,ax_sw) = plt.subplots( 5, 1, sharex=False , constrained_layout=True) 
fig.suptitle('Convolucion de Exponencial Creciente', fontsize=16)
ax_crec.plot(t2,exp_crec)
ax_crec.set_title('Función Exponencial Creciente')
ax_crec.margins(0,0.1)
ax_cos.plot(t,conv22)
ax_cos.set_title('Señal Senoidal.')
ax_cos.margins(0,0.1)
ax_sqr.plot(t,conv21)
ax_sqr.set_title('Señal Cuadrada.')
ax_sqr.margins(0,0.1)
ax_triang.plot(conv23)
ax_triang.set_title('Señal Triangular')
ax_triang.margins(0,0.1)
ax_sw.plot(conv24)
ax_sw.set_title('Señal Diente de Sierra')
ax_sw.margins(0,0.1)

#========================================================================

#Graficas Convolucion Impulso
fig, (ax_imp,ax_cos,ax_sqr, ax_triang ,ax_sw) = plt.subplots( 5, 1, sharex=False , constrained_layout=True) 
fig.suptitle('Convolucion de Impulso', fontsize=16)
ax_imp.plot(t2,impulso)
ax_imp.set_title('Función Impulso')
ax_imp.margins(0,0.1)
ax_cos.plot(conv32)
ax_cos.set_title('Señal Senoidal.')
ax_cos.margins(0,0.1)
ax_sqr.plot(conv31)
ax_sqr.set_title('Señal Cuadrada.')
ax_sqr.margins(0,0.1)
ax_triang.plot(conv33)
ax_triang.set_title('Señal Triangular')
ax_triang.margins(0,0.1)
ax_sw.plot(conv34)
ax_sw.set_title('Señal Diente de Sierra')
ax_sw.margins(0,0.1)

#========================================================================

#Graficas Convolucion Escalon
fig, (ax_esc,ax_cos,ax_sqr, ax_triang ,ax_sw) = plt.subplots( 5, 1, sharex=False , constrained_layout=True) 
fig.suptitle('Convolucion de Escalon', fontsize=16)
ax_esc.plot(t2,escalon)
ax_esc.set_title('Función Escalon')
ax_esc.margins(0,0.1)
ax_cos.plot(conv42)
ax_cos.set_title('Señal Senoidal.')
ax_cos.margins(0,0.1)
ax_sqr.plot(conv41)
ax_sqr.set_title('Señal Cuadrada.')
ax_sqr.margins(0,0.1)
ax_triang.plot(conv43)
ax_triang.set_title('Señal Triangular')
ax_triang.margins(0,0.1)
ax_sw.plot(conv44)
ax_sw.set_title('Señal Diente de Sierra')
ax_sw.margins(0,0.1)

#========================================================================

#Graficas Convolucion Senc
fig, (ax_senc,ax_cos,ax_sqr, ax_triang ,ax_sw) = plt.subplots( 5, 1, sharex=False , constrained_layout=True) 
fig.suptitle('Convolucion de Seno cardinal', fontsize=16)
ax_senc.plot(t2,senc)
ax_senc.set_title('Función Seno cardinal')
ax_senc.margins(0,0.1)
ax_cos.plot(conv52)
ax_cos.set_title('Señal Senoidal.')
ax_cos.margins(0,0.1)
ax_sqr.plot(conv51)
ax_sqr.set_title('Señal Cuadrada.')
ax_sqr.margins(0,0.1)
ax_triang.plot(conv53)
ax_triang.set_title('Señal Triangular')
ax_triang.margins(0,0.1)
ax_sw.plot(conv54)
ax_sw.set_title('Señal Diente de Sierra')
ax_sw.margins(0,0.1)

plt.show()