import string
from tabulate import tabulate
from termcolor import colored

ALPHABET = list(string.ascii_uppercase)
FREQUENCIES = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28,
    'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61,
    'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11,
    'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
}
INPUT_STRING = '''NG T OTF gvtisf 4,000 fvtip tjn, xg t wnrg htssvo Zvgvw Lqdcdaniovixgj wqv wqxg ixaang nc wqv
Gxsv, t ztpwvi phixav plvwhqvo ndw wqvqxvinjsfuqp wqtw wnso wqv pwnif nc qxp snio'p sxcv—
tgo xg pn onxgj qvnuvgvo wqv ivhniovo qxpwnif nc hifuwnsnjf. Qxp rtp gnw t pfpwvz nc
pvhivwrixwxgj tp wqv znovig rniso lgnrp xw; qv dpvo gn cdssf ovkvsnuvo hnov nc
qxvinjsfuqxhpfzans pdapwxwdwxngp. Qxp xgphixuwxng, htikvo tandw 1900 A.H. xgwn wqvsxkxgj
inhl xg wqv ztxg hqtzavi nc wqv wnza nc wqv gnasvztgLqgdzqnwvu XX, zvivsf dpvp pnzv dgdpdts
qxvinjsfuqxh pfzansp qvivtgo wqviv xg usthv nc wqv zniv nioxgtif ngvp. Znpw nhhdi xg wqv stpw
20hnsdzgp nc wqv xgphixuwxng'p 222, xg t pvhwxng ivhnioxgj wqv zngdzvgwpwqtw Lqgdzqnwvu
qto vivhwvo xg wqv pvikxhv nc wqv uqtitnq TzvgvzqvwXX. Wqv xgwvgwxng rtp gnw wn ztlv xw
qtio wn ivto wqv wvyw. Xw rtp wnxzutiw t oxjgxwf tgo tdwqnixwf wn xw, uviqtup xg wqv ptzv rtf
wqtw tjnkvigzvgw uinhstztwxng rxss puvss ndw "Xg wqv fvti nc Ndi Snio Ngvwqndptgo vxjqw
qdgoivo tgo pxywf wqivv" xgpwvto nc edpw rixwxgj "1863."Wqv tgngfzndp phixav ztf tspn qtkv
avvg ovzngpwitwxgj qxp lgnrsvojvcni unpwvixwf. Wqdp wqv xgphixuwxng rtp gnw pvhivw
rixwxgj, adw xwxghniunitwvo ngv nc wqv vppvgwxts vsvzvgwp nc hifuwnjituqf: t
ovsxavitwvwitgpcniztwxng nc wqv rixwxgj. Xw xp wqv nsovpw wvyw lgnrg wn on pn.Wqv
witgpcniztwxngp nhhdi xg cdgvitif cnizdstp, xg t qfzg wn Wqnwq,xg t hqtuwvi nc wqv Annl nc wqv
Ovto, ng wqv ptihnuqtjdp nc wqv uqtitnqPvwx X, xg infts wxwsvp oxpustfvo xg Sdyni, ng wqv
tihqxwitkv nc wqv Wvzusv nc Sdyni, ng pwvsv, xgstdotwnif axnjituqxh xgphixuwxngp. Wqviv xp
gnwqxgj zvtgw wn avhnghvtsvo xg tss wqxp; xgovvo, ztgf nc wqv pwtwvzvgwp tiv ivuvtwvo
xgnioxgtif cniz ixjqw gvyw wn wqv tswvivo ngvp. Rqf, wqvg, wqvwitgpcniztwxngp? Pnzvwxzvp
cni vppvgwxtssf wqv ptzv ivtpng tp xgLqgdzqnwvu'p wnza: wn xzuivpp wqv ivtovi. Nhhtpxngtssf
cni thtssxjituqxh ni ovhnitwxkv vccvhw; itivsf, wn xgoxhtwv t hngwvzunitifuingdghxtwxng; uviqtup
vkvg cni t ovsxavitwv tihqtxpz tp t ivthwxngtjtxgpw cnivxjg xgcsdvghv.Adw ztgf xgphixuwxngp tiv
wxghwdivo, cni wqv cxipw wxzv, rxwq wqvpvhngo vppvgwxts cni hifuwnsnjf—pvhivhf. Xg t cvr
htpvp, wqv pvhivhf rtpxgwvgovo wn xghivtpv wqv zfpwvif tgo qvghv wqv tihtgv ztjxhts unrvip
nchviwtxg ivsxjxndp wvywp. Adw wqv pvhivhf xg ztgf zniv htpvp ivpdswvo cinzwqv
dgovipwtgotasv ovpxiv nc wqv Vjfuwxtgp wn qtkv utppvipaf ivto wqvxivuxwtuqp tgo pn hngcvi
dung wqv ovutiwvo wqv asvppxgjp rixwwvg wqvivxg.Xg Vjfuw, rxwq xwp hnghvgwitwxng dung
wqv tcwvisxcv, wqv gdzavi nc wqvpvxgphixuwxngp pnng • uinsxcvitwvo wn pdhq tg vywvgw wqtw
wqv twwvgwxng tgowqv jnnorxss nc kxpxwnip cstjjvo. Wn ivkxkv wqvxi xgwvivpw, wqv
phixavpovsxavitwvsf ztov wqv xgphixuwxngp t axw naphdiv. Wqvf xgwinodhvo wqvhifuwnjituqxh
pxjgp wn htwhq wqv ivtovi'p vfv, ztlv qxz rngovi, tgowvzuw qxz xgwn dgixoosxgj wqvz — tgo pn
xgwn ivtoxgj wqv asvppxgjp. Xwrtp t pniw nc Ztoxpng Tkvgdv wvhqgxbdv xg wqv Ktssvf nc wqv
Lxgjp. Adwwqv wvhqgxbdv ctxsvo dwwvisf. Xgpwvto nc xgwvivpwxgj wqv ivtovip, xwvkxovgwsf
ovpwinfvo vkvg wqv psxjqwvpw ovpxiv wn ivto wqv vuxwtuqp, cnipnng tcwvi wqv cdgvitif
hifuwnjituqf rtp avjdg, xw rtp tatgongvo.
'''

