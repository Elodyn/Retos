from enum import Enum
import keyboard
screen =[["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"]]

class Movement(Enum):
   DOWN = 1
   RIGHT = 2
   LEFT = 3
   ROTATE = 4
   
def move_pieces(screen: list, movement: Movement, rotation: int) -> (list, int):
   new_screen = [["🔲"]*10 for _ in range(10)]
   new_row_index = 0
   new_column_index = 0 

   rotation_item= 0
   rotations = [[(1,1),(0,0),(-2,0),(-1,-1)],
                [(0,1),(-1,0),(0,-1),(1,-2)],
                [(0,2),(1,1),(-1,1),(-2,0)],
                [(0,1),(1,0),(2,-1),(1,-2)]]
   new_rotation = rotation
   if movement is Movement.ROTATE:
      new_rotation = 0 if rotation == 3 else rotation + 1
   for row_index, index in enumerate(screen):
      for column_index, item in enumerate(index):

         if item == "🔳":
            match movement:
               case Movement.DOWN:
                  new_row_index = row_index +1
                  new_column_index = column_index
               case Movement.LEFT:
                  new_row_index = row_index
                  new_column_index = column_index -1
               case Movement.RIGHT:
                  new_row_index = row_index
                  new_column_index = column_index +1
               case Movement.ROTATE:
                  new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                  new_column_index = column_index + rotations[new_rotation][rotation_item][1]
                  rotation_item += 1

            if new_row_index > 9 or new_column_index > 9 or new_column_index < 0: 
               print("No se puede realizar el movimiento")
               return (screen, rotation)
            else:
               new_screen[new_row_index][new_column_index] = "🔳"
   
   print_screen(new_screen)
   return (new_screen, new_rotation)


def print_screen(screen: list):
   print("\nPantalla Tetris:\n")
   for row in screen:
      print("".join(map(str,row)))


def tetris():

   screen =[["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
            ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"]]
   
   rotation = 0

   while(True):
      event =keyboard.read_event()

      if event.name == "esc":
         break
      elif event.name == keyboard.KEY_DOWN:
         if event.name == "down":
            (screen,rotation) = move_pieces(screen,Movement.DOWN,rotation)
         elif event.name == "right":
            (screen,rotation) = move_pieces(screen,Movement.RIGHT,rotation)
         elif event.name == "left":
            (screen,rotation) = move_pieces(screen,Movement.LEFT,rotation)
         elif event.name == "space":
            (screen,rotation) = move_pieces(screen,Movement.ROTATE,rotation)

   print_screen(screen)
   

tetris()
