with open("input_day2.txt", "r") as pwdlist:
    input = pwdlist.read().splitlines()

def checkPwd(input):
    counts = 0
    for allPwds in input:
        req, letter, pwd = allPwds.split()
        letter = letter.replace(':','')
        low, high = req.split('-')
        counting = pwd.count(letter)

        if counting in range(int(low), (int(high)+1)):
            counts += 1
    
    print(counts)

checkPwd(input)

