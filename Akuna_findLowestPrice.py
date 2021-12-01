#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findLowestPrice' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_STRING_ARRAY products
#  2. 2D_STRING_ARRAY discounts
#

def findLowestPrice(products, discounts):
    # Write your code here
    
    # reformats discounts
    dict_discounts = {}
    for discount in discounts:
        dict_discounts[discount[0]] = [int(discount[1]), int(discount[2])]
                                      # type of discount, discount amount
    print(dict_discounts)
                                      
    total = 0
    
    print(products)
    # ring up all the products
    for product in products:
        print(product)
        og_price = int(product[0])
        min_price = og_price
    
        # apply all the discounts and find the smallest
        for i in range(1, len(product)):
            temp_price = og_price
            if product[i] == 'EMPTY':
                pass
            else:
                if dict_discounts[product[i]][0] == 0:
                    # New fixed price
                    temp_price = dict_discounts[product[i]][1]
                elif dict_discounts[product[i]][0] == 1:
                    # % off
                    temp_price = (100 - dict_discounts[product[i]][1]) * og_price / 100
                elif dict_discounts[product[i]][0] == 2:
                    # Flat discount
                    temp_price =  og_price - dict_discounts[product[i]][1]
                print("  Possible Discount:", temp_price, product[i])
                
            # find the discord
            if temp_price < min_price:
                min_price = temp_price
            
        print("Min:", min_price) 
        total += int(min_price)
        
    return total

if __name__ == '__main__':


