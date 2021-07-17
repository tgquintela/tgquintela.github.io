---
title: '¿Para qué sirven los modelos?'
subtitle: 'La utilidad de tener modelos para mejorar gestiones y la toma de decisiones'
excerpt: 'Se han hablado mucho de los modelos matemáticos, pero poco se ha dicho de ellos. ¿Para qué sirven? ¿Cuáles son sus limitaciones? Son algunas de las preguntas que nos hacemos en este post.'
date: 2020-06-10
permalink: /blog/2020/06/para-que-sirven-los-modelos/

header:
  overlay_image: https://www.sciencemag.org/sites/default/files/styles/article_main_image_-_1280w__no_aspect_/public/ma_0817_Sato_main_15245D6373E_6770702%3B5.jpg
  overlay_filter: 0.4

tags:
  - data
  - epidemiologia
  - management
  - policies
categories:
  - data
  - policies
  - statistics
  - philosophy
---

Y llegó la crisis, y todos fuimos tragados por la curva exponencial... de modelos. Cualquiera que tuviera una mínima idea de conceptos básicos de matématica (ya ni siquiera programación), se lanzaron a hacer modelos para el coronavirus. Por un momento parecía que la única respuesta a la pregunta "¿Para qué sirven los modelos?" solo podía ser, para entretener a los que los desarrollan.

