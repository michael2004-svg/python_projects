#! python3
# deletes files from the project folder using os module
import os
for quiznum in range(35):
    filepath1 = 'capitalquiz_answers%s.txt' % (quiznum+1)
    filepath2 = 'capitalsquiz%s.txt' %(quiznum+1)
    if os.path.isfile(filepath1):
       os.remove(filepath1)
       if os.path.isfile(filepath2):
          os.remove(filepath2)  
       print('file has been successfully removes')
    else:
        print('this file does not exists')
        