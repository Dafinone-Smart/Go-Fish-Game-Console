from random import shuffle


def deckOfCards():
    deck = []
    letterDeck = ["A", "J", "Q", "K"]

    for cards in range(len(letterDeck)):
        for x in range(2, 11):
            deck.append(str(x))
        for y in letterDeck:
            deck.append(y)

    shuffle(deck)
    return deck


class Players:

    def __init__(self, playernames):
        self.playernames = playernames

    # Share Cards to all Players
    def share_cards(self):
        self.firstPlayer = [CreateDeck.pop(), CreateDeck.pop(
        ), CreateDeck.pop(), CreateDeck.pop(), CreateDeck.pop()]
        self.secondPlayer = [CreateDeck.pop(), CreateDeck.pop(
        ), CreateDeck.pop(), CreateDeck.pop(), CreateDeck.pop()]
        self.thirdPlayer = [CreateDeck.pop(), CreateDeck.pop(
        ), CreateDeck.pop(), CreateDeck.pop(), CreateDeck.pop()]
        self.fourthPlayer = [CreateDeck.pop(), CreateDeck.pop(
        ), CreateDeck.pop(), CreateDeck.pop(), CreateDeck.pop()]
        return self.firstPlayer, self.secondPlayer, self.thirdPlayer, self.fourthPlayer

    # convert Player cards to List
    def player_card(self, playercode):
        self.playercode = playercode
        self.player_cards = [
            self.firstPlayer, self.secondPlayer, self.thirdPlayer, self.fourthPlayer]
        self.playerDetails = self.player_cards[self.playercode]
        return self.playerDetails

    # Get number of similar cards
    def scoreConfig(self, playerdetails):
        player_dict = {}
        self.playerDetails = playerdetails
        for cards in playerdetails:
            if cards in player_dict:
                player_dict[cards] += 1
            else:
                player_dict[cards] = 1
        return player_dict

    # Calculate players scores
    def calculate_win(self, player_name_list):
        player_score = {}
        self.player_name_list = player_name_list
        for names in player_name_list:
            if names in player_score:
                player_score[names] += 1
            else:
                player_score[names] = 1
        return player_score

    # Get similar cards upto 4
    def get_dict_repetition(self, dict_list):
        self.dict_list = dict_list
        dict_members = Players_List.scoreConfig(dict_list)
        final_list = []
        s = []
        dict_values = dict_members.values()
        real_list_values = list(dict_values)

        for count in dict_members:
            s.append(count)
        counter = 0
        for values in real_list_values:
            if values == 4:
                values_x = s[counter]
                final_list.append(values_x)
                final_list.append(values)
            counter += 1
        return final_list

    # Print information about game!
    def get_help(self):
        print("You have 52 cards in the deck to shuffle once the game starts." + "\n" +
              "Each player would be given 5 cards each at the start of the game." + "\n" +
              "There are 4 players in total for this game. The game would go clockwise " + "\n" +
              "and each players are meant to take turns to play. Once its your turn, " + "\n" +
              "you can ask any player for a card, if they do not have your requested card" + "\n" +
              "you have to pick a card from the deck of cards. If you pick the same card as" + "\n" +
              "what you requested, you have to keep picking another card from the deck and" + "\n" +
              "show the other players until you have a different card!. If the player has" + "\n" +
              "your requested card, you collect it and the game continues. Once you have" + "\n" +
              "4 of the same kind of card, you put them aside and continue the game. If the" + "\n" +
              "cards in the deck finishes, you continue the game until all players have no" + "\n" +
              "cards left. You get 1 point for each group of cards of same kind put aside." + "\n" +
              "\n"
              "The Player with the most points wins!")
        print("\n")
        print("\n")
        resume_game = input("Type  --resume  to go back to the game!- ")
        if resume_game == "--resume":
            return True
        else:
            return False

    # Request help
    def help_streak(self, playerrequest):
        self.playerrequest = playerrequest
        if self.playerrequest == "--help":
            if Players_List.get_help():
                player_request = input(
                    "Enter name of player or what you need here: ")
            else:
                get_response = input("Do you want to quit? (y/n): ")
                if get_response == "n":
                    player_request = input(
                        "Enter name of player or what you need here: ")
                else:
                    Players_List.quit_game()
        return player_request

    # Quit Game!
    def quit_game(self):
        print("Sorry to see you go!")
        exit()

    # Check if player has cards
    def check_if_player_has_cards(self, currentList, playername):
        self.currentList = currentList
        self.playername = playername
        if self.currentList == []:
            if len(CreateDeck) > 4:
                for new_cards in range(5):
                    self.currentList.append(CreateDeck.pop())
                    return True
            elif len(CreateDeck) > 0 and len(CreateDeck) < 5:
                deckLength = len(CreateDeck)
                for new_cards in range(deckLength):
                    self.currentList.append(CreateDeck.pop())
                    return True
            else:
                game_over.append(self.playername)
                print(game_over)
                return False

        return True

    # Check if player has 4 cards
    def has_four(self, player_List, position):
        self.player_list = player_List
        self.position = position
        hasFours = self.get_dict_repetition(self.player_list)
        if hasFours != []:
            hasFoursObj = hasFours[0]
            for el in self.player_list:
                if el == hasFoursObj:
                    self.player_list.remove(el)
                    if el in self.player_list:
                        self.player_list.remove(el)
            newPlayerName = get_player_name(self.position)
            playerNameStore.append(newPlayerName)
            print(playerNameStore)

    # Check if player has 4 cards
    def has_four_2(self, player_List, position, choice):
        self.playerlist = player_List
        self.position = position
        self.choice = choice
        hasFours = self.get_dict_repetition(self.playerlist)
        if hasFours != []:
            hasFoursObj = hasFours[0]
            # check number of repeated cards
            choice_count = 0
            for el in self.playerlist:
                if el == self.choice:
                    choice_count += 1
            if choice_count > 4:
                for el in range(4):
                    self.playerlist.remove(el)
            else:
                for el in self.playerlist:
                    if el == hasFoursObj:
                        self.playerlist.remove(el)
                        if el in self.playerlist:
                            self.playerlist.remove(el)
            newPlayerName = get_player_name(self.position)
            playerNameStore.append(newPlayerName)
            print(playerNameStore)

    # Continous Loop while card request is available from other players
    def continous_card_loop(self, x, counter, addition, choice, position):
        self.cardlist = x
        self.counter = counter
        self.addition = addition
        self.choice = choice
        self.position = position
        while self.counter > 0:
            if self.addition == self.choice:
                if CreateDeck == []:
                    break
                else:
                    self.addition = CreateDeck.pop()
                    if self.addition == self.choice:
                        self.cardlist.append(self.addition)
                        # Check if player has 4 same cards
                        self.has_four(self.cardlist, self.position)
                    else:
                        self.cardlist.append(self.addition)
                        # Check if player has 4 same cards
                        self.has_four(self.cardlist, self.position)
                        self.counter = 0
            else:
                self.counter = 0

    # def __str__(self):
    #     return ("Score: " + str(self.score) + "\n" + "Number of Similar Cards: " + str(self.countSimilarCards))


