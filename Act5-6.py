import numpy as np
from scipy import  signal
import matplotlib.pyplot as plt
import scipy.integrate as integrate

u = lambda t: np.piecewise(t,t>=0,[1,0])

#variable tiempo
t=np.linspace(0,1,1000 , endpoint=True)
t2=np.arange(-10,10,0.01)
periodo=2*np.pi+1

#Onda Senoidal
senoidal=np.sin(2*np.pi*5*t)

#Onda Cuadrada
cuadrada= signal.square(2*np.pi*5*t)

#Onda Triangular
triangular= signal.sawtooth(2*np.pi*5*t,width=0.5)

#Onda Dientes de Sierra
d_sierra= signal.sawtooth(2*np.pi*5*t)

#Impulso
impulso=(u(t2)-u(t2-0.01))

#Escalon
escalon=u(t2)

#Convluciones
#========================================================================

#Impulso - cuadrada
conv31= signal.convolve(cuadrada,impulso,mode='same')

#Impulso - senoidal
conv32= signal.convolve(senoidal ,impulso,mode='same')

#Impulso - dientes de cierra
conv33= signal.convolve(d_sierra,impulso,mode='same')

#Impulso - triangular
conv34= signal.convolve(triangular,impulso,mode='same')

#Escalon - triangular
conv44= signal.convolve(d_sierra,escalon,mode='same')/sum(escalon)

#Calculo Energias y Potencias 
#========================================================================

energiacos = integrate.simps(abs(conv32)**2,t)
potenciacos = (1/periodo)*energiacos

energiasqr = integrate.simps(abs(conv31)**2,t)
potenciasqr = (1/periodo)*energiasqr

energiasw = integrate.simps(abs(conv33)**2,t)
potenciasw = (1/periodo)*energiasw

energiatriang = integrate.simps(abs(conv34)**2,t)
potenciatriang = (1/periodo)*energiatriang

energiaescalon = integrate.simps(abs(conv44)**2,t)
potenciaescalon = (1/periodo)*energiaescalon

#Graficos
#========================================================================
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv32)
ax.set_title('Señal Senoidal - Impulso.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiacos*1000,2))+' [KJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(round(potenciacos*1000,2))+' [KW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv31)
ax.set_title('Señal Cuadrada - Impulso.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiasqr*1000,2))+' [KJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(round(potenciasqr*1000,2))+' [KW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv33)
ax.set_title('Señal Triangular - Impulso.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiatriang*1000,2))+' [KJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(round(potenciatriang*1000,2))+' [KW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv34)
ax.set_title('Señal Diente de Sierra - Impulso.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiasw*1000,2))+' [KJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(round(potenciasw*1000,2))+' [KW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv44)
ax.set_title('Señal Diente de Sierra - Escalon.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiaescalon*1000,2))+' [KJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de un periodo = '+str(round(potenciaescalon*1000,2))+' [KW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
        
plt.show()