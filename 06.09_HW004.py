# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - 
# для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time

def random(max, min):
    t_data = '%.9F' % time.time()
    time.sleep(0.0001)
    interval = max - min
    razrad = len(str(interval)) * -1
    smech = int(t_data[razrad:])
    
    while smech > interval:
        smech = int(smech / 2)
        
    rnd = min + smech
    return rnd

print(random(99, 0))