PlayerNames = []
game_over = []
playerNameStore = []


# get player position
def get_player_position(name):
    if name == PlayerNames[0]:
        Position = 0
    elif name == PlayerNames[1]:
        Position = 1
    elif name == PlayerNames[2]:
        Position = 2
    else:
        Position = 3
    return Position


# get player name
def get_player_name(position):
    if position == 0:
        playername = PlayerNames[0]
    elif position == 1:
        playername = PlayerNames[1]
    elif position == 2:
        playername = PlayerNames[2]
    else:
        playername = PlayerNames[3]
    return playername


# get player identification
def get_players_identification():
    for player in range(4):
        Player = input("Hi There! Please enter your name: ")
        PlayerNames.append(Player)


# Play game Loop
def play_game():
    counter = 0
    decider = 0
    if CreateDeck != []:
        for player in PlayerNames:
            # Check if player has cards
            check = Players_List.player_card(counter)
            if not Players_List.check_if_player_has_cards(check, player):
                print(f"Game over for {player}!")
                PlayerNames.remove(player)
                break

            print(player + " List: " + str(check))
            # Get info from player
            print(f"{player} its your Turn! Ask any player for a card!" + "\n")
            player_name = input(f"{player} enter name of player here: ")
            if player_name == "--help":
                player_name = Players_List.help_streak(player_name)

            choice = input(f"{player_name} I need: ")
            if choice == "--help":
                choice = Players_List.help_streak(choice)
            # Get player card List
            Position = get_player_position(player_name)
            x = Players_List.player_card(Position)

            # Check if player does not have card request
            if choice not in x:
                print(f"{player} Go Fish!")
                newPosition = get_player_position(player)
                newCounter = 0
                if CreateDeck == []:
                    break
                else:
                    addition = CreateDeck.pop()
                    # check if card picked from deck is same as card request
                    if addition == choice and newCounter == 0:
                        x = Players_List.player_card(newPosition)
                        x.append(addition)

                        # Check if player has 4 of same cards
                        Players_List.has_four(x, newPosition)

                        newCounter += 1
                        print(f"{player} picked {addition}")
                    else:
                        x = Players_List.player_card(newPosition)
                        x.append(addition)

                        # Check if player has 4 of same cards
                        Players_List.has_four(x, newPosition)

                    # Continue to loop till card picked from deck is different
                    Players_List.continous_card_loop(
                        x, newCounter, addition, choice, newPosition)

                    print(f"Deck: {CreateDeck}")
                    print(player + " List: " + str(check))

            x = Players_List.player_card(Position)
            if choice in x:
                xcount = 0
                for el in x:
                    if el == choice:
                        xcount += 1
                decider += 1
                y = Players_List.player_card(counter)
                for el in range(xcount):
                    y.append(choice)

                # Check if player has 4 same cards
                Players_List.has_four_2(y, counter, choice)

                for el in x:
                    if el == choice:
                        x.remove(choice)
                        if el in x:
                            x.remove(choice)

                print(f"Deck: {CreateDeck}")
                print(player + " List: " + str(check))

                """
                    Continue to loop while card requested from other player is gotten
                    Loop stops when other players do not have requested card!
                """
                while decider > 0:
                    # Check if player has any cards else game over for the player
                    check = Players_List.player_card(counter)
                    if not Players_List.check_if_player_has_cards(check, player):
                        print(f"Game over for {player}!")
                        PlayerNames.remove(player)
                        break
                    # Continue to pick until no player has your request
                    player_name = input(
                        f"{player} pick player again!:- ")

                    if player_name == "--help":
                        player_name = Players_List.help_streak(player_name)

                    choice = input(f"{player_name} I need: ")

                    if choice == "--help":
                        choice = Players_List.help_streak(choice)

                    Position = get_player_position(player_name)
                    x = Players_List.player_card(Position)

                    # Check if player has card request
                    if choice not in x:
                        print(f"{player} Go Fish!")
                        newPosition = get_player_position(player)
                        newCounter = 0
                        if CreateDeck == []:
                            break
                        else:
                            addition = CreateDeck.pop()
                            # Check if requested card is same as what is picked from deck
                            if addition == choice and newCounter == 0:
                                x = Players_List.player_card(newPosition)
                                x.append(addition)

                                # Check if player has 4 same cards
                                Players_List.has_four(x, newPosition)

                                newCounter += 1
                                print(f"{player} picked {addition}")
                            else:
                                x = Players_List.player_card(newPosition)
                                x.append(addition)

                                # Check if player has 4 same cards
                                Players_List.has_four(x, newPosition)

                            # Continue to loop till card picked from deck is different
                            Players_List.continous_card_loop(
                                x, newCounter, addition, choice, newPosition)

                        print(f"Deck: {CreateDeck}")
                        print(player + " List: " + str(check))
                        decider = 0
                    x = Players_List.player_card(Position)
                    if choice in x:
                        xcount = 0
                        for el in x:
                            if el == choice:
                                xcount += 1
                        decider += 1
                        y = Players_List.player_card(counter)
                        for el in range(xcount):
                            y.append(choice)

                        # Check if player has 4 same cards
                        Players_List.has_four_2(y, counter, choice)

                        for el in x:
                            if el == choice:
                                x.remove(choice)
                                if el in x:
                                    x.remove(choice)
                        print(f"Deck: {CreateDeck}")
                        print(player + " List: " + str(check))
            counter += 1
        counter = 0
    else:
        while len(PlayerNames) > 1:
            for player in PlayerNames:
                if player in game_over:
                    pass
                else:
                    # Check if player has any card
                    check = Players_List.player_card(counter)
                    if not Players_List.check_if_player_has_cards(check, player):
                        print(f"Game over for {player}!")
                        PlayerNames.remove(player)
                        break

                    print(player + " List: " + str(check))
                    # Get player card request
                    print(
                        f"{player} its your Turn! Ask any player for a card!" + "\n")
                    player_name = input(
                        f"{player} enter name of player here: ")

                    if player_name == "--help":
                        player_name = Players_List.help_streak(player_name)

                    choice = input(f"{player_name} I need: ")

                    if choice == "--help":
                        choice = Players_List.help_streak(choice)

                    Position = get_player_position(player_name)
                    x = Players_List.player_card(Position)

                    """
                        Check if player request has empty card list :
                            Game over for the player if list is empty
                    """
                    if x == []:
                        print(f"{player_name} game has ended!")
                        PlayerNames.remove(player_name)
                        break

                    # Check if player has card request
                    if choice not in x:
                        print(f"{player_name} does not have requested card!")
                        continue
                    if choice in x:
                        xcount = 0
                        for el in x:
                            if el == choice:
                                xcount += 1
                        decider += 1
                        y = Players_List.player_card(counter)
                        for el in range(xcount):
                            y.append(choice)

                        # Check if player has 4 same cards
                        Players_List.has_four_2(y, counter, choice)

                        # Check if current player has cards
                        if y == []:
                            print(f"{player_name} game has ended!")
                            PlayerNames.remove(player_name)
                            break

                        for el in x:
                            if el == choice:
                                x.remove(choice)
                                if el in x:
                                    x.remove(choice)

                        # Check if other player has cards
                        if x == []:
                            print(f"{player_name} game has ended!")
                            PlayerNames.remove(player_name)
                            break

                        print(player + " List: " + str(check))

                        """
                            Continous loop till player other players do not have requested cards
                                Loops end once request card is not available
                        """
                        while decider > 0:
                            # Continue to request for cards
                            player_name = input(
                                f"{player} pick player again!:- ")
                            if player_name == "--help":
                                player_name = Players_List.help_streak(
                                    player_name)

                            choice = input(f"{player_name} I need: ")

                            if choice == "--help":
                                choice = Players_List.help_streak(choice)

                            Position = get_player_position(player_name)
                            x = Players_List.player_card(Position)

                            # Check if player has card request
                            if choice not in x:
                                decider = 0
                            if choice in x:
                                xcount = 0
                                for el in x:
                                    if el == choice:
                                        xcount += 1
                                decider += 1
                                y = Players_List.player_card(counter)
                                for el in range(xcount):
                                    y.append(choice)

                                # Check if player has 4 same cards
                                Players_List.has_four_2(y, counter, choice)

                                # Check if current player has cards
                                if y == []:
                                    print(f"{player_name} game has ended!")
                                    PlayerNames.remove(player_name)
                                    break

                                for el in x:
                                    if el == choice:
                                        x.remove(choice)
                                        if el in x:
                                            x.remove(choice)

                                # Check if other player has cards
                                if x == []:
                                    print(f"{player_name} game has ended!")
                                    PlayerNames.remove(player_name)
                                    break

                                print(player + " List: " + str(check))
                # Continue to loop between players till players
                counter += 1
            counter = 0


# Create Deck!
CreateDeck = deckOfCards()
print(CreateDeck)
get_players_identification()
# Instantiate Player Class
Players_List = Players(PlayerNames)
# print(Players_List)
print(Players_List.playernames)
print("The game would go like so: \n" + Players_List.playernames[0] + " would go first\n" + Players_List.playernames[1] +
      " would go second\n" + Players_List.playernames[2] + " would go third\n" + Players_List.playernames[3] + " would go fourth!")


while (True):
    Players_List.share_cards()
    print(f"Deck: {CreateDeck}")
    # Continue to loop till more than 3 players have emptied their cards
    while len(PlayerNames) > 1:
        play_game()

    # Get winner!
    win_List = []
    win_dict = Players_List.calculate_win(playerNameStore)
    win_values = win_dict.values()
    real_win_values = list(win_values)

    counter = 0
    winner = 0
    for values in real_win_values:
        if values > winner:
            winner = values
        else:
            winner = winner
        counter += 1

    for members in win_dict:
        win_List.append(members)

    print("Winner of the game is: " +
          str(win_List[counter - 1]) + " with " + str(winner) + " points!")

    break
