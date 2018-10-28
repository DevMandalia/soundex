import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')
    f.initial_state = 'start'
    f.add_state('intial-zero')
    f.add_state('1-9')
    f.add_state('10-16')
    f.add_state('17')
    f.add_state('18')
    f.add_state('19')
    f.add_state('17a')
    f.add_state('18a')
    f.add_state('19a')
    f.add_state('ET')
    f.add_state('ET-UN')
    f.add_state('20-69')
    f.add_state('ET-7')
    f.add_state('ET-ON')
    f.add_state('70-79')
    f.add_state('77')
    f.add_state('78')
    f.add_state('79')
    f.add_state('77a')
    f.add_state('78a')
    f.add_state('79a')
    f.add_state('80-89')
    f.add_state('90-99')
    f.add_state('200-999')
    
    
    f.set_final('start')
    f.set_final('intial-zero')
    f.set_final('1-9')
    f.set_final('10-16')
    f.set_final('17a')
    f.set_final('18a')
    f.set_final('19a')
    f.set_final('20-69')
    f.set_final('ET-UN')
    f.set_final('70-79')
    f.set_final('ET-ON')
    f.set_final('77a')
    f.set_final('78a')
    f.set_final('79a')
    

    f.add_arc('start', 'intial-zero', '0', [])
    f.add_arc('intial-zero', '1-9', '0', [])
    
    # 0-9
    for ii in range(1,9):
      f.add_arc('1-9', '1-9', [str(ii)], [kFRENCH_TRANS[ii]])
    
    f.add_arc('1-9', '1-9', '0', [])

    #10 - 16
    
    f.add_arc('intial-zero', '10-16', '1', [])
    
    f.add_arc('10-16', '10-16', '0', [kFRENCH_TRANS[10]])
    
    f.add_arc('10-16', '10-16', '1', [kFRENCH_TRANS[11]])
    f.add_arc('10-16', '10-16', '2', [kFRENCH_TRANS[12]]) 
    f.add_arc('10-16', '10-16', '3', [kFRENCH_TRANS[13]])
    f.add_arc('10-16', '10-16', '4', [kFRENCH_TRANS[14]])
    f.add_arc('10-16', '10-16', '5', [kFRENCH_TRANS[15]])
    f.add_arc('10-16', '10-16', '6', [kFRENCH_TRANS[16]])
    
    # 17, 18, 19
    f.add_arc('10-16', '17', '7', [kFRENCH_TRANS[10]])
    f.add_arc('17', '17a', (), [kFRENCH_TRANS[7]])
    
    f.add_arc('10-16', '18', '8', [kFRENCH_TRANS[10]])
    f.add_arc('18', '18a', (), [kFRENCH_TRANS[8]])
    
    f.add_arc('10-16', '19', '9', [kFRENCH_TRANS[10]])
    f.add_arc('19', '19a', (), [kFRENCH_TRANS[9]])
    
    
    # 20 - 69
    
    f.add_arc('intial-zero', '20-69', '2', [kFRENCH_TRANS[20]])
    f.add_arc('intial-zero', '20-69', '3', [kFRENCH_TRANS[30]])
    f.add_arc('intial-zero', '20-69', '4', [kFRENCH_TRANS[40]])
    f.add_arc('intial-zero', '20-69', '5', [kFRENCH_TRANS[50]])
    f.add_arc('intial-zero', '20-69', '6', [kFRENCH_TRANS[60]])
  
    # 20, 30, 40, 50, 60
    f.add_arc('20-69', '20-69', '0', [])
    f.add_arc('20-69', '20-69', '0', [])
    f.add_arc('20-69', '20-69', '0', [])
    f.add_arc('20-69', '20-69', '0', [])
    f.add_arc('20-69', '20-69', '0', [])
    
    
    # 21, 31, 41, 51, 61
    f.add_arc('20-69', 'ET', '1', [kFRENCH_AND])
    f.add_arc('ET', 'ET-UN', (), [kFRENCH_TRANS[1]])
   
    
    # rest all in 20-69
    for i in range(2,9):
      f.add_arc('20-69', '20-69', [str(i)], [kFRENCH_TRANS[i]])
    
    
    # 70 - 79
    f.add_arc('intial-zero', '70-79', '7', [kFRENCH_TRANS[60]])
    
    #70, 72-76
    f.add_arc('70-79', '70-79', '0', [kFRENCH_TRANS[10]])
    f.add_arc('70-79', '70-79', '2', [kFRENCH_TRANS[12]])
    f.add_arc('70-79', '70-79', '3', [kFRENCH_TRANS[13]])
    f.add_arc('70-79', '70-79', '4', [kFRENCH_TRANS[14]])
    f.add_arc('70-79', '70-79', '5', [kFRENCH_TRANS[15]])
    f.add_arc('70-79', '70-79', '6', [kFRENCH_TRANS[16]])
    
    # 71
    f.add_arc('70-79', 'ET-7', '1', [kFRENCH_AND])
    f.add_arc('70-79', 'ET-ON', (), [kFRENCH_TRANS[11]])
    
    # 77, 78, 79
    f.add_arc('70-79', '77', '7', [kFRENCH_TRANS[10]])
    f.add_arc('77', '77a', (), [kFRENCH_TRANS[7]])
    
    f.add_arc('70-79', '78', '8', [kFRENCH_TRANS[10]])
    f.add_arc('78', '78a', (), [kFRENCH_TRANS[8]])
    
    f.add_arc('70-79', '79', '9', [kFRENCH_TRANS[10]])
    f.add_arc('79', '79a', (), [kFRENCH_TRANS[9]])
    
    
    # 80 - 89
    f.add_arc('intial-zero', '80-89', '8', [kFRENCH_TRANS[4]])
    f.add_arc('80-89', '1-9', (), [kFRENCH_TRANS[20]])

    # 90 - 99
    f.add_arc('intial-zero', '90-99', '9', [kFRENCH_TRANS[4]])
    f.add_arc('90-99', '10-16', (), [kFRENCH_TRANS[20]])
    
    # 100 - 199
    f.add_arc('start', 'intial-zero', '1', [kFRENCH_TRANS[100]])
    
    # 200 - 999
    for i in range(2, 9):
      f.add_arc('start', '200-999', str(i), [kFRENCH_TRANS[i]])
    
    f.add_arc('200-999', 'intial-zero', (), [kFRENCH_TRANS[100]])
    
    return f


if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))

