
Feature: Pagina de registro


  @issue=TEST-1
  Scenario: Happy Path
    Given Abro el portal de Montepio
    Then Cierro el modal informativo
    Then Hago click en el boton "Registro"
    Then Espero 8 segundos
    Then Selecciono masculino como mi genero
    Then Ingreso mi nombre
    Then Ingreso mi segundo nombre
    Then Ingreso mi apellido paterno
    Then Ingreso mi apellido materno
    Then Ingreso mi RFC
    Then Ingreso mi correo electronico
    Then Confirmo mi correo electronico
    Then Ingreso mi celular
    Then Ingreso mi contrasena
    Then Confirmo mi contrasena
    Then Ingreso mi ano de nacimiento
    Then Ingreso mi mes de nacimiento
    Then Ingreso mi dia de nacimiento
    Then Acepto los terminos y condiciones
    Then Hago click en el boton "siguiente"
    Then Espero 8 segundos
    Then Selecciono mi pais de nacimiento
    Then Selecciono mi nacionalidad
    Then Ingreso mi codigo postal
    Then Selecciono un pais
    Then Espero 8 segundos
    Then Selecciono un estado
    Then Espero 8 segundos
    Then Selecciono una delegacion
    Then Espero 8 segundos
    Then Selecciono una colonia
    Then Ingreso mi calle
    Then Ingreso mi numero exterior
