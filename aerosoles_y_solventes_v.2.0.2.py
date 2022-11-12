import os
import csv
import pandas as pd
import datetime
import os
import time
import sys

import keyboard
keyboard.press('f11')

#FUNCIONES DE RETORNO
def go_back():
    os.system('cls')
    menu_principal(main_menu)
def go_back1():
    os.system('cls')
    materia_prima()
def go_back2():
    os.system('cls')
    inv_consum()

#FUNCIONES DE FÓRMULAS-PRODUCCIÓN
def p_m4814():
    print()
    print()
    formula = 'M4814ES'
    cp = int(input('\t \t ¿Cuántas cajas de M4814 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_eb1():
    print()
    print()
    formula = 'EB1ES'
    cp = int(input('\t \t ¿Cuántas cajas de EB1 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_btc6():
    print()
    print()
    formula = 'BTC6ES'
    cp = int(input('\t \t ¿Cuántas cajas de BTC6 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_m2308():
    print()
    print()
    formula = 'M2308ES'
    cp = int(input('\t \t ¿Cuántas cajas de M2308 se produjeron?:   '))
    bp = cp * 24
    inventarios_q_c(formula, usr_name, cp, bp)
def p_m914():
    print()
    print()
    formula = 'M914ES'
    cp = int(input('\t \t ¿Cuántas cajas de M914 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_l112():
    print()
    print()
    formula = 'L112ES'
    cp = int(input('\t \t ¿Cuántas cajas de L112 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_nm6():
    print()
    print()
    formula = 'NM6ES'
    cp = int(input('\t \t ¿Cuántas cajas de NM6 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_l616():
    print()
    print()
    formula = 'L616ES'
    cp = int(input('\t \t ¿Cuántas cajas de L616 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_l711():
    print()
    print()
    formula = 'L711ES'
    cp = int(input('\t \t ¿Cuántas cajas de L711 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_azmpc30():
    print()
    print()
    formula = 'AZMPC30'
    cp = int(input('\t \t ¿Cuántas cajas de AZMPC30 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_mpc30():
    print()
    print()
    formula = 'MPC30ES'
    cp = int(input('\t \t ¿Cuántas cajas de MPC30 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_btp6():
    print()
    print()
    formula = 'BTP6ES'
    cp = int(input('\t \t ¿Cuántas cajas de BTP6 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_m5612():
    print()
    print()
    formula = 'M5612ES'
    cp = int(input('\t \t ¿Cuántas cajas de M5612 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)
def p_l212():
    print()
    print()
    formula = 'L212ES'
    cp = int(input('\t \t ¿Cuántas cajas de L212 se produjeron?:   '))
    bp = cp * 12
    inventarios_q_c(formula, usr_name, cp, bp)

#FUNCIONES PARA CAJAS
def c_m4814():
    print()
    print()
    codigo = "ASC0002"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_eb1():
    print()
    print()
    codigo = "ASC0016"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_btc6():
    print()
    print()
    codigo = "ASC0011"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_m2308():
    print()
    print()
    codigo = "ASC0033"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_m914():
    print()
    print()
    codigo = "ASC0029"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_l112():
    print()
    print()
    codigo = "ASC0045"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_nm6():
    print()
    print()
    codigo = "ASC0043"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_l616():
    print()
    print()
    codigo = "ASC0023"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_l711():
    print()
    print()
    codigo = "ASC0026"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_azmpc30():
    print()
    print()
    codigo = "ASC0006"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_mpc30():
    print()
    print()
    codigo = "ASC0038"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_btp6():
    print()
    print()
    codigo = "ASC0014"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_m5612():
    print()
    print()
    codigo = "ASC0036"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_l212():
    print()
    print()
    codigo = "ASC0020"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def c_m2616():
    print()
    print()
    codigo = "ASC0051"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)

#FUNCIONES PARA BOTE
def b_m4814():
    print()
    print()
    codigo = "ASC0001"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_eb1():
    print()
    print()
    codigo = "ASC0017"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_m2308():
    print()
    print()
    codigo = "ASC0030"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_m914():
    print()
    print()
    codigo = "ASC0028"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_l112():
    print()
    print()
    codigo = "ASC0044"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_l616():
    print()
    print()
    codigo = "ASC0024"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_l711():
    print()
    print()
    codigo = "ASC0025"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_azmpc30():
    print()
    print()
    codigo = "ASC0007"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_m5612():
    print()
    print()
    codigo = "ASC0035"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_l212():
    print()
    print()
    codigo = "ASC0019"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_gen_chico():
    print()
    print()
    codigo = "ASC0012"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_gen_grande():
    print()
    print()
    codigo = "ASC0039"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_gen_chico_resina():
    print()
    print()
    codigo = "ASC0046"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_gen_grande_resina():
    print()
    print()
    codigo = "ASC0047"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def b_gen_plastico_sonata1Lt():
    print()
    print()
    codigo = "ASC0056"
    if x > 0:
        n = int(input("\t \t ¿Cuántos botes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos botes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)

#FUNCIONES PARA PRODUCTO_TERMINADO
def PT_m4814():
    print()
    print()
    codigo = "M4814ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de M4814ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de M4814ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_eb1():
    print()
    print()
    codigo = "EB1ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de EB1ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de EB1ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_btc6():
    print()
    print()
    codigo = "BTC6ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de BTC6ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de BTC6ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_m2308():
    print()
    print()
    codigo = "M2308ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de M2308ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de M2308ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_m914():
    print()
    print()
    codigo = "M914ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de M914ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de M914ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_l112():
    print()
    print()
    codigo = "L112ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de L112ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de L112ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_nm6():
    print()
    print()
    codigo = "NM6ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de NM6ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de NM6ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_l616():
    print()
    print()
    codigo = "L616ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de L616ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de L616ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_l711():
    print()
    print()
    codigo = "L711ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de L711ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de L711ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_azmpc30():
    print()
    print()
    codigo = "AZMPC30"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de AZMPC30 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de AZMPC30 Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_mpc30():
    print()
    print()
    codigo = "MPC30ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de MPC30ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de MPC30ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_btp6():
    print()
    print()
    codigo = "BTP6ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de BTP6ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de BTP6ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_m5612():
    print()
    print()
    codigo = "M5612ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de M5612ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de M5612ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)
def PT_l212():
    print()
    print()
    codigo = "L212ES"
    if x > 0:
        n = int(input("\t \t ¿Cuántas cajas de L212ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas cajas de L212ES Salieron?:   "))
    inventario_producto_terminado(n, codigo, usr_name)

#FUNCIONES PARA QUIMICOS
def propelente():
    print()
    print()
    codigo = "AS0001"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Propelente Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Propelente Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def varsol():
    print()
    print()
    codigo = "AS0002"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Varsol Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Varsol Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def v_176():
    print()
    print()
    codigo = "AS0003"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de V-176 Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de V-176 Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def cerflon():
    print()
    print()
    codigo = "AS0004"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Cerflon Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Cerflon Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def glicol_DB():
    print()
    print()
    codigo = "AS0005"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Glicol Eter DB Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Glicol Eter DB Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def molivan():
    input("Prueba otro químico")
def pai_ricn():
    print()
    print()
    codigo = "AS0007"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de PAI-RICN Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de PAI-RICN Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def sarsol():
    print()
    print()
    codigo = "AS0008"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Sarsol Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Sarsol Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def aceite_mineral():
    print()
    print()
    codigo = "AS0009"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Aceite Mineral Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Aceite Mineral Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def silicon_5000():
    print()
    print()
    codigo = "AS0010"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Silicon 5000 Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Silicon 5000 Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def grasa_litio():
    print()
    print()
    codigo = "AS0011"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Grasa de litio Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Grasa de litio Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def metanol():
    print()
    print()
    codigo = "AS0012"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Metanol Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Metanol Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def acetona():
    print()
    print()
    codigo = "AS0013"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Acetona Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Acetona Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def oxido_zinc():
    print()
    print()
    codigo = "AS0014"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Óxido de Zinc Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Óxido de Zinc Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def xilol():
    print()
    print()
    codigo = "AS0015"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Xilol Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Xilol Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def cloruro_metileno():
    print()
    print()
    codigo = "AS0016"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Cloruro de Metileno Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Cloruro de Metileno Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def heptano():
    print()
    print()
    codigo = "AS0017"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Heptano Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Heptano Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def cirrasol_g_1096():
    print()
    print()
    codigo = "AS0018"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Cirrasol G 1096 Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Cirrasol G 1096 Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def diesel():
    print()
    print()
    codigo = "AS0019"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Diesel Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Diesel Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def glicol_EB():
    print()
    print()
    codigo = "AS0020"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Glicol Eter EB Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Glicol Eter EB Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def aromina_150():
    print()
    print()
    codigo = "AS0021"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Aromina 150 Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Aromina 150 Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def glicol_tpm():
    print()
    print()
    codigo = "AS0022"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Glicol Eter TPM Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Glicol Eter TPM Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def novasolv():
    print()
    print()
    codigo = "AS0023"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Novasolv 110 Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Novasolv 110 Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def lubricit():
    print()
    print()
    codigo = "AS0024"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Lubricit TPM Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Lubricit TPM Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def agua_destilada():
    print()
    print()
    codigo = "AS0025"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Agua Destilada Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Agua Destilada Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def natrasense_ag810():
    print()
    print()
    codigo = "AS0026"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Natrasense AG810 Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Natrasense AG810 Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def cirrasol_expel():
    print()
    print()
    codigo = "AS0027"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Cirrasol Expel Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Cirrasol Expel Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def bicarbonato_sodio():
    print()
    print()
    codigo = "AS0028"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Bicarbonato de sodio Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Bicarbonato de sodio Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def rojo_metilo():
    print()
    print()
    codigo = "AS0029"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Rojo de Metilo Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Rojo de Metilo Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def solvent_red():
    print()
    print()
    codigo = "AS0030"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Solvent RED Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Solvent RED Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def tpc_1160():
    print()
    print()
    codigo = "AS0031"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de TPC 1160 Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de TPC 1160 Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def frag_brisa_m():
    print()
    print()
    codigo = "AS0032"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Fragancia Brisa Marina Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Fragancia Brisa Marina Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def frag_vainilla():
    print()
    print()
    codigo = "AS0033"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Fragancia Vainilla Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Fragancia Vainilla Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def frag_auto_n():
    print()
    print()
    codigo = "AS0034"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Fragancia Auto Nuevo Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Fragancia Auto Nuevo Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def crodazoline():
    print()
    print()
    codigo = "AS0035"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Crodazoline Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Crodazoline Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def glicerina():
    print()
    print()
    codigo = "AS0036"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Glicerina Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Glicerina Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def emulsion_silicon():
    print()
    print()
    codigo = "AS0037"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Emulsion de Silicón Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Emulsiçon de Silicón Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def hidantoina():
    print()
    print()
    codigo = "AS0038"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Hidantoina Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Hidantoina Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def less():
    print()
    print()
    codigo = "AS0039"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de LESS Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de LESS Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def rosa_brillante():
    print()
    print()
    codigo = "AS0040"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Rosa Brillante Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Rosa Brillante Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def percloroetileno():
    print()
    print()
    codigo = "AS0041"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Percloroetileno Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Percloroetileno Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def isopropanol():
    print()
    print()
    codigo = "AS0042"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Isopropanol Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Isopropanol Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def monoetileng():
    print()
    print()
    codigo = "AS0043"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Monoetilenglicol Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Monoetilenglicol Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def amarillo_brax():
    print()
    print()
    codigo = "AS0044"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Amarillo Braxime GDCX Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Amarillo Braxime GDCX Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def silicon_60k():
    print()
    print()
    codigo = "AS0045"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Silicón 60,000 cst Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Silicón 60,000 cst Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def hexyl_cell():
    print()
    print()
    codigo = "AS0046"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Hexyl Cellosolve Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Hexyl Cellosolve Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def ecosurf_eh3():
    print()
    print()
    codigo = "AS0047"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Ecosurf EH-3 Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Ecosurf EH-3 Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def inhibidor_corrosion_agua():
    print()
    print()
    codigo = "AS0050"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Inhibidor de corrosion Base Agua Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Inhibidor de corrosion Base Agua Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def rojo_brax():
    print()
    print()
    codigo = "AS0051"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Rojo Braxime RCHX Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Rojo Braxime RCHX Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def verde_esmer():
    print()
    print()
    codigo = "AS0052"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Verde Esmeralda 5 Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Verde Esmeralda 5 Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)
def diox_titanio():
    print()
    print()
    codigo = "AS0053"
    if x > 0:
        n = float(input("\t \t ¿Cuántos kilogramos de Dióxido de Titanio Entraron?:   "))
    else:
        n = float(input("\t \t ¿Cuántos kilogramos de Dióxido de Titanio Salieron?:   "))
    inventario_quimicos_(n, codigo, usr_name)

#FUNCIONES PARA TAPAS
def tapa_amarilla():
    print()
    print()
    codigo = "ASC0021"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Tapas amarillas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Tapas amarillas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def tapa_cepillo():
    print()
    print()
    codigo = "ASC0010"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Tapas con cepillo Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Tapas con cepillo Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def tapa_negraM2308():
    print()
    print()
    codigo = "ASC0031"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Tapas M2308ES Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Tapas M2308ES Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def tapa_chica_R():
    print()
    print()
    codigo = "ASC0022"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Tapas chicas rectas azules Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Tapas chicas rectas azules Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def tapa_grande_R():
    print()
    print()
    codigo = "ASC0005"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Tapas grandes rectas azules Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Tapas grandes rectas azules Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def tapa_chica_B():
    print()
    print()
    codigo = "ASC0053"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Tapas chicas c/borde azules Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Tapas chicas c/borde azules Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def tapa_grande_B():
    print()
    print()
    codigo = "ASC0052"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Tapas grandes c/borde azules Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Tapas grandes c/borde azules Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def tapa_rojaM5612():
    print()
    print()
    codigo = "ASC0037"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Tapas rojas M5612 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Tapas rojas M5612 Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def tapa_28_410_natural():
    print()
    print()
    codigo = "ASC0057"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Tapas 28/410 Natural Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Tapas 28/410 Natural Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)

#FUNCIONES PARA ETIQUETAS
def etq_btc6():
    print()
    print()
    codigo = "ASC0027"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Etiquetas BTC6 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Etiquetas BTC6 Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def etq_btp6():
    print()
    print()
    codigo = "ASC0015"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Etiquetas BTP6 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Etiquetas BTP6 Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def etq_nm6():
    print()
    print()
    codigo = "ASC0041"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Etiquetas NM6 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Etiquetas NM6 Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def etq_mpc30():
    print()
    print()
    codigo = "ASC0040"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Etiquetas MPC30 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Etiquetas MPC30 Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def etq_m2308():
    print()
    print()
    codigo = "ASC0034"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Etiquetas M2308 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Etiquetas M2308 Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def etq_M2616():
    print()
    print()
    codigo = "ASC0048"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Etiquetas M2616 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Etiquetas M2616 Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def etq_nm1():
    print()
    print()
    codigo = "ASC0049"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Etiquetas NM1 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Etiquetas NM1 Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def etq_m206ope():
    print()
    print()
    codigo = "ASC0050"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Etiquetas M206OPE Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Etiquetas M206OPE Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)

#FUNCIONES PARA valvulas
def v_ch():
    print()
    print()
    codigo = "ASC0042"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Válvulas chicas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Válvulas chicas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def v_gde():
    print()
    print()
    codigo = "ASC0018"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Válvulas grandes Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Válvulas grandes Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def v_med():
    print()
    print()
    codigo = "ASC0003"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Válvulas medianas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Válvulas medianas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def v_espuma():
    print()
    print()
    codigo = "ASC0008"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Válvulas de espuma Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Válvulas de espuma Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def act_espuma():
    print()
    print()
    codigo = "ASC0009"
    if x > 0:
        n = int(input("\t \t ¿Cuántos Activadores Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos Activadores Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def tubo_ext():
    print()
    print()
    codigo = "ASC0004"
    if x > 0:
        n = int(input("\t \t ¿Cuántos Tubos de extensión Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántos Tubos de extensión Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)

#FUNCIONES PARA OTROS
def liner_m2308():
    print()
    print()
    codigo = "ASC0032"
    if x > 0:
        n = int(input("\t \t ¿Cuántas Liners M2308 Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas Liners M2308 Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)
def canica():
    print()
    print()
    codigo = "ASC0013"
    if x > 0:
        n = int(input("\t \t ¿Cuántas canicas Entraron?:   "))
    else:
        n = int(input("\t \t ¿Cuántas canicas Salieron?:   "))
    inventario_consumibles_(n, codigo, usr_name)

#FUNCIONES PARA CALIDAD
def q_m4814():
    print()
    print()
    n = "N/A"
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "M4814"
    ir_dens(n, d, usr_name, sku)
def q_eb1():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "EB1"
    ir_dens(n, d, usr_name, sku)
def q_btc6():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "BTC6"
    ir_dens(n, d, usr_name, sku)
def q_m2308():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "M2308"
    ir_dens(n, d, usr_name, sku)
def q_m914():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "M914"
    ir_dens(n, d, usr_name, sku)
def q_l112():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "L112"
    ir_dens(n, d, usr_name, sku)
def q_nm6():
    print()
    print()
    print("\t \t \t NO APLICA")
    print()
    print()
    input("\t \t \t Presiona una tecla para continuar...")
def q_l616():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "L616"
    ir_dens(n, d, usr_name, sku)
def q_l711():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "L711"
    ir_dens(n, d, usr_name, sku)
def q_azmpc30():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "AZMPC30"
    ir_dens(n, d, usr_name, sku)
def q_mpc30():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "MPC30"
    ir_dens(n, d, usr_name, sku)
def q_btp6():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "BTP6"
    ir_dens(n, d, usr_name, sku)
def q_m5612():
    print()
    print()
    print("\t \t \t NO APLICA")
    print()
    print()
    input("\t \t \t Presiona una tecla para continuar...")
def q_l212():
    print()
    print()
    n = float(input("\t \t Introduce el índice de Refracción:   "))
    d = float(input("\t \t Introduce el peso del líquido en el picnometro:    "))
    sku = "L212"
    ir_dens(n, d, usr_name, sku)



##############################################################################################################################



#FUNCIONES MENU_QUIMICOS (MATERIA PRIMA)
def liquidos():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE QUÍMICOS EN ESTADO LÍQUIDO")
    while True:
        print("\n")
        for index, item in enumerate(list_quim_liquidos, 1):
            print()
            print("\t {}  {}".format(index, item[0]))
        print("\n")
        choice = int(input(" \t Elige una opción:   "))
        if choice < 1 or choice > len(list_quim_liquidos):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            list_quim_liquidos[choice][1]()
        os.system('cls')
list_quim_liquidos = [
["Propelente", propelente],
["Varsol", varsol],
["V-176", v_176],
["Cerflon", cerflon],
["Glicol Eter DB", glicol_DB],
["Molyvan", molivan],
["PAI RICN", pai_ricn],
["Sarsol", sarsol],
["Aceite mineral", aceite_mineral],
["Aceite de silicon 5,000", silicon_5000],
["Grasa de litio", grasa_litio],
["Metanol", metanol],
["Acetona", acetona],
["Xilol", xilol],
["Cloruro de metileno", cloruro_metileno],
["Heptano", heptano],
["Cirrasol G 1096", cirrasol_g_1096],
["Diesel", diesel],
["Glicol Eter EB", glicol_EB],
["Aromina 150", aromina_150],
["Glicol Eter TPM", glicol_tpm],
["NovaSolv 110", novasolv],
["Lubricit TMP", lubricit],
["Agua destilada", agua_destilada],
["Natrasense AG810", natrasense_ag810],
["Cirrasol Expel", cirrasol_expel],
["TPC 1160", tpc_1160],
["Fragancia Brisa Marina", frag_brisa_m],
["Fragancia Vainilla", frag_vainilla],
["Fragancia Auto Nuevo", frag_auto_n],
["Crodazoline", crodazoline],
["Glicerina", glicerina],
["Emulsión de silicón 80%", emulsion_silicon],
["Hidantoina", hidantoina],
["LESS (Lauril Eter Sulfato de Sodio)", less],
["Percloroetileno", percloroetileno],
["Isopropanol", isopropanol],
["Monoetilenglicol", monoetileng],
["Silicón 60,000 cst", silicon_60k],
["Hexyl Cellosolve", hexyl_cell],
["Ecosurf EH-3", ecosurf_eh3],
["Inhibidor de corrosión Base Agua", inhibidor_corrosion_agua],
["Regresa al menu anterior", go_back1]
]
def solidos():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE QUÍMICOS EN ESTADO SÓLIDO")
    while True:
        print("\n")
        for index, item in enumerate(list_quim_solidos, 1):
            print()
            print("\t {}  {}".format(index, item[0]))
        print("\n")
        choice = int(input(" \t Elige una opción:   "))
        if choice < 1 or choice > len(list_quim_solidos):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            list_quim_solidos[choice][1]()
        os.system('cls')
list_quim_solidos = [
["Óxido de Zinc", oxido_zinc],
["Bicarbonato de sodio", bicarbonato_sodio],
["Rojo de metilo", rojo_metilo],
["Solvent RED (rojo)", solvent_red],
["Rosa brillante", rosa_brillante],
["Amarillo Braxime GDCX", amarillo_brax],
["Rojo Braxime RCHX", rojo_brax],
["Verde Esmeralda 5", verde_esmer],
["Dióxido de Titanio", diox_titanio],
["Regresa al menu anterior", go_back1]
]


#FUNCIONES MENU_CONSUMIBLES (MATERIA PRIMA)
def cajas():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE CAJAS")
    while True:
        print("\n")
        for index, item in enumerate(menu_cajas, 1):
            print()
            print("\t {}  {}".format(index, item[0]))
        print("\n")
        choice = int(input(" \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_cajas):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_cajas[choice][1]()
        os.system('cls')
menu_cajas = [
["M4814ES - Limpiador de carburador", c_m4814],
["EB1ES - Desengrasante para motores", c_eb1],
["BTC6ES - Limpiador de terminales de batería", c_btc6],
["M2308ES - Aditivo para gasolina", c_m2308],
["M914ES - Silicón en spray", c_m914],
["L112ES - Aceite penetrante aflojatodo", c_l112],
["NM6ES - Limpiador de partes electrónicas", c_nm6],
["L616ES - Grasa blanca de litio", c_l616],
["L711ES - Lubricante de cables y cadenas", c_l711],
["AZMPC30 - Limpiador de tapicería AUTOZONE", c_azmpc30],
["MPC30ES - Limpiador de tapicería GUNK", c_mpc30],
["BTP6ES - Protector de terminales de batería", c_btp6],
["M5612ES - Limpiador de boya", c_m5612],
["L212ES - Lubricante aflojatodo", c_l212],
["M2616ES - Fuel System Cleaner", c_m2616],
["Regresa al menu anterior", go_back2]
]
def bote():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE BOTE")
    while True:
        print("\n")
        for index, item in enumerate(menu_botes, 1):
            print()
            print("\t {}  {}".format(index, item[0]))
        print("\n")
        choice = int(input(" \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_botes):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_botes[choice][1]()
        os.system('cls')
menu_botes = [
["M4814ES - Limpiador de carburador", b_m4814],
["EB1ES - Desengrasante para motores", b_eb1],
["M2308ES - Aditivo para gasolina", b_m2308],
["M914ES - Silicón en spray", b_m914],
["L112ES - Aceite penetrante aflojatodo", b_l112],
["L616ES - Grasa blanca de litio", b_l616],
["L711ES - Lubricante de cables y cadenas", b_l711],
["AZMPC30 - Limpiador de tapicería AUTOZONE", b_azmpc30],
["M5612ES - Limpiador de boya", b_m5612],
["L212ES - Lubricante aflojatodo", b_l212],
["Bote genérico chico", b_gen_chico],
["Bote genérico grande", b_gen_grande],
["Bote genérico chico c/resina", b_gen_chico_resina],
["Bote genérico grande c/resina", b_gen_grande_resina],
["Bote Sonata 1Lt Natural", b_gen_plastico_sonata1Lt],
["Regresa al menu anterior", go_back2]
]
def tapa():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE TAPA")
    while True:
        print("\n")
        for index, item in enumerate(menu_tapa, 1):
            print()
            print("\t {}  {}".format(index, item[0]))
        print("\n")
        choice = int(input(" \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_tapa):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_tapa[choice][1]()
        os.system('cls')
menu_tapa = [
["Tapa amarilla Liquid Wrench", tapa_amarilla],
["Tapa cepillo AZMPC30/MPC30", tapa_cepillo],
["Tapa negra M2308", tapa_negraM2308],
["Tapa recta chica Azul", tapa_chica_R],
["Tapa recta grande Azul", tapa_grande_R],
["Tapa c/borde chica Azul", tapa_chica_B],
["Tapa c/borde grande Azul", tapa_grande_B],
["Tapa roja M2612", tapa_rojaM5612],
["Tapa 28/410 Natural", tapa_28_410_natural],
["Regresa al menu anterior", go_back2]
]
def etiquetas():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE ETIQUETAS")
    while True:
        print("\n")
        for index, item in enumerate(menu_etiquetas, 1):
            print()
            print("\t {}  {}".format(index, item[0]))
        print("\n")
        choice = int(input(" \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_etiquetas):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_etiquetas[choice][1]()
        os.system('cls')
menu_etiquetas = [
["Etiqueta BTC6ES", etq_btc6],
["Etiqueta BTCPES", etq_btp6],
["Etiqueta NM6ES", etq_nm6],
["Etiqueta MPC30ES", etq_mpc30],
["Etiqueta M2308ES", etq_m2308],
["Etiqueta M2616ES", etq_M2616],
["Etiqueta NM1ES", etq_nm1],
["Etiqueta M206OPE", etq_m206ope],
["Regresa al menu anterior", go_back2]
]
def valv_act():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE VÁLVULAS")
    while True:
        print("\n")
        for index, item in enumerate(menu_valvulas, 1):
            print()
            print("\t {}  {}".format(index, item[0]))
        print("\n")
        choice = int(input(" \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_valvulas):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_valvulas[choice][1]()
        os.system('cls')
menu_valvulas = [
["Válvula chica", v_ch],
["Válvula mediana", v_med],
["Válvula larga", v_gde],
["Válvula espuma", v_espuma],
["Activador espuma", act_espuma],
["Tubo de extensión", tubo_ext],
["Regresa al menu anterior", go_back2]
]
def otros():
    os.system('cls')
    print()
    print("\t \t \t OTROS")
    while True:
        print("\n")
        for index, item in enumerate(menu_otros, 1):
            print()
            print("\t {}  {}".format(index, item[0]))
        print("\n")
        choice = int(input(" \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_otros):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_otros[choice][1]()
        os.system('cls')
menu_otros = [
["Liners M2308", liner_m2308],
["Canicas", canica],
["Regresa al menu anterior", go_back2]
]


#Funciones MENU INVENTARIO
def inv_quim():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE QUÍMICOS")
    while True:
        for index, item in enumerate(menu_inv_quimicos, 1):
            print("\n")
            print("\t{}  {}".format(index, item[0]))
            print()
        print("\n")
        choice = int(input("\t \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_inv_quimicos):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_inv_quimicos[choice][1]()
        os.system('cls')
menu_inv_quimicos = [
["Líquidos", liquidos],
["Sólidos", solidos],
["Regresa al menu anterior", go_back1]
]
def inv_consum():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE CONSUMIBLES")
    while True:
        for index, item in enumerate(menu_inv_consumible, 1):
            print("\n")
            print("\t{}  {}".format(index, item[0]))
            print()
        print("\n")
        choice = int(input("\t \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_inv_consumible):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_inv_consumible[choice][1]()
        os.system('cls')
menu_inv_consumible = [
["Cajas", cajas],
["Bote", bote],
["Tapa", tapa],
["Etiquetas", etiquetas],
["Valvulas y Activadores", valv_act],
["Otros", otros],
["Regresa al menu anterior", go_back1]
]
def inv_prod_term():
    os.system('cls')
    print()
    print("\t \t \t INVENTARIO DE PRODUCTO TERMINADO")
    while True:
        print("\n")
        for index, item in enumerate(menu_prod_term, 1):
            print()
            print("\t {}  {}".format(index, item[0]))
        print("\n")
        choice = int(input(" \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_prod_term):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_prod_term[choice][1]()
        os.system('cls')
menu_prod_term = [
["M4814ES - Limpiador de carburador", PT_m4814],
["EB1ES - Desengrasante para motores", PT_eb1],
["BTC6ES - Limpiador de terminales de batería", PT_btc6],
["M2308ES - Aditivo para gasolina", PT_m2308],
["M914ES - Silicón en spray", PT_m914],
["L112ES - Aceite penetrante aflojatodo", PT_l112],
["NM6ES - Limpiador de partes electrónicas", PT_nm6],
["L616ES - Grasa blanca de litio", PT_l616],
["L711ES - Lubricante de cables y cadenas", PT_l711],
["AZMPC30 - Limpiador de tapicería AUTOZONE", PT_azmpc30],
["MPC30ES - Limpiador de tapicería GUNK", PT_mpc30],
["BTP6ES - Protector de terminales de batería", PT_btp6],
["M5612ES - Limpiador de boya", PT_m5612],
["L212ES - Lubricante aflojatodo", PT_l212],
["Regresa al menu anterior", go_back1]
]



#FUNCION ACTUALIZACIÓN DE INVENTARIOS PARA PRODUCCIÓN
def inventarios_q_c(formula, usr_name, cp, bp):
    consumible = formula

    lista_sus = []
    lista_cont = []
    dict_temp = {}

    lista_consu = []
    lista_c_cant = []
    dict_temp2 = {}

    lista_nom = [formula]
    lista_cajas = [cp]
    dict_temp3 = {}

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(formula + '.csv','r')as f:
        data = csv.reader(f)
        next(data)

        for row in data:
            lista_sus.append(row[0])
            masa = round(float(row[1])*bp/1000,3)
            lista_cont.append(masa)

    with open(consumible + '_consumible.csv','r')as g:
        data_c = csv.reader(g)
        next(data_c)

        for row in data_c:
            lista_consu.append(row[0])
            cant_tot = round(float(row[1])*bp, 1)
            lista_c_cant.append(cant_tot)

    dict_temp = dict(zip(lista_sus, lista_cont))
    dict_temp2 = dict(zip(lista_consu, lista_c_cant))
    dict_temp3 = dict(zip(lista_nom, lista_cajas))

    tablaquim = pd.read_csv('inventarioquimicos.csv', encoding='latin-1')  ##Actualización de inventario químicos
    indexes = tablaquim.index
    for i in indexes:
        a = tablaquim.iat[i, 0]
        b = tablaquim.iat[i, 1]
        for k in dict_temp.keys():
            if a == k:
                v = dict_temp[k]
                new = b - v
                nombre = tablaquim.iat[i, 2]
                if new > 0:
                    tablaquim.iat[i, 1] = new
                    tablaquim.to_csv('inventarioquimicos.csv', index=False)
                    reg = [date, "Consumido", v, usr_name, k, "Kilogramos"]
                    registrofile = open("registro.csv", 'a', newline='')
                    wr = csv.writer(registrofile)
                    wr.writerow(reg)
                    registrofile.close()
                    if new < 5:
                        print("\t \t Revisa tus inventarios. Hay menos de 5 kg de ", nombre, " en la planta" )
                        print("\t \t Presiona ENTER para continuar...")
                        input()

                else:
                    tablaquim.iat[i, 1] = 0
                    tablaquim.to_csv('inventarioquimicos.csv', index=False)
                    reg = [date, "Consumido", v, usr_name, k, "Kilogramos"]
                    registrofile = open("registro.csv", 'a', newline='')
                    wr = csv.writer(registrofile)
                    wr.writerow(reg)
                    registrofile.close()
                    print("\t \t Revisa tus inventarios. se acabó el ", nombre)
                    print("\t \t Presiona ENTER para continuar...")
                    input()

    tablaconsu = pd.read_csv('inventarioconsumibles.csv', encoding='latin-1')   ##Actualización de inventario consumibles
    indexes = tablaconsu.index
    for i in indexes:
        a = tablaconsu.iat[i, 0]
        b = tablaconsu.iat[i, 1]
        for k in dict_temp2.keys():
            if a == k:
                v = dict_temp2[k]
                new = b - v
                nombre = tablaconsu.iat[i, 2]
                if new > 0:
                    tablaconsu.iat[i, 1] = new
                    tablaconsu.to_csv('inventarioconsumibles.csv', index=False)
                    reg = [date, "Consumido", v, usr_name, k, "Piezas"]
                    registrofile = open("registro.csv", 'a', newline='')
                    wr = csv.writer(registrofile)
                    wr.writerow(reg)
                    registrofile.close()
                    if new < 1000:
                        print("\t \t Revisa tus inventarios. Hay menos de 1000 piezas de ", nombre, " en la planta" )
                        print("\t \t Presiona ENTER para continuar...")
                        input()
                else:
                    tablaconsu.iat[i, 1] = 0
                    tablaconsu.to_csv('inventarioconsumibles.csv', index=False)
                    reg = [date, "Consumido", v, usr_name, k, "Piezas"]
                    registrofile = open("registro.csv", 'a', newline='')
                    wr = csv.writer(registrofile)
                    wr.writerow(reg)
                    registrofile.close()
                    print()
                    print("\t \t Revisa tus inventarios. Se acabó el ", nombre)
                    print("\t \t Presiona ENTER para continuar...")
                    input()

    tablaproducc = pd.read_csv('inventario_produccion.csv', encoding='latin-1')
    indexes = tablaproducc.index
    for i in indexes:
        a = tablaproducc.iat[i, 0]
        b = tablaproducc.iat[i, 1]
        for k in dict_temp3.keys():
            if a == k:
                v = dict_temp3[k]
                new = b + v
                tablaproducc.iat[i, 1] = new
                tablaproducc.to_csv('inventario_produccion.csv', index=False)
                reg = [date, "Entrada", v, usr_name, k, "Producto terminado"] #revisar para que concuerde con el registro
                registrofile = open("registro.csv", 'a', newline='')
                wr = csv.writer(registrofile)
                wr.writerow(reg)
                registrofile.close()
                print()

    print()
    print("\t \t Se registraron ", cp," cajas de ", formula)
    print()
    print()
    print("\t \t Presiona una tecla para continuar")
    input()
def inventario_consumibles_(n, codigo, usr_name):

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tablaconsu = pd.read_csv('inventarioconsumibles.csv', encoding='latin-1')   ##Actualización de inventario consumibles
    indexes = tablaconsu.index
    for i in indexes:
        a = tablaconsu.iat[i, 0]
        b = tablaconsu.iat[i, 1]
        nombre = tablaconsu.iat[i, 2]
        if a == codigo:
            new = b + x*n
            tablaconsu.iat[i, 1] = new
            tablaconsu.to_csv('inventarioconsumibles.csv', index=False)
            if x > 0:
                print()
                comentario = input("\t \t Agrega un comentario:  ")
                reg = [date, "Entrada", n, usr_name, nombre, "Piezas", comentario]
                registrofile = open("registro.csv", 'a', newline='')
                wr = csv.writer(registrofile)
                wr.writerow(reg)
                registrofile.close()
                print()
                print("\t \t Se registró la Entrada de ", n," piezas de ", nombre)
                print()
                print()
                print("\t \t Presiona una tecla para continuar")
                input()
            else:
                print()
                comentario = input("\t \t Agrega un comentario:  ")
                reg = [date, "Salida", n, usr_name, nombre, "Piezas", comentario]
                registrofile = open("registro.csv", 'a', newline='')
                wr = csv.writer(registrofile)
                wr.writerow(reg)
                registrofile.close()
                print()
                print("\t \t Se registró la Salida de ", n," piezas de ", nombre)
                print()
                print()
                print("\t \t Presiona una tecla para continuar")
                input()
def inventario_quimicos_(n, codigo, usr_name):

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tablaquim = pd.read_csv('inventarioquimicos.csv', encoding='latin-1')   ##Actualización de inventario consumibles
    indexes = tablaquim.index
    for i in indexes:
        a = tablaquim.iat[i, 0]
        b = tablaquim.iat[i, 1]
        nombre = tablaquim.iat[i, 2]
        if a == codigo:
            new = round(b + x*n,3)
            tablaquim.iat[i, 1] = new
            tablaquim.to_csv('inventarioquimicos.csv', index=False)
            if x > 0:
                print()
                comentario = input("\t \t Agrega un comentario:  ")
                reg = [date, "Entrada", n, usr_name, nombre, "Kilogramos", comentario]
                registrofile = open("registro.csv", 'a', newline='')
                wr = csv.writer(registrofile)
                wr.writerow(reg)
                registrofile.close()
                print()
                print("\t \t Se registró la Entrada de ", n," kilogramos de ", nombre)
                print()
                print()
                print("\t \t Presiona una tecla para continuar")
                input()
            else:
                print()
                comentario = input("\t \t Agrega un comentario:  ")
                reg = [date, "Salida", n, usr_name, nombre, "Kilogramos", comentario]
                registrofile = open("registro.csv", 'a', newline='')
                wr = csv.writer(registrofile)
                wr.writerow(reg)
                registrofile.close()
                print()
                print("\t \t Se registró la Salida de ", n," kilogramos de ", nombre)
                print()
                print()
                print("\t \t Presiona una tecla para continuar")
                input()
def inventario_producto_terminado(n, codigo, usr_name):

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tablaproducc = pd.read_csv('inventario_produccion.csv', encoding='latin-1')
    indexes = tablaproducc.index
    for i in indexes:
        a = tablaproducc.iat[i, 0]
        b = tablaproducc.iat[i, 1]
        if a == codigo:
            new = b + x*n
            if new < 0:
                print("\t \t ERROR - Estas dandole salida a más cajas de las que están registradas")
                print("\t \t Intentalo de nuevo....")
                input()
            else:
                tablaproducc.iat[i, 1] = new
                tablaproducc.to_csv('inventario_produccion.csv', index=False)
                if x > 0:
                    print()
                    comentario = input("\t \t Agrega un comentario:  ")
                    reg = [date, "Entrada", n, usr_name, a, "Producto terminado", comentario]
                    registrofile = open("registro.csv", 'a', newline='')
                    wr = csv.writer(registrofile)
                    wr.writerow(reg)
                    registrofile.close()
                    print()
                    print("\t \t Se registró la Entrada de ", n," cajas de ", a)
                    print()
                    print()
                    print("\t \t Presiona una tecla para continuar")
                    input()
                else:
                    print()
                    comentario = input("\t \t Agrega un comentario:  ")
                    reg = [date, "Salida", n, usr_name, a, "Producto terminado facturado", comentario]
                    registrofile = open("registro.csv", 'a', newline='')
                    wr = csv.writer(registrofile)
                    wr.writerow(reg)
                    registrofile.close()
                    print()
                    print("\t \t Se registró la Salida de ", n," cajas de ", a)
                    print()
                    print()
                    print("\t \t Presiona una tecla para continuar")
                    input()

#FUNCION PARA REGISTRO DE DATOS DE CALIDAD  (I.R. Y DENSIDAD)
def ir_dens(n, d, usr_name, sku):

    den_fin = round(d/50,3)
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    reg = [date, usr_name, n, den_fin, sku]
    registrofile = open("registro_calidad.csv", 'a', newline='')
    wr = csv.writer(registrofile)
    wr.writerow(reg)
    registrofile.close()
    print()
    print("\t \t Se realizó el registro")
    print()
    print()
    print("\t \t Presiona una tecla para continuar")
    input()

#PRIMER MENU DEL PROGRAMA
def calidad():
    os.system('cls')
    print()
    print("\t \t \t CALIDAD")
    def menu_quality(menu_prod):
        while True:
            print("\n")
            for index, item in enumerate(menu_calidad, 1):
                print()
                print("\t {}  {}".format(index, item[0]))
            print("\n")
            choice = int(input(" \t Elige una opción:   "))
            if choice < 1 or choice > len(menu_calidad):
                print()
                print("\t Elige una opción correcta")
                input()
                os.system('cls')
            else:
                choice = choice - 1
                menu_calidad[choice][1]()
            os.system('cls')
    menu_quality(menu_prod)
menu_calidad = [
["M4814ES - Limpiador de carburador", q_m4814],
["EB1ES - Desengrasante para motores", q_eb1],
["BTC6ES - Limpiador de terminales de batería", q_btc6],
["M2308ES - Aditivo para gasolina", q_m2308],
["M914ES - Silicón en spray", q_m914],
["L112ES - Aceite penetrante aflojatodo", q_l112],
["NM6ES - Limpiador de partes electrónicas", q_nm6],
["L616ES - Grasa blanca de litio", q_l616],
["L711ES - Lubricante de cables y cadenas", q_l711],
["AZMPC30 - Limpiador de tapicería AUTOZONE", q_azmpc30],
["MPC30ES - Limpiador de tapicería GUNK", q_mpc30],
["BTP6ES - Protector de terminales de batería", q_btp6],
["M5612ES - Limpiador de boya", q_m5612],
["L212ES - Lubricante aflojatodo", q_l212],
["Regresa al menu anterior", go_back]
]
def menu_princ_produccion():
    os.system('cls')
    print()
    print("\t \t \t MENU DE FÓRMULAS")
    def menu_produccion(menu_prod):
        while True:
            print("\n")
            for index, item in enumerate(menu_prod, 1):
                print()
                print("\t {}  {}".format(index, item[0]))
            print("\n")
            choice = int(input(" \t Elige una opción:   "))
            if choice < 1 or choice > len(menu_prod):
                print()
                print("\t Elige una opción correcta")
                input()
                os.system('cls')
            else:
                choice = choice - 1
                menu_prod[choice][1]()
            os.system('cls')
    menu_produccion(menu_prod)
menu_prod = [
["M4814ES - Limpiador de carburador", p_m4814],
["EB1ES - Desengrasante para motores", p_eb1],
["BTC6ES - Limpiador de terminales de batería", p_btc6],
["M2308ES - Aditivo para gasolina", p_m2308],
["M914ES - Silicón en spray", p_m914],
["L112ES - Aceite penetrante aflojatodo", p_l112],
["NM6ES - Limpiador de partes electrónicas", p_nm6],
["L616ES - Grasa blanca de litio", p_l616],
["L711ES - Lubricante de cables y cadenas", p_l711],
["AZMPC30 - Limpiador de tapicería AUTOZONE", p_azmpc30],
["MPC30ES - Limpiador de tapicería GUNK", p_mpc30],
["BTP6ES - Protector de terminales de batería", p_btp6],
["M5612ES - Limpiador de boya", p_m5612],
["L212ES - Lubricante aflojatodo", p_l212],
["Regresa al menu anterior", go_back]
]
def materia_prima():
    os.system('cls')
    print()
    print()
    print('\t \t ¿Qué vas a registrar? ¿ENTRADAS O SALIDAS?')
    def pregunta():
        print()
        print("\t \t Selecciona una opción")
        print()
        print("\t \t1 - ENTRADAS")
        print("\t \t2 - SALIDAS")
        print("\t \t3 - salir")
        print()

    pregunta()
    global x
    opcion_pregunta = input("\t \t inserta un numero valor >> ")

    if opcion_pregunta == "1":
        x = 1
        os.system('cls')
    elif opcion_pregunta == "2":
        x = -1
        os.system('cls')
    elif opcion_pregunta == "3":
        go_back()
    else:
        print()
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

    while True:
        print()
        print("\t \t \t MENU MATERIA PRIMA")
        for index, item in enumerate(menu_inventarios, 1):
            print("\n")
            print("\t{}  {}".format(index, item[0]))
            print()
        print("\n")
        choice = int(input("\t \t Elige una opción:   "))
        if choice < 1 or choice > len(menu_inventarios):
            print()
            print("\t Elige una opción correcta")
            input()
            os.system('cls')
        else:
            choice = choice - 1
            menu_inventarios[choice][1]()
        os.system('cls')
menu_inventarios = [
["Químicos", inv_quim],
["Consumibles (bote, caja, etiquetas, etc.)", inv_consum],
["Producto terminado", inv_prod_term],
["Regresa al menu anterior", go_back]
]
def salir():
    print()
    for i in range(len(animation)):
        time.sleep(0.1)
        sys.stdout.write("\r \t \t Closing: " + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    print()
    print()
    print("\t \t Ya puedes cerrar esta ventana...")
    print()
    print()
    quit()



#FUNCION DE EJECUCIÓN DEL MENU PRINCIPAL
def menu_principal(main_menu):
    while True:
        try:
            for index, item in enumerate(main_menu, 1):
                print("\n")
                print("\t{}  {}".format(index, item[0]))
                print()
            print("\n")
            choice = int(input("\t \t Elige una opción:   "))
            if choice < 1 or choice > len(main_menu):
                print()
                print("\t Elige una opción correcta")
                input()
                os.system('cls')
            else:
                choice = choice - 1
                main_menu[choice][1]()
            os.system('cls')
        except ValueError:
            print()
            print("\t \t ERROR!!   Debes introducir un número y luego presiona la tecla 'Enter'")
            input("\t \t Prueba de nuevo...")
            os.system('cls')
main_menu = [
["Calidad", calidad],
["Producción", menu_princ_produccion],
["Materia Prima y Producto Terminado", materia_prima],
["Salir", salir]
]



print()
print()
print()
print()
print()
print()
print()
usr_name = input("\t \t Nombre de usuario:   ")
animation = [
"[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□]", "[■■■□□□□□□□□□□□□□□□□□]", "[■■■■□□□□□□□□□□□□□□□□]",
"[■■■■■□□□□□□□□□□□□□□□]", "[■■■■■■□□□□□□□□□□□□□□]", "[■■■■■■■□□□□□□□□□□□□□]", "[■■■■■■■■□□□□□□□□□□□□]", "[■■■■■■■■■□□□□□□□□□□□]", "[■■■■■■■■■■□□□□□□□□□□]",
"[■■■■■■■■■■■■□□□□□□□□]", "[■■■■■■■■■■■■■■■□□□□□]", "[■■■■■■■■■■■■■■■■□□□□]", "[■■■■■■■■■■■■■■■■■■■■]"
]
print()
for i in range(len(animation)):
    time.sleep(0.07)
    sys.stdout.write("\r \t \t Loading: " + animation[i % len(animation)])
    sys.stdout.flush()
print()
os.system('cls')
menu_principal(main_menu)
