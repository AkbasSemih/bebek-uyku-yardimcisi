# fuzzy_logic.py

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Girdilerim
isik = ctrl.Antecedent(np.arange(0, 101, 1), 'isik')
sicaklik = ctrl.Antecedent(np.arange(15, 31, 1), 'sicaklik')
ses = ctrl.Antecedent(np.arange(0, 101, 1), 'ses')
aktivite = ctrl.Antecedent(np.arange(0, 11, 1), 'aktivite')
uyku = ctrl.Antecedent(np.arange(0, 181, 1), 'uyku')

# Çıktılarım
uyuma = ctrl.Consequent(np.arange(0, 101, 1), 'uyuma')
destek = ctrl.Consequent(np.arange(0, 4, 1), 'destek')

# Üyelik fonksiyonlarım
isik['dusuk'] = fuzz.trimf(isik.universe, [0, 0, 50])
isik['orta'] = fuzz.trimf(isik.universe, [30, 50, 70])
isik['yuksek'] = fuzz.trimf(isik.universe, [50, 100, 100])

sicaklik['dusuk'] = fuzz.trimf(sicaklik.universe, [15, 15, 22])
sicaklik['ideal'] = fuzz.trimf(sicaklik.universe, [20, 23, 26])
sicaklik['yuksek'] = fuzz.trimf(sicaklik.universe, [24, 30, 30])

ses['dusuk'] = fuzz.trimf(ses.universe, [0, 0, 40])
ses['orta'] = fuzz.trimf(ses.universe, [30, 50, 70])
ses['yuksek'] = fuzz.trimf(ses.universe, [60, 100, 100])

aktivite['az'] = fuzz.trimf(aktivite.universe, [0, 0, 5])
aktivite['cok'] = fuzz.trimf(aktivite.universe, [4, 10, 10])

uyku['yeni'] = fuzz.trimf(uyku.universe, [0, 0, 60])
uyku['eski'] = fuzz.trimf(uyku.universe, [30, 180, 180])

uyuma['dusuk'] = fuzz.trimf(uyuma.universe, [0, 0, 50])
uyuma['orta'] = fuzz.trimf(uyuma.universe, [30, 50, 70])
uyuma['yuksek'] = fuzz.trimf(uyuma.universe, [50, 100, 100])

destek['sessizlik'] = fuzz.trimf(destek.universe, [0, 0, 1])
destek['ninni'] = fuzz.trimf(destek.universe, [0, 1, 2])
destek['ortam'] = fuzz.trimf(destek.universe, [1, 2, 3])
destek['yok'] = fuzz.trimf(destek.universe, [2, 3, 3])

rules = [
    ctrl.Rule(isik['dusuk'] & ses['dusuk'] & sicaklik['ideal'] & aktivite['cok'] & uyku['eski'], (uyuma['yuksek'], destek['ninni'])),
    ctrl.Rule(isik['yuksek'] | ses['yuksek'], (uyuma['dusuk'], destek['sessizlik'])),
    ctrl.Rule(sicaklik['dusuk'] | sicaklik['yuksek'], (uyuma['dusuk'], destek['ortam'])),
    ctrl.Rule(uyku['yeni'], (uyuma['dusuk'], destek['yok'])),
    ctrl.Rule(isik['orta'] & ses['orta'], (uyuma['orta'], destek['ninni'])),
]

uyku_kontrol = ctrl.ControlSystem(rules)
uyku_simulasyon = ctrl.ControlSystemSimulation(uyku_kontrol)

def hesapla(isik_val, sicaklik_val, ses_val, aktivite_val, uyku_val):
    uyku_simulasyon.input['isik'] = isik_val
    uyku_simulasyon.input['sicaklik'] = sicaklik_val
    uyku_simulasyon.input['ses'] = ses_val
    uyku_simulasyon.input['aktivite'] = aktivite_val
    uyku_simulasyon.input['uyku'] = uyku_val

    uyku_simulasyon.compute()

    uyuma_sonuc = round(uyku_simulasyon.output['uyuma'])
    destek_sonuc = round(uyku_simulasyon.output['destek'])

    return uyuma_sonuc, destek_sonuc
