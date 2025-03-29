@echo off
title Server App For Windows
:: Habilita delayed expansion
setlocal enabledelayedexpansion

:: Establece dir
cd dist

:: Busca parametros
set Par=%1

:: Verifica si Hay Parametros
if "!Par!"=="" (
    echo [31mIntroduzca un parametro.[0m
    echo.
    echo [32mParametros admitidos:[0m
    echo.
    echo -App = Inicia la App con normalidad.
    echo -AppRes = Restablece la app a estado de fabrica.
) else (
    :: Ejecuta Uno de estos parametros
    if /i "!Par!"=="-App" (
        echo [32mIniciando App
        NodeApp.exe
    )
    if /i "!Par!"=="-AppRes" (
        echo [32mIniciando Reset de App
        AppReset.exe
    )
)
:: Vuelve al directorio anterior
cd ..