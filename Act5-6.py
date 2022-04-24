import numpy as np
from scipy import  signal
import matplotlib.pyplot as plt
import scipy.integrate as integrate

u = lambda t: np.piecewise(t,t>=0,[1,0])

#variable tiempo
t=np.arange(-10,10,0.01)
periodo=2*np.pi

#Exponencial decreciente
exp_dec = np.exp(-t)*(u(t)-u(t-1))

#Exponencial creciente
exp_crec = np.exp(t)*(u(t)-u(t-1))

#Impulso
impulso=u(t)-u(t-0.01)

#Escalon
escalon=u(t)

#Seno cardinal
senc=np.sinc(t)

#Convluciones
#========================================================================

#Exponencial decreciente - Exponencial creciente
conv1= signal.convolve(exp_dec,exp_crec,mode='same')/sum(exp_dec)

#Exponencial creciente - Impulso
conv2= signal.convolve(exp_crec,impulso,mode='same')

#Impulso - Escalon
conv3= signal.convolve(impulso,escalon,mode='same')

#Escalon - Seno cardinal
conv4= signal.convolve(escalon,senc,mode='same')/sum(senc)

#Seno cardinal - Exponencial decreciente
conv5= signal.convolve(senc,exp_dec,mode='same')/sum(senc)

#Calculo Energias y Potencias 
#========================================================================

energiaconv1 = integrate.simps(abs(conv1)**2,t)
potenciaconv1 = (1/periodo)*energiaconv1

energiaconv2= integrate.simps(abs(conv2)**2,t)
potenciaconv2 = (1/periodo)*energiaconv2

energiaconv3 = integrate.simps(abs(conv3)**2,t)
potenciaconv3 = (1/periodo)*energiaconv3

energiaconv4 = integrate.simps(abs(conv4)**2,t)
potenciaconv4 = (1/periodo)*energiaconv4

energiaconv5 = integrate.simps(abs(conv5)**2,t)
potenciaconv5 = (1/periodo)*energiaconv5

#Graficos
#========================================================================
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv1)
ax.set_title('Exponencial decreciente - Exponencial creciente.')
ax.set_xlabel('Segundos')
ax.set_ylabel('Metros')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiaconv1*1000,2))+' [mJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(round(potenciaconv1*1000,2))+' [mW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv2)
ax.set_xlabel('Segundos')
ax.set_ylabel('Metros')
ax.set_title('Exponencial creciente - Impulso.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiaconv2*1000,2))+' [mJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(round(potenciaconv2*1000,2))+' [mW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv3)
ax.set_xlabel('Segundos')
ax.set_ylabel('Metros')
ax.set_title('Impulso - Escalon.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiaconv3*1000,2))+' [mJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(round(potenciaconv3*1000,2))+' [mW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv4)
ax.set_xlabel('Segundos')
ax.set_ylabel('Metros')
ax.set_title('Escalon - Seno cardinal.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiaconv4*1000,2))+' [mJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de la onda = '+str(round(potenciaconv4*1000,2))+' [mW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)

#========================================================================

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t,conv5)
ax.set_xlabel('Segundos')
ax.set_ylabel('Metros')
ax.set_title('Seno cardinal - Exponencial decreciente.')
ax.margins(0,0.1)
ax.text(0.02, 0.07, 'Energia de la onda = '+str(round(energiaconv5*1000,2))+' [mJ]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
ax.text(0.02, 0.01, 'Potencia de un periodo = '+str(round(potenciaconv5*1000,2))+' [mW]',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='black', fontsize=12)
        
plt.show()