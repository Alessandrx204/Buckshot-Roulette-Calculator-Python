from fractions import Fraction

# Initialize variables
cartidge = []  # List to store the cartridge
BLANK = 0  # Number of blanks
FULL = 0  # Number of full shots
tracker_is_running = True  # Flag to keep the loop running

# burner phone managed here below

#TODO 1: avoid burner_phone's 1 & 2 contradict burner phone's 3
#TODO 2: avoid burner_phone's 3 to set more BLANKS & FULL than available checking if []s in cartidge > BLANKS & FULLS then error
#TODO 3: if S contradict values update values accordingly making S useful to clear mistakes
#TODO 4: inverter

"""
Burner_Phone(cartidge, total_ammo, BLANK, FULL)

A function of curious purpose, simulating a 'Burner Phone' which offers cryptic insight
into the nature of an impending shot — blank or full.

The user is prompted to select a message type: a guaranteed blank, a full round, a custom
specification, or to cancel the operation altogether. Each choice must be confirmed by a
simple 'Y' or 'N' via the auxiliary function YN(), which ensures the user's conviction.

If confirmed, the function crafts a new cartridge array, marking a single chamber with
the foretold shot type. In cases of doubt or cancellation, it returns gracefully.

A modest yet clever mechanism for encoding premonitions into ammunition.

Usage:
    cartidge, updated = Burner_Phone(cartidge, total_ammo, BLANK, FULL)
"""
# ______________________________________________

def Burner_Phone(cartidge, total_ammo, BLANK, FULL):
    # Denwa = telephone in japanese (technically Keitai or Sumaho but you get the idea)
    denwa_num = 0
    denwa_val = 0

    # denwa_num: Stores the selected shot's index
    # denwa_val: Stores the shot type ('[B]' for Blank, '[F]' for Full)

    def YN():  # funzione per verificare se sei sicura la userò spesso
        cond = ''
        # Assegna a cond un valore nullo
        while cond not in ['Y', 'N']:
            cond = input('U sure?(y/n): ').upper()
            if cond not in ['Y', 'N']:
                print("Input non valido. Riprova.")

        return cond

    # YN works upon a simple concept: while our var 'cond' it's not to be found in the list ['Y','N'] ask an input which is either 'Y' or 'N' returns 'cond' and ends
    unsure = True  # variable for the burner phone menu name from the idea "unsure" abt teh msg until you saw it
    while unsure:
        try:
            print('What did the Burner Phone tell?')
            Phone_msg = int(input(
                "How unfortunate! Please choose:\n"
                " • [1] → Next is a blank round\n"
                " • [2] → Next is a live round\n"
                " • [3] → The ??? is a B/F *\n"
                " • [4] → Oh, nevermind, I misclicked\n"
                "Type here: "
            ))

            # piantala con gli OP ternari
            if Phone_msg in [1, 2]:  # how unfortunate
                responze = YN()
                unsure = False if responze == 'Y' else True
                denwa_num = 0
                denwa_val = '[B]' if Phone_msg == 1 else '[F]'

            elif Phone_msg == 3:  # custom
                responze = YN()
                unsure = False if responze == 'Y' else True

                while unsure == False:
                    try:
                        while True:
                            print("You must enter two values separated by ':' ")
                            denwa_num, denwa_val = input('which???(Nbr:B/F)').upper().split(':')
                            denwa_num = int(denwa_num) - 1
                            if denwa_num < 0 or denwa_num >= total_ammo:
                                print("Index out of range!")
                                continue
                            if cartidge[denwa_num] != '[X]':
                                print('invalid override')
                                continue

                            break #a
                        # Se l'input è valido, esci dal ciclo
                        print(denwa_num, denwa_val)
                        break
                    except ValueError:
                        print("Invalid format.You must enter two values separated by ':' ")


            elif Phone_msg == 4:
                responze = YN()
                unsure = False if responze == 'Y' else True
                pass  # ignora il messaggio

            else:
                continue



        except ValueError:
            continue

    if Phone_msg != 4:

        #cartidge = ['[X]' for _ in range(total_ammo)]
        cartidge[denwa_num] = f'[{denwa_val}]'


        return cartidge
    else:
        return Phone_msg


# ______________PROBABILITY_CHEQUE_____確率______