#     {
#     'mSFzy': [0, 40068],
#     'GuedKICl6': [2, 563],
#     'qx3V87rxx4': [2, 405],
#     'UBVfZu': [0, 53174], 'Vfg3XA': [0, 67319], 'KcK': [2, 584], 'zthJCK9m': [0, 74047], 'z63J1yVl': [0, 53893], 'DccoWGq0P': [0, 74166], 'WF2hiGHyy': [0, 66024], 'K9': [2, 619], 'bc60t': [2, 861], 's465': [0, 80175], '2qqLvKvI9p': [0, 83969], 'q4e9j3': [1, 37], '1': [1, 80], 'kxVnBd': [1, 44], 'bB50QilPDY': [1, 63], 'di': [2, 516], 'YDys': [1, 16], 'L': [0, 78440], '4eeL9': [1, 65], 'P': [2, 495], 'GsEAR61': [2, 607], 'DiRO05Jo': [0, 84886], 'ELFk03EQkh': [2, 817], 'KmXQ': [2, 972], 'NPE4mO6Fr': [0, 11472], 'f17xdvkp': [2, 42], 'Toa7j': [1, 20], 'q': [1, 34], 'e9HnvE': [0, 41655]}
# [['97326', 'P', 'GuedKICl6', 'GsEAR61', 'EMPTY', 'GsEAR61', 'GsEAR61', 'GuedKICl6', 'Vfg3XA', 'WF2hiGHyy', 'z63J1yVl', 'EMPTY', 'Toa7j', 'EMPTY', 'P', 'WF2hiGHyy', 'YDys', 'Vfg3XA', 'KmXQ', 'f17xdvkp', 'bB50QilPDY', 'di', '1', 'GuedKICl6', 'DccoWGq0P', 'EMPTY'], ['97170', 'K9', 'qx3V87rxx4', 'KmXQ', 'L', '1', 'bc60t', 'f17xdvkp', 'KcK', 'ELFk03EQkh', 'Toa7j', 'Toa7j', 'Toa7j', 'EMPTY', 'mSFzy', 'EMPTY', 's465', 'e9HnvE', 's465', 'EMPTY', 'EMPTY', 'WF2hiGHyy', 'EMPTY', 'K9', 'EMPTY', 'EMPTY'], ['94478', 'qx3V87rxx4', 'Vfg3XA', 'DccoWGq0P', 'YDys', '1', 's465', 'bB50QilPDY', 'bc60t', 'ELFk03EQkh', 'DccoWGq0P', 'KcK', 'qx3V87rxx4', 'bc60t', 'q4e9j3', 'EMPTY', 'EMPTY', 'bc60t', 'UBVfZu', 'EMPTY', 'KcK', 'Vfg3XA', 'EMPTY', '4eeL9', 'kxVnBd', '2qqLvKvI9p'], ['87136', 'EMPTY', 'WF2hiGHyy', 'K9', 'EMPTY', 'EMPTY', 'DiRO05Jo', 'EMPTY', 'EMPTY', 'z63J1yVl', 'q4e9j3', 'di', 'Toa7j', 'EMPTY', 'UBVfZu', 'EMPTY', 'EMPTY', 'WF2hiGHyy', 'EMPTY', '4eeL9', 'P', 'bc60t', 'YDys', 'EMPTY', 'bB50QilPDY', 'EMPTY'], ['95427', 'K9', 'bc60t', 'UBVfZu', 'zthJCK9m', 'K9', 'ELFk03EQkh', 'WF2hiGHyy', 'di', 'EMPTY', 'q', 'di', 'EMPTY', 'EMPTY', 'bB50QilPDY', 'UBVfZu', 'DiRO05Jo', 'EMPTY', 'WF2hiGHyy', 'ELFk03EQkh', 'EMPTY', 'GuedKICl6', 'EMPTY', 'EMPTY', '2qqLvKvI9p', 'z63J1yVl'], ['87346', 'q', 'EMPTY', 'bB50QilPDY', 's465', 'mSFzy', 'L', 'UBVfZu', 'EMPTY', 'q', 'EMPTY', 'Toa7j', 'EMPTY', 'EMPTY', 'WF2hiGHyy', 'GuedKICl6', 'DiRO05Jo', 'EMPTY', 'EMPTY', 'bB50QilPDY', 'bB50QilPDY', 'e9HnvE', 'Toa7j', 'KmXQ', 'GsEAR61', 'P'], ['99583', 'kxVnBd', 'EMPTY', 'EMPTY', 'WF2hiGHyy', 'q4e9j3', 'GuedKICl6', 'z63J1yVl', 'z63J1yVl', 'EMPTY', 'EMPTY', 'qx3V87rxx4', 'EMPTY', 'di', 'f17xdvkp', 's465', 'DccoWGq0P', 'DccoWGq0P', 'KmXQ', '1', 'K9', 'EMPTY', 'KmXQ', 's465', 'GsEAR61', 'L'], ['85154', 'EMPTY', '2qqLvKvI9p', 'UBVfZu', 'di', 'q', 'EMPTY', 'di', 'EMPTY', 'DiRO05Jo', 's465', 'KcK', 'q', 's465', 'di', 'Vfg3XA', 'K9', 'EMPTY', 'bc60t', 'P', 'GsEAR61', 'q', 'e9HnvE', 'mSFzy', 'kxVnBd', 'e9HnvE'], ['99762', 'qx3V87rxx4', 'NPE4mO6Fr', 'DiRO05Jo', 'bB50QilPDY', 'bB50QilPDY', 'di', 'qx3V87rxx4', 'L', 'EMPTY', 'q', 'EMPTY', 'P', 'Vfg3XA', 'EMPTY', 'zthJCK9m', 'KcK', 'q4e9j3', 'WF2hiGHyy', 'EMPTY', 'EMPTY', 'GuedKICl6', 'UBVfZu', 'mSFzy', 'EMPTY', 'bc60t'], ['81022', 'EMPTY', 'Toa7j', 'qx3V87rxx4', 'EMPTY', 'EMPTY', '4eeL9', 's465', '1', 'bc60t', 'KmXQ', 'di', 'Vfg3XA', 's465', 'YDys', 'EMPTY', 'P', 'q4e9j3', 'Vfg3XA', '1', 'mSFzy', 'bB50QilPDY', 'bB50QilPDY', 'NPE4mO6Fr', 'Vfg3XA', 'Vfg3XA'], ['92023', 'Toa7j', 'NPE4mO6Fr', 'UBVfZu', 'EMPTY', 'L', 'EMPTY', 'zthJCK9m', 'e9HnvE', 'EMPTY', 'KmXQ', 'Toa7j', 'YDys', 'EMPTY', 'DccoWGq0P', 's465', 'f17xdvkp', 'ELFk03EQkh', 'NPE4mO6Fr', 'KmXQ', 's465', 'bc60t', 'EMPTY', 'zthJCK9m', 'qx3V87rxx4', 'mSFzy'], ['85066', '2qqLvKvI9p', 'ELFk03EQkh', 'EMPTY', 'DccoWGq0P', 'EMPTY', 'GuedKICl6', 'KmXQ', 'z63J1yVl', 'ELFk03EQkh', 'WF2hiGHyy', 'EMPTY', 'e9HnvE', 's465', 'EMPTY', 'Vfg3XA', 'z63J1yVl', 'EMPTY', 'GuedKICl6', '2qqLvKvI9p', 'ELFk03EQkh', 'kxVnBd', 'DiRO05Jo', 'P', 'EMPTY', 'KcK'], ['88173', 'EMPTY', 'L', 'EMPTY', 'q4e9j3', '4eeL9', 'kxVnBd', '2qqLvKvI9p', 'YDys', 'L', 'NPE4mO6Fr', 'bB50QilPDY', 'mSFzy', 'Vfg3XA', 'EMPTY', 'KmXQ', 'UBVfZu', 'YDys', 'EMPTY', 'UBVfZu', 'YDys', 'q4e9j3', 'EMPTY', 's465', '1', 'EMPTY'], ['88531', 'P', 'mSFzy', 'EMPTY', 'EMPTY', 'EMPTY', 'DiRO05Jo', 'Vfg3XA', 'q', 'UBVfZu', 'Vfg3XA', 'bB50QilPDY', 'q4e9j3', 'mSFzy', 'EMPTY', 'KmXQ', 'mSFzy', 'EMPTY', 'EMPTY', 'kxVnBd', 'Toa7j', 'bB50QilPDY', 'z63J1yVl', 'KmXQ', 'EMPTY', 'NPE4mO6Fr'], ['88289', 'bc60t', 'EMPTY', '1', 'EMPTY', 'Toa7j', 'EMPTY', '2qqLvKvI9p', 'qx3V87rxx4', 'EMPTY', 'KmXQ', 'GsEAR61', 'EMPTY', '2qqLvKvI9p', 'EMPTY', 'bB50QilPDY', 'di', 'L', 'z63J1yVl', 'EMPTY', 'GsEAR61', 'P', 'EMPTY', 'GsEAR61', 'GsEAR61', 'GsEAR61'], ['76596', 'mSFzy', 'kxVnBd', 'ELFk03EQkh', 'bc60t', 'WF2hiGHyy', 'KmXQ', 'K9', 'DccoWGq0P', 'qx3V87rxx4', 'q', 'di', 'EMPTY', 'EMPTY', 'DccoWGq0P', 'di', 'YDys', 'EMPTY', 'EMPTY', 'e9HnvE', 'EMPTY', 'EMPTY', 'P', 'KmXQ', 'K9', 'Vfg3XA'], ['97609', 'EMPTY', 'DiRO05Jo', 'YDys', 'e9HnvE', 'UBVfZu', 'KmXQ', '2qqLvKvI9p', 'GsEAR61', 'L', 'P', 'z63J1yVl', 'mSFzy', 's465', 's465', 'EMPTY', 'kxVnBd', 'EMPTY', 'P', 'Vfg3XA', 'f17xdvkp', '1', '4eeL9', 'L', 'qx3V87rxx4', 'EMPTY'], ['84965', 'q4e9j3', 'NPE4mO6Fr', 'KcK', 'GsEAR61', 'DccoWGq0P', 'WF2hiGHyy', 'GuedKICl6', 'f17xdvkp', 'f17xdvkp', 'DccoWGq0P', 'EMPTY', 'EMPTY', 'KmXQ', '4eeL9', 'EMPTY', '2qqLvKvI9p', 'P', 'bc60t', 'EMPTY', 'ELFk03EQkh', 'EMPTY', 'ELFk03EQkh', 'mSFzy', 'Vfg3XA', 'bB50QilPDY'], ['94501', 'UBVfZu', '4eeL9', 'DiRO05Jo', 'KcK', 'P', 'NPE4mO6Fr', 'e9HnvE', 'EMPTY', 'EMPTY', 'WF2hiGHyy', 'EMPTY', 'EMPTY', 'q4e9j3', 'YDys', 'EMPTY', 'ELFk03EQkh', 'e9HnvE', 'NPE4mO6Fr', 'EMPTY', 'zthJCK9m', 's465', 'zthJCK9m', 'K9', 's465', 'EMPTY'], ['89254', '1', 'q4e9j3', 'EMPTY', 'GsEAR61', 'EMPTY', 'GsEAR61', 'q', 'z63J1yVl', 'EMPTY', 'KcK', 'WF2hiGHyy', 'EMPTY', 'bB50QilPDY', 'WF2hiGHyy', 'qx3V87rxx4', 'e9HnvE', 'kxVnBd', 'bc60t', '4eeL9', 'EMPTY', 'EMPTY', 'EMPTY', 'KmXQ', 'q4e9j3', '2qqLvKvI9p'], ['94047', 's465', 'EMPTY', 'DccoWGq0P', 'DiRO05Jo', 's465', 'EMPTY', 'GuedKICl6', 'Toa7j', '1', '4eeL9', 'e9HnvE', 'EMPTY', 's465', 'GsEAR61', 's465', 'EMPTY', 'EMPTY', 'EMPTY', '2qqLvKvI9p', 'EMPTY', '4eeL9', 's465', 'EMPTY', 'zthJCK9m', '4eeL9'], ['86717', 'GsEAR61', 'EMPTY', 'EMPTY', 'DiRO05Jo', '4eeL9', 'EMPTY', 'EMPTY', 'GsEAR61', 'di', 'EMPTY', 'di', 'EMPTY', 'di', 'EMPTY', 'L', 'EMPTY', 'UBVfZu', 'zthJCK9m', 'Vfg3XA', 'e9HnvE', 'EMPTY', 'EMPTY', '1', 'GsEAR61', 'EMPTY'], ['77122', 'UBVfZu', 'zthJCK9m', 'DccoWGq0P', 'EMPTY', 'bB50QilPDY', 'kxVnBd', 'ELFk03EQkh', 'q4e9j3', '4eeL9', '1', 'qx3V87rxx4', 'GsEAR61', 'DccoWGq0P', 'q', 'z63J1yVl', 'f17xdvkp', 'EMPTY', 'bB50QilPDY', 'EMPTY', 'UBVfZu', 'EMPTY', 'bB50QilPDY', 'GuedKICl6', 'EMPTY', 'qx3V87rxx4'], ['89330', 'UBVfZu', '1', 'EMPTY', 'NPE4mO6Fr', 'ELFk03EQkh', 'GuedKICl6', 'q4e9j3', 'bB50QilPDY', 'EMPTY', 'EMPTY', 'zthJCK9m', 'EMPTY', 'EMPTY', 'Toa7j', 'ELFk03EQkh', 'GuedKICl6', 'Vfg3XA', 'EMPTY', 'e9HnvE', 'qx3V87rxx4', 'bc60t', 'EMPTY', 'ELFk03EQkh', 'P', 'EMPTY'], ['99742', 'f17xdvkp', 'ELFk03EQkh', 'NPE4mO6Fr', 'di', 'WF2hiGHyy', 'DiRO05Jo', 'EMPTY', 'q4e9j3', 'di', 'UBVfZu', 'f17xdvkp', 'P', 'EMPTY', 'bc60t', 'e9HnvE', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'mSFzy', 'UBVfZu', 'GsEAR61', 'GuedKICl6', 'EMPTY', '2qqLvKvI9p'], ['81600', 'KmXQ', 'KcK', 'zthJCK9m', 'EMPTY', 'EMPTY', 'P', 'z63J1yVl', 'zthJCK9m', 'EMPTY', '1', 'EMPTY', 'L', 'f17xdvkp', 'mSFzy', 'L', 'EMPTY', 'q', 'zthJCK9m', 'EMPTY', 'mSFzy', 'EMPTY', 'EMPTY', 'EMPTY', 'GuedKICl6', 'Vfg3XA'], ['85076', 'z63J1yVl', 'Toa7j', 'qx3V87rxx4', 'q', 's465', 'EMPTY', 'f17xdvkp', 'DiRO05Jo', '4eeL9', 'q', 'q', 'z63J1yVl', 's465', 'YDys', 'EMPTY', 'KcK', 'K9', 'KmXQ', 'P', 'bc60t', 'EMPTY', 'KmXQ', 'GuedKICl6', 'EMPTY', 'EMPTY'], ['85879', 'UBVfZu', 'z63J1yVl', 'bB50QilPDY', 'Vfg3XA', '4eeL9', 'f17xdvkp', 'Vfg3XA', 'NPE4mO6Fr', 'YDys', 'Vfg3XA', 'z63J1yVl', 'KcK', 'GuedKICl6', 'GsEAR61', 'EMPTY', 'mSFzy', 'ELFk03EQkh', 'qx3V87rxx4', 'EMPTY', 'DccoWGq0P', '4eeL9', 'EMPTY', 'YDys', 'L', 'EMPTY'], ['88778', '2qqLvKvI9p', 'EMPTY', 'K9', 'bB50QilPDY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'Toa7j', 'q4e9j3', 'f17xdvkp', 'EMPTY', 'qx3V87rxx4', 'L', 'EMPTY', 'P', 'bc60t', 'UBVfZu', 'EMPTY', 'WF2hiGHyy', 'q4e9j3', 's465', 'K9', 'KmXQ'], ['92793', 'q', 'Vfg3XA', 'bc60t', 'mSFzy', 'L', 'zthJCK9m', 'di', 'L', 'Vfg3XA', 'kxVnBd', 'GuedKICl6', 'EMPTY', 'EMPTY', 'P', 'EMPTY', 'K9', 'DccoWGq0P', 'GuedKICl6', 'EMPTY', 'q4e9j3', 'YDys', 'mSFzy', 'GuedKICl6', 'YDys', 'z63J1yVl'], ['95427', 'kxVnBd', '2qqLvKvI9p', 'YDys', 'mSFzy', 'Vfg3XA', 'EMPTY', 'z63J1yVl', 'L', 'WF2hiGHyy', 'EMPTY', 'L', 'kxVnBd', 'di', 'EMPTY', 'e9HnvE', 'EMPTY', 'KmXQ', 'EMPTY', 'DiRO05Jo', 'K9', 'z63J1yVl', 'KcK', 'ELFk03EQkh', 'bB50QilPDY', 'EMPTY'], ['94686', 'EMPTY', 'GsEAR61', 'DiRO05Jo', 'EMPTY', 'KmXQ', 'q', 'bB50QilPDY', 'P', 'UBVfZu', 'EMPTY', 'KmXQ', 'bB50QilPDY', 'GsEAR61', 'EMPTY', 'P', 'zthJCK9m', 'EMPTY', 'ELFk03EQkh', 'bB50QilPDY', 'P', '4eeL9', 'KmXQ', 'di', 'WF2hiGHyy', 'EMPTY'], ['96467', 'f17xdvkp', 'EMPTY', 'EMPTY', 'WF2hiGHyy', 'f17xdvkp', 'mSFzy', 'bc60t', 'bc60t', 'GuedKICl6', 'DiRO05Jo', 'DccoWGq0P', '1', 'WF2hiGHyy', 's465', 'K9', 'EMPTY', 'KcK', 'KmXQ', 'ELFk03EQkh', 'e9HnvE', 'Toa7j', 'EMPTY', 'kxVnBd', 'bc60t', 'zthJCK9m'], ['86626', 'Vfg3XA', 'EMPTY', 'bc60t', 'di', 'DiRO05Jo', 'qx3V87rxx4', 'P', 'DiRO05Jo', 'qx3V87rxx4', 'GsEAR61', 'KcK', 'kxVnBd', 'YDys', 'q', '2qqLvKvI9p', 'KcK', 'q4e9j3', '4eeL9', 'mSFzy', 'EMPTY', 's465', 'P', 'EMPTY', 'NPE4mO6Fr', 'q'], ['75739', 'GsEAR61', 'EMPTY', '4eeL9', 'bB50QilPDY', 'kxVnBd', 'P', 'GuedKICl6', 'EMPTY', 'K9', 'bc60t', 'GuedKICl6', 'EMPTY', 'YDys', 'GsEAR61', 'P', 'K9', 'EMPTY', 'z63J1yVl', 'DccoWGq0P', 'EMPTY', 'EMPTY', 'GsEAR61', 'Toa7j', 'EMPTY', 'DccoWGq0P'], ['93180', 'WF2hiGHyy', 'q4e9j3', '4eeL9', 'zthJCK9m', 'di', 'EMPTY', 'NPE4mO6Fr', 'EMPTY', 'f17xdvkp', 'UBVfZu', 'DccoWGq0P', 'GuedKICl6', 's465', 'EMPTY', 'zthJCK9m', 'DiRO05Jo', 'NPE4mO6Fr', 'zthJCK9m', 'f17xdvkp', 'YDys', 'EMPTY', 'YDys', 'DiRO05Jo', 'EMPTY', 'kxVnBd'], ['98571', 'YDys', 'P', 'EMPTY', 's465', 'Vfg3XA', 'EMPTY', 'EMPTY', 'bB50QilPDY', 'DiRO05Jo', 'L', 'UBVfZu', 'GuedKICl6', 'EMPTY', 'EMPTY', 'EMPTY', 'L', 'EMPTY', 'P', 's465', 'zthJCK9m', 'f17xdvkp', 'EMPTY', 'bc60t', 'EMPTY', 'WF2hiGHyy'], ['79207', 'EMPTY', 'zthJCK9m', 'EMPTY', 'KcK', 'EMPTY', 'EMPTY', 'EMPTY', 'qx3V87rxx4', 'EMPTY', 'WF2hiGHyy', 'WF2hiGHyy', 'ELFk03EQkh', 'f17xdvkp', 'EMPTY', 'KcK', 'Vfg3XA', 'EMPTY', 'Toa7j', 'UBVfZu', 'f17xdvkp', 'EMPTY', 'ELFk03EQkh', 'NPE4mO6Fr', 'EMPTY