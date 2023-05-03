# QUIZ and SCORING

pertanyaanDict = {
    'soal1' : {'pertanyaan' : 'What is the fastest land animal on Earth?',
               'jawaban' : 'A',
               'A' : 'Cheetah',
               'B' : 'Lion',
               'C' : 'Elephant',
               'D' : 'Hippopotamus'},
    'soal2' : {'pertanyaan' : 'Which bird is known for its long migration journeys, often spanning thousands of miles?',
               'jawaban' : 'C',
               'A' : 'Penguin',
               'B' : 'Hummingbird',
               'C' : 'Albatross',
               'D' : 'Ostrich',
               'E' : 'Cassowary'},
    'soal3' : {'pertanyaan' : 'Which mammal is known for its ability to glide from tree to tree using a membrane of skin stretched between its limbs?',
               'jawaban' : 'D',
               'A' : 'Tiger',
               'B' : 'Gorilla',
               'C' : 'Orangutan',
               'D' : 'Flying Squirell'}
}

jawabanUserList = []
userScore = 0

# QUIZ START!
print('\nSelamat datang dan selamat mengerjakan QUIZ!')

for questLoop , nomor in zip(pertanyaanDict , range(1,len(pertanyaanDict) + 1)):
    print(f"\n{nomor}. {pertanyaanDict[questLoop]['pertanyaan']}")
    for answerLoop in pertanyaanDict[questLoop] :
        if answerLoop == 'pertanyaan' or answerLoop == 'jawaban' :
            continue
        else :
            print(f"   {answerLoop}. {pertanyaanDict[questLoop][answerLoop]}")
    while True :
        jawabanInput = input('\nMasukan jawaban anda :').upper()
        if jawabanInput == '' :
            makeSure = input('\nApakah anda yakin ingin melewati? (Y/N) ').upper()
            if makeSure == 'Y' :
                jawabanUserList.append(jawabanInput)
                break
        elif jawabanInput.isalpha() and len(jawabanInput) == 1 and (jawabanInput in pertanyaanDict[questLoop]) :
            jawabanUserList.append(jawabanInput)
            break
        else :
            print('\nAyo! masukan jawaban sesuai pilihan ya..')

for jawabanUser , jawabanDict in zip(jawabanUserList , pertanyaanDict):
    if jawabanUser == pertanyaanDict[jawabanDict]['jawaban'] :
        userScore += 1

userScoreTemp = (userScore / len(pertanyaanDict)) * 100
userScoreFinal = str(round((int(userScoreTemp) if userScoreTemp.is_integer() else userScoreTemp),1)) + '%'

print(f'\nAnda benar : {userScoreFinal}\n')

for jawabanUser , jawabanDict in zip(jawabanUserList , pertanyaanDict):
    if jawabanUser != pertanyaanDict[jawabanDict]['jawaban'] :
        print(f'Anda salah menebak soal nomor {jawabanDict[-1]}\nJawaban anda {jawabanUser}\nJawaban seharusnya {pertanyaanDict[jawabanDict]["jawaban"]}')