cipher_key = {letter: None for letter in ALPHABET}
v1_cipher_key = {
    'V': 'e', 'T': 'a', 'W': 't', 'Q': 'h', 'N': 'o', 'G': 'n',
    'C': 'f', 'I': 'r', 'S': 'l', 'F': 'y', 'O': 'd', 'P': 's',
    'J': 'g', 'X': 'i', 'R': 'w', 'H': 'c', 'A': 'b', 'U': 'p',
    'D': 'u', 'Z': 'm', 'L': 'k', 'K': 'v', 'Y': 'x', 'B': 'q',
    'E': 'j'
}

def calculate_frequencies(s):
    freq = {letter: 0 for letter in string.ascii_uppercase}

    for i in s.upper():
        if i in ALPHABET:
            freq[i] += 1

    return freq

def build_table(frequencies, title):
    sorted_freq = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    table = [[letter, freq] for letter, freq in sorted_freq]
    return tabulate(table, headers=[title, "Frequency"], tablefmt="pretty").split("\n")

def side_by_side_tables(table1, table2):
    combined = []
    max_len = max(len(table1), len(table2))
    for i in range(max_len):
        line1 = table1[i] if i < len(table1) else " " * len(table1[0])
        line2 = table2[i] if i < len(table2) else " " * len(table2[0])
        combined.append(f"{line1}   {line2}")
    return "\n".join(combined)

def substitute_letters(sub, sub_with, s):
    s_list = list(s)

    for i in range(len(s_list)):
        if s_list[i] == sub:
            s_list[i] = sub_with

    return ''.join(s_list)

def colorize_lowercase(text):
    colored_text = ""
    color = "green"
    for char in text:
        if char.islower():
            colored_text += colored(char, color)
        else:
            colored_text += char
    return colored_text

def update_cipher_key(sub, sub_with):
    cipher_key[sub] = sub_with

def reset_cipher_key():
    for letter in cipher_key:
        cipher_key[letter] = None

def print_cipher_key():
    key_table = [[cipher_letter, cipher_key[cipher_letter] if cipher_key[cipher_letter] else '-'] for cipher_letter in ALPHABET]
    print(tabulate(key_table, headers=["Cipher Letter", "Mapped To"], tablefmt="pretty"))

def apply_cipher_key():
    s_list = list(INPUT_STRING.upper())
    for i in range(len(s_list)):
        if s_list[i] in v1_cipher_key:
            update_cipher_key(s_list[i], v1_cipher_key[s_list[i]])
            s_list[i] = v1_cipher_key[s_list[i]]
    return ''.join(s_list)

def main():
    message_frequencies = calculate_frequencies(INPUT_STRING)
    english_table = build_table(FREQUENCIES, "English Letter")
    message_table = build_table(message_frequencies, "Message Letter")
    tables = side_by_side_tables(english_table, message_table)
    s = INPUT_STRING.upper()

    print("Letter Frequency Comparison:\n")
    print(tables)
    print(f"\nInput string:\n\n{s}\n")
    while True:
        print("\nSelect an option:")
        print("1: Print frequencies")
        print("2: Print cypher string")
        print("3: Substitute a letter in the cypher")
        print("4: Print the key table")
        print("5: Decipher Variant 1")
        print("r: Reset")
        print("q: Quit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == 'q':
            print("Exiting program.")
            break
        elif choice == '1':
            print("Letter Frequency Comparison:\n")
            print(tables)
        elif choice == '2':
            print(f"\nInput string:\n\n{colorize_lowercase(s)}\n")
        elif choice == '3':
            a = input("Type the letter in the string to substitute: ").strip().upper()
            b = input("Type the letter to substitute with: ").strip().lower()
            s = substitute_letters(a, b, s)
            update_cipher_key(a, b)
            print(f"\nLetter '{a}' was substituted with '{b}' in the cypher string!\n")
        elif choice == '4':
            print("\nCurrent Cipher Key Table:\n")
            print_cipher_key()
        elif choice == '5':
            s = apply_cipher_key()
            print("\nVariant 1 string was decyphered with a known cypher key!\n")
        elif choice == 'r':
            s = INPUT_STRING.upper()
            reset_cipher_key()
            print("\nThe cypher string and key table were reset to initial state!\n")

if __name__ == "__main__":
    main()
