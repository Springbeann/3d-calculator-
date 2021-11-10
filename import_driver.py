
import matplotlib.pyplot as plt 
import threed_project
import scatter3d
import contourplot
import import_handler
70
user_input = import_handler.askinput("Please enter (x,y,z)", 3)
try:
    threed_project.threedplot(int(user_input[0]), int(user_input[1]), int(user_input[2]))
    scatter3d.scatter(int(user_input[0]), int(user_input[1]), int(user_input[2]))
    user_input_2 = import_handler.askinput("Please enter (x,y,z)", 3)
    contourplot.contour(int(user_input[0]), int(user_input[1]), int(user_input[2]), int(user_input_2[0]), int(user_input_2[1]), int(user_input_2[2]))
except:
    print("Please provide three integer arguments (x,y,z)")
