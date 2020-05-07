from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack =Stack("Middle")
right_stack = Stack("Right")
stacks.extend([left_stack, middle_stack, right_stack])
#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3 \n"))
for i in range(num_disks, 0, -1):
  left_stack.push(i)
  
num_optimal_moves =(2 ** num_disks) - 1
print("\n The fastest you can solve this game is in {} moves".format(num_optimal_moves))
#Get User Input
def get_input():
  choices = [(stack.get_name()[0]) for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name =stacks[i]. get_name()
      letter = choices[i]
      print("Enter {let} for {nam}".format(let=letter, nam=name))
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
#Play the Game
num_user_moves = 0
