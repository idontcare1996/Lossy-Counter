# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 12:28:34 2018
"""
print ( """
 AUTOR: Carlos Oliveira n. 88702

 Algoritmo baseado no exemplo em pseudo-código de:

 Graham Cormode e Marios Hadjieleftheriou
 (Algorithm 2: LossyCounting(k))
 G. Cormode & M. Hadjieleftheriou, Finding the frequent items in streams of
 data, Commun. ACM, Vol. 52, N. 10, 2009
                       e
 Gurmeet Singh Manku
 G.S. Manku. Frequency counts over data streams.
 http://www.cse.ust.hk/vldb2002/VLDB2002-proceedings/slides/S10P03slides.pdf, 2002

""")

import math
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter


def generate_datastream(size):

    generated_datastream=[]

    alphabet = ['a','b','c','d','e','f',
                'g','h','i','j','k','l',
                'm','n','o','p','q','r',
                's','t','u','v','w','x',
                'y','z']

    gamma = np.random.gamma(1,5,26)
    gamma = np.array(gamma)
    gamma /= gamma.sum()

    #print (gamma)

    for i in range (0,size):
        generated_datastream.append(np.random.choice(alphabet,p=gamma))

   #print (generated_datastream)
    return generated_datastream;

def get_next_character(f):
    """Reads one character from the given textfile"""
    c = f.read(1)
    while c:
        yield c
        c = f.read(1)

def datastream_to_file(datastream,size):
    filename = "datastreams/"+str(size) + ".txt"

    isFileOpen = False
    try:
        myFile = open(filename, mode="w", encoding="utf-8")
        isFileOpen = True
    except FileNotFoundError:
        print("oops, sorry, didn't find the file... my bad")
    except IOError:
        print("There was an IO error")
    except:
        print("Sorry, I don't know what went wrong")

        #if the file is open, start writing/appending to it
    if isFileOpen:
        print(" File successfully opened. \n Writing datastream to it")
        for each in datastream:

            myFile.write(each)
            myFile.write("  ")
        myFile.close()
        print ( " \n\n\n\n Datastream criada, por favor corra o programa novamente para começar a análise \n\n\n\n")

def file_to_datastream(size):
    filename = "datastreams/"+str(size) + ".txt"

    isFileOpen = False
    try:
        myFile = open(filename, mode="r", encoding="utf-8")
        isFileOpen = True
    except FileNotFoundError:
        print("oops, sorry, didn't find the file... my bad")
        print(" I'll create a new one... ")
        datastream_to_file(generate_datastream(size),size)
        file_to_datastream(size)
    except IOError:
        print("There was an IO error")
    except:
        print("Sorry, I don't know what went wrong")

        #if the file is open, start writing/appending to it
    read_datastream = []
    if isFileOpen:

        for c in get_next_character(myFile):
            if (c!=' '):

                read_datastream.append(c)
    return read_datastream




def LossyCounting (k, datastream):

    lista = {}          # Dicionário Vazio
    current_window = 1  # nº da janela
    n_items = 0         # Nº. de items processados
    #epsylon = 0.2       # User specified error threshhold

    for each_item in datastream:

        x=each_item     # Coloca em x o item a ler
        n_items+=1      # Aumenta o contador


        """ Inserção """
        if ( x in lista):
            previous_value = lista.get(x,"none")
            new_value = [previous_value[0]+1,previous_value[1]]
            lista[x]= new_value

        else:
            new_list = [1,(current_window)-1]
            lista[x]=new_list

        #print ("lista: ",lista)

        """ Remoção """
        if ((n_items % k )==0):

            L = list(lista.keys())
            for each_element in L:
                i = each_element
                previous_value = list(lista.get(i,"none"))
                freq = previous_value[0]
                delta = previous_value[1]
                #print (previous_value,freq,delta)
                if (freq + delta <= current_window):
                    del lista[i]
            current_window+=1;

    return lista


def print_statistics (datastream, lista_final,size):

    """ Arranjar as frequências absolutas de cada char
        e comparar com a lista criada pelo algoritmo"""

    cs = Counter(datastream)

    Lista_cs = list(cs.keys())
    Lista_lf = list(lista_final.keys())


    print ("\n Items marcados com *5% ou *10% ocorrem mais de 5% ou 10% das vezes, respectivamente"  )

    print ("\n Caracteres presentes na lista criada pelo algoritmo e \n presentes na datastream: ")
    Lista_lf_cs = [x for x in Lista_cs if x in Lista_lf]

    print ("\n ",Lista_lf_cs,"\n")
    print ("\n \t\t[\tValores certos\t\t][\tValores do algoritmo\t\t ]")
    for each_cs in Lista_lf_cs:

        fa = cs.get(each_cs,"none")
        fr = (fa/size * 100)
        fLC = (lista_final.get(each_cs,"none"))[0]
        deltaLC = (lista_final.get(each_cs,"none"))[1]

        if ( fLC+deltaLC > size*0.05):
            if (fLC+deltaLC > size*0.1):
                per100 = " \t->10%"
            else:
                per100 = " \t->5%"
        else:
            per100=""



        print ("\tChar: ",each_cs," f.abs.:",fa,"\t f.rel.:","%.1f%%"%(fr),"\t| f.LC.: ", fLC,"\t +/-",deltaLC,per100)


    print ("\n Caracteres ausentes da lista criada pelo algoritmo mas \n presentes na datastream: ")
    Lista_cs_lf = [x for x in Lista_cs if x not in Lista_lf]

    print ("\n ",Lista_cs_lf,"\n")

    for each_cs in Lista_cs_lf:
        fa = cs.get(each_cs,"none")
        fr = (fa/size * 100)
        print ("\tChar: ",each_cs," f.abs.:",fa,"\t f.rel.:","%.1f%%"%(fr))




""" Início do programa """

tamanho_datastream = 100
epsylon_setting = 0.2          #Threshold
multiplier = tamanho_datastream

""" Caso seja necessário outro valor de k, descomentar o valor de k """
k = math.ceil((1/epsylon_setting))     # tamanho da window (contadores associados)

# k= 20


print ( " A correr o algoritmo Lossy Compression \n para dataset de tamanho: [",tamanho_datastream,"] ...")

ds = file_to_datastream(tamanho_datastream)
lf = LossyCounting(k,ds)
print_statistics(ds,lf,tamanho_datastream)


