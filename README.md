1. **La paradoja de los puntos**: Los métodos de Trapecio y Simpson utilizaron 13 evaluaciones de la función. Gauss-Legendre solo evaluó la función 5 veces en total.
2. **Análisis del error**: A pesar de usar menos de la mitad de los puntos, Gauss-Legendre obtuvo un error de $1.37\times 10^{-7}$. Esto es casi 4000 veces más preciso que Simpson y 100000 veces más preciso que el Trapecio.

**Análisis**: Los incisos de arriba suceden porque, mientras que los métodos de Trapecio y Simpson utilizaron n=13 puntos equiespaciados, Gauss-Legendre utilizó n=5 puntos elegidos y distribuidos cuidadosamente para maximizar la precisión de la aproximación.

**Pregunta 1: Eficiencia computacional.** Tomando en cuenta los resultados de la terminal, explique la relación entre el número de evaluaciones de la función $f(x)$ y el error absoluto obtenido por Gauss-Legendre frente a los métodos de Newton-Cotes. ¿Por qué se dice que Gauss optimiza el costo computacional?

**Respuesta**. El costo computacional depende del número de iteraciones necesarias para obtener la aproximación deseada. En este contexto, Gauss-Legendre hizo con 5 evaluaciones una aproximación con un error mucho menor que Newton-Cotes, con 13 evaluaciones asignadas. 

**Pregunta 2: El efecto de la oscilación.** Observe el comportamiento de la función en el intervalo dado. ¿Qué ocurre con la pendiente y la oscilación en las zonas de mayor curvatura? Explique matemáticamente por qué los métodos compuestos tradicionales fallan más en esa zona que la cuadratura de Gauss-Legendre.

**Respuesta**. En funciones como $f(x)=cos(x^2)$ la frecuencia de oscilación crece conforme aumenta $x$.
Derivando: $$f'(x)=-2x\sin(x^2)$$
$$f''(x)=-2\sin(x^2)-4x^2\cos(x^2)$$.
Se observa que la curvatura aumenta significativamente para valores grandes de $x$.
Cuando la función oscila rápidamente, las aproximaciones locales de Trapecio y Simpson dejan de seguir la forma real de la curva porque utilizan subintervalos equiespaciados. Como Gauss-Legendre evita utilizar puntos uniformes sino puntos estratégicos derivados a partir del polinomio de Legendre, capturan mejor la variación incluso en los extremos más oscilantes de la curva, utilizando menos puntos.

**Pregunta 3: Límites del Método**. Si cambiáramos la función por el polinomio exacto $P(x)=x^7-3x^4+2x$, ¿cuántos nodos $n$ requeriría Gauss-Legendre para obtener un error absoluto de exactamente cero?

**Respuesta**. Dado que el polinomio es de grado 7, se requiere el menor $n$ tal que $2n-1 \geq 7 \rightarrow n=4$ es el número mínimo de nodos necesarios para obtener error absoluto exactamente igual a cero. Se evidencia que con una cantidad considerablemente baja de nodos se puede llegar a una aproximación con error igual a 0, superando con creces al método de Trapecio y de Simpson.
