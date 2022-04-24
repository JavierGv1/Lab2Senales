import numpy as np
from scipy import  signal
import matplotlib.pyplot as plt
import scipy.integrate as integrate

u = lambda t: np.piecewise(t,t>=0,[1,0])

#variable tiempo
t=np.linspace(0,1,1000 , endpoint=True)
t2=np.arange(-10,10,0.01)
periodo=2*np.pi

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

energiacos = round(integrate.simps(abs(conv32),t),3)
potenciacos = round((1/periodo)*energiacos,3)

energiasqr = round(integrate.simps(abs(conv31),t),3)
potenciasqr = round((1/periodo)*energiasqr,3)

energiasw = round(integrate.simps(abs(conv33),t),3)
potenciasw = round((1/periodo)*energiasw,3)

energiatriang = round(integrate.simps(abs(conv34),t),3)
potenciatriang = round((1/periodo)*energiatriang,2)

energiaescalon = round(integrate.simps(abs(conv44),t),3)
potenciaescalon = round((1/periodo)*energiaescalon,3)

#Graficos
#========================================================================
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv32)
ax.set_title('Señal Senoidal - Impulso.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(energiacos)+'[J]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(potenciacos)+'[W]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv31)
ax.set_title('Señal Cuadrada - Impulso.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(energiasqr)+'[J]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(potenciasqr)+'[W]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv33)
ax.set_title('Señal Triangular - Impulso.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(energiatriang)+'[J]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(potenciatriang)+'[W]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv34)
ax.set_title('Señal Diente de Sierra - Impulso.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(energiasw)+'[J]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(potenciasw)+'[W]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv44)
ax.set_title('Señal Diente de Sierra - Escalon.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(energiaescalon)+'[J]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de un periodo = '+str(potenciaescalon)+'[W]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
        
plt.show()
