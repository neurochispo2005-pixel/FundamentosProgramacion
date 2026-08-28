{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b1f0203a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nombre: Aldo\n",
      "Tiempo total: 10.0 horas\n",
      "Porcentaje del día: 41.66666666666667 %\n"
     ]
    }
   ],
   "source": [
    "nombre = input(\"Escribe tu nombre: \")\n",
    "\n",
    "redes = float(input(\"Horas en redes sociales: \"))\n",
    "msj = float(input(\"Horas en mensajes: \"))\n",
    "series = float(input(\"Horas viendo series: \"))\n",
    "videos = float(input(\"Horas viendo videos: \"))\n",
    "gaming = float(input(\"Horas jugando videojuegos: \"))\n",
    "\n",
    "total = redes + msj + series + videos + gaming\n",
    "\n",
    "porcentaje = total / 24 * 100\n",
    "\n",
    "print(\"Nombre:\", nombre)\n",
    "print(\"Tiempo total:\", total, \"horas\")\n",
    "print(\"Porcentaje del día:\", porcentaje, \"%\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
[Actividad 1 progra.ipynb](https://github.com/user-attachments/files/31563396/Actividad.1.progra.ipynb)