# Print the updated probability
def Kakuritsu(BLANK, FULL, total_ammo):
    print(f"Probability is {Fraction(BLANK, total_ammo)} blanks & {Fraction(FULL, total_ammo)}")
    print(f'% is {(BLANK / total_ammo) * 100:.3f}% a Blank & {(FULL / total_ammo) * 100:.3f}% a full Shot')


# DECIMAL ARE LIARS


# ______________________________________________
def main():
    # Declare variables as global so they can be modified inside the function
    global BLANK, FULL, cartidge, tracker_is_running

    tracker_is_running = True  # Start of the first part of the process

    # Main loop that runs while tracker_is_running is True
    while tracker_is_running:
        # Get input from the user for the number of blanks and full shots
        try:
            BLANK = int(input("insert number of Blanks: "))
            FULL = int(input("insert number of Full shots: "))
        except ValueError:
            print('Invalid input. Please entre integers only.')
            continue

        total_ammo = FULL + BLANK  # Total ammo is the sum of blanks and full shots

        # Print the number of bullets in the cartridge and the remaining blanks and fulls
        print(f"there are {total_ammo} bullets in this cartridge, {BLANK} blanks & {FULL} fulls left")

        # Represent the cartridge with '[X]' for each bullet
        # cartidge = '[X]' * total_ammo (old method tagg was a string not a list)
        cartidge = ['[X]' for i in range(total_ammo)]  # Creates cartridge we gonna use it all the programme long
        print(cartidge)

        # Print the probability of blanks and full shots remaining

        Kakuritsu(BLANK, FULL, total_ammo)
        print('確率')
        # End the loop after the first run
        tracker_is_running = False

    # Start second loop to check for any updates
    anyNEWS = True

    while anyNEWS:
        run_condition = input(f'any news?(y/n): ')
        # add condition no nevermind from Items()
        if run_condition == 'y':
            #  if AnyNews
            UPDATE = input('どのcontidion?(shot/soda[S] Burner Phone[R] OR else): ').strip().upper()
            # fine input UPDATE (UPDATE is Called so cuz it UPDATES the STATUS QUO)


            if UPDATE == 'R':
                cartidge = Burner_Phone(cartidge, total_ammo, BLANK, FULL)
                Kakuritsu(BLANK, FULL, total_ammo)
                print(cartidge)


            elif UPDATE == 'S':  # If S start Here

                Used_bullet = input('B/F?: ').upper()  # Ask if the used bullet is blank or full
                if Used_bullet == 'B':  # If blank is used
                    BLANK -= 1 if BLANK != 0 else BLANK


                elif Used_bullet == 'F':  # If full is used
                    FULL -= 1 if FULL != 0 else FULL
                # ifから出た
                # Calculate the new total_ammo
                total_ammo = BLANK + FULL

                # Print the updated status
                print(f"there are {total_ammo} bullets in this cartridge, {BLANK} blanks & {FULL} fulls left")

                # UPDATE the cartridge display
                # cartidge = '[X]' * total_ammo
                '''STAMP AMMO'''
                del cartidge[0]
                '''print(cartidge) if (BLANK != 0 and FULL != 0) else '[B]' * total_ammo if FULL == 0 else '[F]' * total_ammo'''
                if BLANK != 0 and FULL != 0:
                    #print(cartidge)
                    pass
                elif BLANK == 0 and FULL == 0:
                    print('this stupid programme took days show respect and donate pls(even a coffe)')
                    print('PS: Dont worry about the error, the programme is 終わった anyway (^ω^)7')
                    print('I reccomend to start a new instance sis')
                else:
                    if BLANK == 0:
                        cartidge = ['[F]'] * total_ammo
                    elif FULL == 0:
                        cartidge = ["[B]"] * total_ammo

                print(cartidge)





                '''

                # Print the updated probability
                print(f"Probability is {Fraction(BLANK, total_ammo)} blanks & {Fraction(FULL, total_ammo)}")
                print(f'% is {(BLANK/total_ammo)*100:.3f}% a Blank & {(FULL/total_ammo)*100:.3f}% a full Shot')
                # DECIMAL ARE LIARS
                '''
                Kakuritsu(BLANK, FULL, total_ammo)
            else:
                print('COMING IN NEXT VERSION')  # Placeholder for other updates
                '''こっちにアイテムのコードのすべてタイプするべきだ'''
        else:
            pass  # If no news, just つづく



if __name__ == '__main__':
    main()
