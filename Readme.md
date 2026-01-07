# Tarea Dev Junior - Ruuf Solar

## Descripción

Esta solución resuelve el problema de calcular la **máxima cantidad de paneles solares** que caben en un techo rectangular.

El código está implementado en **Python**.

---

## Algoritmo y lógica

1. Se reciben como entrada:
   - `ancho_panel` y `alto_panel`
   - `ancho_techo` y `alto_techo`

2. Se prueban las **dos orientaciones posibles** de cada panel:
   - Panel horizontal (`ancho x alto`)
   - Panel vertical (`alto x ancho`)

3. Para cada orientación:
   - Se iteran todas las posibles cantidades de filas que caben en el techo.
   - Para cada cantidad de filas:
     - Se calcula cuántos paneles caben en esas filas.
     - Se calcula cuántos paneles adicionales pueden colocarse en el **espacio sobrante** usando la orientación rotada.

4. Se selecciona el **máximo número total de paneles** entre todas las combinaciones posibles.

   - Se retorna el valor obtenido