![Ola de artículos científicos](https://www.sciencemag.org/sites/default/files/styles/article_main_image_-_1280w__no_aspect_/public/ma_0817_Sato_main_15245D6373E_6770702%3B5.jpg?itok=2TKO4g1i)
**Imagen 1**: <span style="color:#808080">SARA GIRONI CARNEVALE</span>

<br />

Surgieron todo tipo de modelos. Algunos desarrollados en simple excel siguiendo principios simples, mientras que otros complejos, desarrollados e implementados en miles de lineas de código y que requieren horas de computación.
Lo cierto es que lo único que se consiguió es **generar confusión colectiva**.
La gente no estaba preparada para valorar qué modelo es bueno y cuales no lo son. O para qué casos son buenos unos y para qué pueden ser utilizados otros.
Unos decían una cosa, otros decían otras y sin herramientas para poder diferenciar de cual fiarse, mucha gente optó simplemente por descalificar a todos ellos. No fiarse de ninguno.

De este enredo no se puede culpar a los *investigadores* (muchos han protestado contra esa ciencia a contrarreloj [[1](https://twitter.com/soragnilab/status/1247576236563369985)][[2](https://www.wired.com/story/the-science-of-this-pandemic-is-moving-at-dangerous-speeds/)] que se salta sus proprios procesos y reglas solo para acelerar los tiempos, y que dejan más claro y visible que nunca su falta de infalibilidad [[3](https://www.agenciasinc.es/Reportajes/El-coronavirus-baja-a-la-ciencia-de-su-pedestal-habra-una-crisis-de-confianza)]), ni a la buena voluntad de los que han querido acercarse a la ciencia y entienden su importancia. Pero tampoco a aquellos que sin tener una preparación y conocimiento científico se ve sobrecargados y deciden desconfiar o directamente renegar de la ciencia. *El problema ha sido colectivo*. No tenemos estructuras preparadas para afrontar estos nuevos desafíos. No hay un gran red de periodistas especializados que conocen como funciona la ciencia y una red de divulgadores científicos con una visibilidad importante en la sociedad. Sobre temas científicos todavía sigue valiendo más la opinión de un político que la de un científico.

Desde la más humilde intención y para intentar contribuir en **desenredar** este enredo escribo esta entrada del blog. En ella intentaremos entender que tipos de modelos hay y para que se pueden utilizar. Pero también entender cuales son sus **límites**.


## ¿Qué son los modelos?
Los modelos son **simplificaciones** de como funciona el mundo (o aquello que se pretende modelar), pero que se comporta como se comporta la realidad. Un modelo pretende siempre limpiar el polvo, quitar las cosas de encima de la mesa y observarla desnuda. Mostrando transparente toda su esencia, para poderla entender mejor.

El sistema que se quiere estudiar queda reducido a pequeños componentes modulares que interaccionan entre ellos de una forma determinada.

Un modelo **se alimenta de datos** (medidas sobre el sistema antes del evento/s que queremos modelar) y **su resultado son datos** (medidas sobre el sistema después del evento/s que queremos modelar).

Idealmente si dichas medidas sobre el sistema modelado antes y después del periodo que queremos modelar se acercan en todas las circunstancias a las que produce el modelo podemos decir que el modelo es un buen modelo.


## Tipos de modelos
Durante estos últimos meses hemos visto diferentes tipos de modelos, que podemos catalogar utilizando diferentes parámetros que los describen, según cuales sean las respuestas a las siguientes preguntas:

### ¿Qué información utiliza el modelo?
En esta crisis sanitaria hemos visto especialmente modelos de dos tipos:
* Información sobre los contagios detectados (información solo referente a lo que queremos predecir)
* Información relacionada con la dinámica de los contagios (datos de movilidad y de espacios compartidos entre personas).

La gran mayoría de los modelos *amateur* que fueron apareciendo solo consideraban el primer tipo de información. Los más elaborados empezaron incluyendo además información de movilidad e información adicional que pudiera ser relevante para predecir la viralidad del virus.

### ¿Qué lógica matemática utiliza el modelo?
Los modelos matemáticos utilizados seguian logicas muy distintas entre ellos. A *grosso modo* podemos ver dos muy diferentes:
* *Modelos regresivos*: cogiendo los datos de las curvas intentaban ajustar lineas y esperar que sean estrapolables a las regiones de las cuales todavía no tenemos datos.
Estos son modelos muy limitados y que no ayudan a entender las causas. Pueden ser útiles en fenomenos que generan patrones muy claros de estacionalidad o de un comportamiento muy característico, ya que en esos casos es facil de extrapolar en el futuro e intentar predecir con ellos.
![Regresión]({{ base_path }}/files/modelos_introduccion/regression_example.png)
**Figura 1**: Ejemplo de una regresión.

<br />
* *Modelos de simulación*: que se basan en definir una dinámica de cómo funciona de base el mecanismo que queremos modelar. En el caso de una epidemía, un ejemplo de este tipo de modelos es el **módelo SIR** que tanto se ha nombrado. Un modelo que trata de separar la población en 3 posibles estados (Susceptibles de ser infectados, Infectados y Recuperados). Las probabilidades de transicionar entre unos y otros es lo que debemos averiguar con los datos. Una vez tenemos dichas probablidades podemos hacer predicciones.
![Componentes del modelo](https://miro.medium.com/max/1400/1*TIZaRpt70TR1RFtf2dmlew.png)
![Datos resultados del modelo](https://miro.medium.com/max/1400/1*E6L3YUMAmyR4PX0s_HFFTw.png)
**Figura 2**: Modelo SEIRD [[4](https://towardsdatascience.com/infectious-disease-modelling-beyond-the-basic-sir-model-216369c584c4)]. La primera figura representa los componentes y la estructura del modelo. La segunda los datos que devuelve la simulación.


## ¿Para qué queremos los modelos?

Los modelos tienen como principales objectivos:
* **Entender** el sistema que queremos modelar. ¿Cómo funciona?¿Cuáles son sus dinámicas?
* Tener capacidad de **predecir** qué pasará. Toda predicción viene determinada de un contexto, unas *condiciones iniciales*. Dichas condiciones iniciales son datos a introducir al modelo para que éste nos de los datos de la predicción. En nuestro caso vendrían dadas por las propiedades características de este virus. Su capacidad de contagio, su periodo de incuvación, ...
* Alcanzar una capacidad de **controlar**, de tomar decisiones. Ser capaz de modelar no solo el comportamiendo del sistema que queremos **entender** y **predicir**, si no también la interacción de dicho sistema con las herramientas de control que tenemos y que pueden interactuar con tal sistema. En el caso de la pandemia debemos analizar la capacidad de hacer tests, capacidad de hospitales y camas de UCIs.

Este último tipo de modelos es especialmente interesante para la toma de decisiones. Poder predecir que resultados pueden tener cada una de nuestras acciones (siempre con una cierta incerteza, recordemos que esto es ciencia), nos da el poder de decidir haciendo un balance de costes y beneficios.

Para la demostración de este fenomeno podemos utilizar una herramienta creada para entender la Covid-19 y como restringir su contagio.

[![Regresión]({{ base_path }}/files/modelos_introduccion/que_pasara_ahora.png)](https://vrruiz.github.io/covid-19/)
**Figura 3**: Esta pagina [[5](https://vrruiz.github.io/covid-19/)] inicialmente creado para la explicación más didactica sobre la covid-19, nos vale de ejemplo simple de simulaciones para el control y la toma de decisiones.


<br />

En nuestro imaginario, la persona responsable de la toma de sus posibles decisiones tendría la opciones de insertar sus decisiones y ver el resultado esperado de las mismas.


## Los modelos necesitan datos
Antes hemos dicho que un modelo se alimenta de datos. Sin datos, podemos tener el mejor modelo del mundo pero no dará las predicciones correctas. Generar mediciones es el primer y más significante paso para generar modelos buenos y útiles.

Una de las grandes críticas y aplausos que le podemos hacer a las entidades públicas españolas es la gestión de las medidas en esta crisis. Críticas debido al caos inicial de los tests y la lejanía de los casos detectados respecto a los reales. Sin esos datos, **cualquiera de las decisiones que se puedan tomar son inconscientes**. Y las intenciones de dichas decisiones se alejarán notablemente del resultado final de la decisión tomada.
Pero también tenemos el buen ejemplo del estudio serológico realizado más grande de Europa [[6](https://www.mscbs.gob.es/gabinete/notasPrensa.do?id=4853)][[7](https://www.mscbs.gob.es/ciudadanos/enfLesiones/enfTransmisibles/sida/EPICOS/RESUMEN.pdf)][[8](https://www.huffingtonpost.es/entry/los-resultados-del-estudio-serologico-muestran_es_5ebc18f2c5b6270384a999e7)][[9](https://www.the-scientist.com/news-opinion/researchers-applaud-spanish-covid-19-serological-survey-67590)].
Obteniendo los datos y dandolos a los investigadores, se puede llenar de luz a las siguientes deciones que se deban tomar. Sin saber que sólo en 5% de los españoles habían sido expuesto al SARS-COV-2 dificilmente se podrían tomar las mejores decisiones.
Sin conocer datos sobre la mobilidad como grupos de investigación han utilizado 

Si queremos tomar las decisiones correctas debemos luchar por tener **mejores datos** y que puedan estar bajo el **escrutinio público** para asegurar su calidad. Varias iniciativas han surgido durante esta pandemia para acercar la ciencia y sus resultados a la población, como las iniciativas de medida de la movilidad [[10](https://www.covid-19-mobility.org/mobility-monitor/)][[11](https://analytics.ifisc.uib-csic.es/en/covid-19-response/)][[12](https://www.google.com/covid19/mobility/)].


## Modelos en la gestión pública

Poco a poco vemos que comienzan a surgir opiniones de expertos clamando por más ciencia y espíritu científico en la gestión pública [[13](https://thehill.com/opinion/healthcare/497533-let-science-lead-we-need-more-leaders-with-science-backgrounds)]. No porque vayan a saber resolver y responder todas las preguntas y tomar las mejores decisiones. No! Sino precisamente porque saben que hay cosas que no se pueden saber. Porque saben lo que significa la incertidumbre. Porque saben que la ciencia es estudiar cada día y aprender cosas nuevas. Y porque saben que la ciencia no te da la potestad de tomar las decisiones correctas si no de minimizar los riesgos de equivocarse.

Esto es válido más allá de la gestión de la pandemia. Cada medida social y económica debería tener una simulación asociada.
Ya hay casos en España que van en esa dirección [[14](https://www.niusdiario.es/economia/datos-renta-minima-big-data-revolucion-politicas-publicas-ingreso-minimo-vital-donde-pedirlo-papeles-necesarios-cuando-cobra_18_2954445304.html)] pero deberían extenderse en la medida de lo posible.


## El peligro de la política contra la ciencia

Pero al mismo tiempo hemos visto como por parte de ciertos grupos se ataca con especial fiereza a científicos que han tenido que asesorar a sus gobiernos sobre esta crisis. Bien conocidos son los casos de **Christian Drosten** [[12](https://www.dw.com/es/diario-alem%C3%A1n-bild-arremete-contra-el-vir%C3%B3logo-m%C3%A1s-popular-de-alemania/a-53623311)][[16](https://www.lavanguardia.com/vida/20200530/481471811782/la-covid-situa-a-los-virologos-alemanes-en-la-linea-del-amor-odio-mediatico.html)], el virólogo alemán asesor del gobierno de Merkel, o **Anthony Fauci** [[17](https://cnnespanol.cnn.com/video/anthony-fauci-amenzas-muerto-coronavirus-eeuu-alejandra-oraa-cafe-cnnee/)], asesor científico del gobierno de Estados Unidos. Ambos, como muestran en los artículos, han sido amenazados de muerte por gente que devalúa la ciencia nada más que otra opinión. Grandes medios de comunicación, como "Bild" (el periódico más leído de Europa), o "Fox News" se han visto envueltos en esos ataques feroces y despiadados contra éstos científicos. En España tampoco se han escapado de este tipo de circunstancias. Como bien dijo un científico: *"Los científicos somos el blanco de quienes buscan culpables en lugar de soluciones a la COVID-19"* [[18](https://www.agenciasinc.es/Entrevistas/Los-cientificos-somos-el-blanco-de-quienes-buscan-culpables-en-lugar-de-soluciones-a-la-COVID-19)].

Los patrones de dichos ataques siguen los patrones habituales:
* O **explotan la ignorancia de la sociedad sobe qué es la ciencia** o cómo funciona el sistema científico. Pensando qué la ciencia es la verdad absoluta, y si éstos expertos fallan en momentos puntuales, o cambian de opinión antes nuevas evidencias, es simplemente que no son científicos. Esta circunstancia es la más facil de resolver. Necesitamos una red de divulgadores científicos con visibilidad notable. Ya no solo en los medios públicos, o en el *mainstream* (grandes medios), si no en podcasts, blogs y redes sociales. Explicando que la ciencia es ciencia, no es magia. Qué nos podemos esperar de ella y qué no.
* O simplemente **niegan la ciencia** o todo lo que se parezca. Rebajan la ciencia a una mera opinión más. Abrazan teorías de la conspiración de lo más exóticas. Todo es válido. La verdad y la mentira se diluyen sin ninguna prueba. Todo lo que vale es la fuerza del creer. Y si tú crees en algo, quién es la ciencia pra negartelo. Éstos son los más peligrosos para la sociedad, en parte porque pese a cualquier evidencia que surja, nunca cambiarán de opinión y en parte porque pueden mover a otros a creer ciegamente en proposiciones científicas aceptadas en dicho momento pero que pueden no ser verdad. 

Para aplicar la ciencia en métodos de gestión pública debemos ser consciente de estas amenazas. La primera debe ser solucionable con divulgación y un sistema de educación de calidad. La segunda debe simplemente ser tolerada como algo que existe en la sociedad y con lo cual debemos convivir. Pero nunca debemos tratar la ciencia como una herramienta infalible ni como un credo que debemos simplemente creer.

Conocer a que nos enfrentamos no queda fuera del alcance de la misma ciencia y ya existen iniciativas que intentan conocer y entender las dinámicas de desinformación y infodemia [[19](https://www.nature.com/articles/d41586-020-01452-z)][[20](https://covid19obs.fbk.eu)].


## En resumen,
Cuando se toman decisiones sería deseable siempre conocer el alcance de las consecuencias de dichas decisiones. Conocer como van a afectar cada una de las decisiones que tomamos por adelantado es la función de los modelos matemáticos.
Tener a disposición la información de impacto de cada decisión ayuda a tomar decisiones mejor informadas y balancear mejor los costes y beneficios.
Todo ello no evita que los modelos tengan una incerteza innata, y con ella debemos vivir.


## Referencias
* [1] [Twit de @soragnilab sobre la masiva creación de nuevos modelos](https://twitter.com/soragnilab/status/1247576236563369985)
* [2] [La ciencia de la pandemia se está moviendo a una velocidad peligrosa](https://www.wired.com/story/the-science-of-this-pandemic-is-moving-at-dangerous-speeds/)
* [3] [El coronavirus baja a la ciencia de su pedestal, ¿habrá una crisis de confianza?](https://www.agenciasinc.es/Reportajes/El-coronavirus-baja-a-la-ciencia-de-su-pedestal-habra-una-crisis-de-confianza)
* [4] [Infectious Disease Modelling: Beyond the Basic SIR Model](https://towardsdatascience.com/infectious-disease-modelling-beyond-the-basic-sir-model-216369c584c4)
* [5] [¿Qué pasará ahora?](https://vrruiz.github.io/covid-19/)
* [6] [El Ministerio de Sanidad promueve el primer ensayo clínico para prevenir la enfermedad por coronavirus en profesionales sanitarios](https://www.mscbs.gob.es/gabinete/notasPrensa.do?id=4853)
* [7] [EPICOS: ficha técnica](https://www.mscbs.gob.es/ciudadanos/enfLesiones/enfTransmisibles/sida/EPICOS/RESUMEN.pdf)
* [8] [Sólo el 5% de la población ha tenido el coronavirus en España](https://www.huffingtonpost.es/entry/los-resultados-del-estudio-serologico-muestran_es_5ebc18f2c5b6270384a999e7)
* [9] [Científicos aplauden el estudio serológico español sobre la COVID-19](https://www.the-scientist.com/news-opinion/researchers-applaud-spanish-covid-19-serological-survey-67590)
* [10] [Monitor de movilidad](https://www.covid-19-mobility.org/mobility-monitor/)
* [11] [IFISC/CSIC - respuesta al COVID-19](https://analytics.ifisc.uib-csic.es/en/covid-19-response/)
* [12] [Mira como tu comunidad se desplaza diferente debido al COVID-19](https://www.google.com/covid19/mobility/)
* [13] [Necesitamos más líderes con formación científica](https://thehill.com/opinion/healthcare/497533-let-science-lead-we-need-more-leaders-with-science-backgrounds)
* [14] [Big data niusdiario IMV Ingreso mínimo](https://www.niusdiario.es/economia/datos-renta-minima-big-data-revolucion-politicas-publicas-ingreso-minimo-vital-donde-pedirlo-papeles-necesarios-cuando-cobra_18_2954445304.html)
* [12] [Diario alemán "Bild" arremete contra el virólogo más popular de Alemania](https://www.dw.com/es/diario-alem%C3%A1n-bild-arremete-contra-el-vir%C3%B3logo-m%C3%A1s-popular-de-alemania/a-53623311)
* [16] [La COVID sitúa a los virólogos alemanes en la línea del amor-odio mediático](https://www.lavanguardia.com/vida/20200530/481471811782/la-covid-situa-a-los-virologos-alemanes-en-la-linea-del-amor-odio-mediatico.html)
* [17] [Aumentan las amenazas de muerte contra Anthony Fauci](https://cnnespanol.cnn.com/video/anthony-fauci-amenzas-muerto-coronavirus-eeuu-alejandra-oraa-cafe-cnnee/)
* [18] [*"Los científicos somos el blanco de quienes buscan culpables en lugar de soluciones a la COVID-19"*](https://www.agenciasinc.es/Entrevistas/Los-cientificos-somos-el-blanco-de-quienes-buscan-culpables-en-lugar-de-soluciones-a-la-COVID-19)
* [19] [La batalla épica contra la desinformación y las teorias de conspiración](https://www.nature.com/articles/d41586-020-01452-z)
* [20] [Covid19 Infodemics Observatory](https://covid19obs.fbk.eu)
