#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random 
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
#generate 35 quiz files
for quiznum in range(35):
    #create the quiz and answer key files
    quizfile = open('capitalsquiz%s.txt' %(quiznum+1), 'w')
    answerkeyfile = open('capitalquiz_answers%s.txt' % (quiznum+1),'w')
    #write out the header for the quiz
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((''*20 )+'state capital quiz(form%s)' %(quiznum+1) )
    quizfile.write('\n\n')
    #shuffle the order of the states
    states =list(capitals.keys())
    random.shuffle(states)
    #loop through all 50 states making a question for each

    for questionnum in range(50):
         #get right and wrong answers
        correctanswer =capitals[states[questionnum]]
        wronganswer = list(capitals.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wronganswer = random.sample(wronganswer, 3)
        answeroption = wronganswer + [correctanswer]
        random.shuffle(answeroption)
    
    # Write the question and the answer options to the quiz file.
        quizfile.write('%s. What is the capital of %s?\n' % (questionnum + 1,states[questionnum]))
        for i in range(4):
             quizfile.write(' %s. %s\n' % ('ABCD'[i], answeroption[i]))
        quizfile.write('\n')
        # Write the answer key to a file.
        answerkeyfile.write('%s. %s\n' % (questionnum + 1, 'ABCD'[answeroption.index(correctanswer)]))
        print('hello at' , quiznum , 'youu' , questionnum)
    quizfile.close()
    answerkeyfile.close()