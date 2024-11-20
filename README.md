Funciones de distribucion
Las funciones de distribución, tanto continuas como discretas, permiten modelar el comportamiento de variables aleatorias y analizar sus propiedades. Aquí te detallo las funciones de distribución más comunes en ambas categorías y los parámetros clave asociados para el cálculo de sus datos estadísticos.

---

### Distribuciones Discretas

1. **Distribución Binomial**
   - **Descripción**: Modela el número de éxitos en una serie de experimentos independientes con dos posibles resultados (éxito o fracaso).
   - **Parámetros**:
     - \( n \): Número de experimentos.
     - \( p \): Probabilidad de éxito en cada experimento.
   - **Estadísticos**:
     - Media: \( \mu = np \)
     - Varianza: \( \sigma^2 = np(1 - p) \)

2. **Distribución de Poisson**
   - **Descripción**: Modela el número de eventos que ocurren en un intervalo de tiempo o espacio dado, donde los eventos son independientes y ocurren a una tasa constante.
   - **Parámetro**:
     - \( \lambda \): Tasa media de ocurrencia de eventos por intervalo.
   - **Estadísticos**:
     - Media: \( \mu = \lambda \)
     - Varianza: \( \sigma^2 = \lambda \)

3. **Distribución Geométrica**
   - **Descripción**: Modela el número de ensayos necesarios para obtener el primer éxito en una serie de ensayos independientes con probabilidad fija de éxito.
   - **Parámetro**:
     - \( p \): Probabilidad de éxito en cada ensayo.
   - **Estadísticos**:
     - Media: \( \mu = \frac{1}{p} \)
     - Varianza: \( \sigma^2 = \frac{1 - p}{p^2} \)

4. **Distribución Hipergeométrica**
   - **Descripción**: Modela el número de éxitos en una muestra de tamaño fijo sin reemplazo de una población finita que contiene un número específico de éxitos.
   - **Parámetros**:
     - \( N \): Tamaño de la población.
     - \( K \): Número total de éxitos en la población.
     - \( n \): Tamaño de la muestra.
   - **Estadísticos**:
     - Media: \( \mu = \frac{nK}{N} \)
     - Varianza: \( \sigma^2 = \frac{nK(N - K)(N - n)}{N^2(N - 1)} \)

---

### Distribuciones Continuas

1. **Distribución Normal (o Gaussiana)**
   - **Descripción**: Modela variables aleatorias continuas que tienden a acumularse alrededor de una media, formando una campana simétrica.
   - **Parámetros**:
     - \( \mu \): Media de la distribución.
     - \( \sigma \): Desviación estándar de la distribución.
   - **Estadísticos**:
     - Media: \( \mu \)
     - Varianza: \( \sigma^2 \)

2. **Distribución Exponencial**
   - **Descripción**: Modela el tiempo entre eventos en un proceso de Poisson donde los eventos ocurren a una tasa constante.
   - **Parámetro**:
     - \( \lambda \): Tasa de ocurrencia de eventos (inverso del tiempo medio entre eventos).
   - **Estadísticos**:
     - Media: \( \mu = \frac{1}{\lambda} \)
     - Varianza: \( \sigma^2 = \frac{1}{\lambda^2} \)

3. **Distribución Uniforme Continua**
   - **Descripción**: Asigna probabilidades iguales a todos los valores dentro de un rango definido.
   - **Parámetros**:
     - \( a \): Límite inferior del rango.
     - \( b \): Límite superior del rango.
   - **Estadísticos**:
     - Media: \( \mu = \frac{a + b}{2} \)
     - Varianza: \( \sigma^2 = \frac{(b - a)^2}{12} \)

4. **Distribución Gamma**
   - **Descripción**: Modela la suma de tiempos de espera en procesos de Poisson, generalizando la distribución exponencial.
   - **Parámetros**:
     - \( \alpha \): Parámetro de forma.
     - \( \beta \): Parámetro de escala (inverso de la tasa).
   - **Estadísticos**:
     - Media: \( \mu = \alpha \beta \)
     - Varianza: \( \sigma^2 = \alpha \beta^2 \)

5. **Distribución Beta**
   - **Descripción**: Modela proporciones o probabilidades en un intervalo limitado entre 0 y 1.
   - **Parámetros**:
     - \( \alpha \): Parámetro de forma 1.
     - \( \beta \): Parámetro de forma 2.
   - **Estadísticos**:
     - Media: \( \mu = \frac{\alpha}{\alpha + \beta} \)
     - Varianza: \( \sigma^2 = \frac{\alpha \beta}{(\alpha + \beta)^2(\alpha + \beta + 1)} \)

6. **Distribución Chi-Cuadrado**
   - **Descripción**: Modela la suma de los cuadrados de variables normales independientes, comúnmente utilizada en pruebas de hipótesis.
   - **Parámetro**:
     - \( k \): Grados de libertad.
   - **Estadísticos**:
     - Media: \( \mu = k \)
     - Varianza: \( \sigma^2 = 2k \)

---

### Resumen de Estadísticos

Los datos estadísticos que comúnmente se calculan en estas distribuciones son:

Función de Distribución Acumulada (FDA): Proporciona la probabilidad acumulada de que la variable aleatoria tome un valor menor o igual a un valor específico. Es una función que crece de 0 a 1.

Función de Densidad de Probabilidad (FDP): Describe la probabilidad de que una variable aleatoria continua esté en un rango específico de valores. En distribuciones continuas, la FDP representa la forma de la distribución de probabilidad.

Media o Esperanza Matemática (E[X]): Es el valor promedio esperado de la variable aleatoria y proporciona una medida de tendencia central.

Mediana: Es el valor que divide la distribución en dos partes iguales, donde el 50% de los valores están por debajo y el otro 50% por encima.

Moda: Es el valor de la variable aleatoria que tiene la mayor probabilidad de ocurrencia en una distribución. Una distribución puede tener una o varias modas.

Varianza (Var[X]): Mide la dispersión de la variable respecto a la media. Una varianza alta indica que los valores están más dispersos.

Desviación Estándar (σ): Es la raíz cuadrada de la varianza, y proporciona una medida de dispersión en las mismas unidades que la variable aleatoria.

Cuantiles o Percentiles: Son valores de la variable aleatoria que dividen la distribución en segmentos de probabilidad iguales. Por ejemplo, el percentil 25 indica que el 25% de los valores están por debajo de este valor.

Curtosis: Mide el grado de concentración de los datos en torno a la media. Ayuda a determinar si la distribución tiene colas más gruesas o delgadas en comparación con una distribución normal.

Asimetría: Mide la falta de simetría de la distribución. Una distribución puede ser simétrica, sesgada a la derecha (positiva) o a la izquierda (negativa).
