# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def come():
    agent.teleport_to_player()

player.on_chat("come", come)

def move_fw(step):
    agent.move(FORWARD, step)

player.on_chat("fw", move_fw)
def move_bk(step):
    agent.move(BACK, step)

player.on_chat("bk", move_bk)
def move_up(step):
    agent.move(UP, step)

player.on_chat("up", move_up)
def move_down(step):
    agent.move(DOWN, step)

player.on_chat("down", move_down)
def turn_left():
    agent.turn(TurnDirection.LEFT)

player.on_chat("tl", turn_left)
def turn_right():
    agent.turn(TurnDirection.RIGHT)

player.on_chat("tr", turn_right)

def ch1():
    agent.move(FORWARD,4)
    agent.turn(TurnDirection.LEFT)
    agent.move(FORWARD, 4)
    agent.turn(TurnDirection.RIGHT)
    agent.move(FORWARD, 3)
    
    for i in range(3):
            agent.move(UP, 1)
            agent.move(FORWARD, 1)
    agent.move(FORWARD,1)
    for i in range(3):
            agent.move(FORWARD, 1)
            agent.move(DOWN, 1)
   

player.on_chat("ch1", ch1)

def ch2():
    for i in range(3):
        agent.move(UP, 1)
        agent.move(FORWARD, 1)

player.on_chat("ch2", ch2)
def ch3():
    for i in range(3):
        agent.move(FORWARD, 1)
        agent.move(DOWN, 1)

player.on_chat("ch3", ch3)






