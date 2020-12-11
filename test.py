import copy
import re

sample_dict = {
        "posicaoConsolidada": {
        "tabelaPosicaoConsolidada": [
            {
                "descricao": {
                    "texto": "(+) SDO PROVIS\u00d3RIO CTA CORR",
                    "textoAcessivel": "SDO PROVIS\u00d3RIO CTA CORR"
                },
                "valor": "247,67",
                "positivo": False,
                "totalizador": False,
                "limiteAdicional": False,
                "saldoDisponivelEDevedorValor": None,
                "parceleConsignadoCrediario": None,
                "parceleSobMedida": None
            },
            {
                "descricao": {
                    "texto": "(+) SALDO PROVIS\u00d3RIO POUP AUT",
                    "textoAcessivel": "SALDO PROVIS\u00d3RIO POUP AUT"
                },
                "valor": "1.710,73",
                "positivo": True,
                "totalizador": False,
                "limiteAdicional": False,
                "saldoDisponivelEDevedorValor": None,
                "parceleConsignadoCrediario": None,
                "parceleSobMedida": None
            },
            {
                "descricao": {
                    "texto": "(=) SALDO DISPON\u00cdVEL PARA SAQUE",
                    "textoAcessivel": "SALDO DISPON\u00cdVEL PARA SAQUE"
                },
                "valor": "1.463,06",
                "positivo": True,
                "totalizador": True,
                "limiteAdicional": False,
                "saldoDisponivelEDevedorValor": False,
                "parceleConsignadoCrediario": False,
                "parceleSobMedida": False
            },
            {
                "descricao": {
                    "texto": "(=) SDO DISP P/ APLIC HOJE",
                    "textoAcessivel": "SDO DISP P/ APLIC HOJE"
                },
                "valor": "1.463,06",
                "positivo": True,
                "totalizador": False,
                "limiteAdicional": False,
                "saldoDisponivelEDevedorValor": None,
                "parceleConsignadoCrediario": None,
                "parceleSobMedida": None
            },
            {
                "descricao": {
                    "texto": "CHEQUE ESPECIAL - LIS (SUJEITO A ENCARGOS)",
                    "textoAcessivel": "CHEQUE ESPECIAL - LIS (SUJEITO A ENCARGOS)"
                },
                "valor": "9.120,00",
                "positivo": True,
                "totalizador": False,
                "limiteAdicional": True,
                "saldoDisponivelEDevedorValor": None,
                "parceleConsignadoCrediario": None,
                "parceleSobMedida": None
            },
            {
                "descricao": {
                    "texto": "CHEQUE ESPECIAL DISPON\u00cdVEL",
                    "textoAcessivel": "CHEQUE ESPECIAL DISPON\u00cdVEL"
                },
                "valor": "9.120,00",
                "positivo": True,
                "totalizador": True,
                "limiteAdicional": False,
                "saldoDisponivelEDevedorValor": None,
                "parceleConsignadoCrediario": None,
                "parceleSobMedida": None
            }
        ]
    }
}


list_of_keys = ['posicaoConsolidada','tabelaPosicaoConsolidada','descricao','texto']

list_of_keys_1 = ['posicaoConsolidada','tabelaPosicaoConsolidada','valor']

def extract_key(sample_dict,list_of_keys):

    def extract(sample_dict,list_of_keys,arr):
        if isinstance(sample_dict,dict):

            if check_key_present_in_dict(sample_dict,list_of_keys[0]):
                if len(list_of_keys)>1:
                    list_of_keys.pop(0)
                    for k,v in sample_dict.items():
                        extract(v,list_of_keys,arr)
                else:
                    arr.append(sample_dict[list_of_keys[0]])
            else:
                return None
        elif isinstance(sample_dict,list):
            dummy = copy.deepcopy(list_of_keys)
            for i in sample_dict:
                extract(i,dummy,arr)
                dummy = copy.deepcopy(list_of_keys)
        return arr

    arr = []
    values = extract(sample_dict,list_of_keys,arr)
    return values
            


def check_key_present_in_dict(dict_one,key):
    for k,v in dict_one.items():
        if k==key:
            return v
    return False


list_of_values = extract_key(sample_dict,list_of_keys)

print(list_of_values)

def extract_value(sample_dict,list_of_keys):
    if isinstance(sample_dict,dict):
        print('Hi')
        if check_key_present_in_dict(sample_dict,list_of_keys[0]):
            if len(list_of_keys)>1:
                list_of_keys.pop(0)
                for k,v in sample_dict.items():
                    extract_value(v,list_of_keys)
            else:
                return sample_dict[list_of_keys[0]]
        else:
            return None
    elif isinstance(sample_dict,list):
        i = list_of_keys[0]
        list_of_keys.pop(0)
        extract_value(sample_dict[i],list_of_keys)

for i in list_of_values:
    if re.search(".*{}.*".format('SDO PROVISÓRI'),i):
        index = list_of_values.index(i)
        current_balance=sample_dict['posicaoConsolidada']['tabelaPosicaoConsolidada'][index]['valor']
        print(current_balance)
        break


