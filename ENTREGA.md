# Entrega individual — Parte práctica

- Nombre y código:86289 Marcos Dominguez
- URL del repositorio privado:
- Rama entregada:
- Commit final: se presenta en el formulario/mensaje de entrega después del último commit.

## Resultado inicial

- Comando ejecutado:
- Resumen real de pytest antes de cambiar el código:

## Cambios y requisitos

En dos o tres frases, explique qué cambió en modificar_reserva y por qué.

el requerimiento 04 pedia devolver CONFLICTO si en una modificacion los horarios nuevos chocan con otros de la misma sala
asi que agregue el if que entra en esa condicion

## Trazabilidad de sus pruebas

| Nombre de la prueba | Requisito | Resultado esperado |
|---|---|---|
| test_confirmar_no_existe| 01|NO_EXISTE |
| test_confirmar_cancelada| 02|CANCELADA |
| test_confirmar_cambio_de_horario_invalido|03|CONFLICTO|
|test_confirmar_modificacion_valida |05 |OK |
|test_conflicto_de_horario|04|CONFLICTO|

## Resultado final y límites

- Comando ejecutado:.\.venv\Scripts\python.exe -m pytest -v
- Resumen real de pytest (passed/failed y otros resultados si aparecen):todo pasa 
- ¿Qué comportamiento sigue sin comprobar? Escriba una limitación concreta:

No presente una prueba fallida como aprobada. Conserve y explique cualquier pendiente.
