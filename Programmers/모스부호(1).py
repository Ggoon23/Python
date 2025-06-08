letter = ".... . .-.. .-.. ---"


def solution(letter):
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    m_index = []
    a = -1
    for i in letter :
        a += 1
        if i == " " :
            m_index.append(a)
    
    

    answer = ''
    return answer


print(solution(letter))