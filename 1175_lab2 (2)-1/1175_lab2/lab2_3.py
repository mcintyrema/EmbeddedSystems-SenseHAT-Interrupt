from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
orange = (255, 127, 0)
yellow =(255, 255, 0)
green = (0, 255, 0)
blue = (0,0,255)
indigo = (75, 0, 130)
white = (255, 255, 255)
black = (0,0,0)

x_left_count = 0
x_right_count = 0
y_down_count = 0
y_up_count = 0
#Task 3
while True:
	
	orientation = sense.get_orientation()
	acceleration = sense.get_accelerometer_raw()
	sense.clear()

	z = acceleration['z']
	z = round(z, 1)
	y = acceleration['y']
	y = round(y, 1)
	x = acceleration['x']
	x = round(x, 1)

	if z>0 and x==0 and y==0:
		image = [white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,
		white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,
		white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,
		white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white]
		sense.set_pixels(image)
	elif z>0:
	 if(abs(x)>abs(y)):
		 if x<0:
		   x_left_count = 0
		   y_down_count = 0
		   y_up_count = 0
		   if x_right_count==0:
			   for i in range(8):
				   sense.set_pixel(7, i, orange)
			   x_right_count = 1; 
		   elif x_right_count==1:
			   for i in range(8):
				   sense.set_pixel(6, i, indigo)
			   x_right_count = 2; 
		   elif x_right_count==2:
			   for i in range(8):
				   sense.set_pixel(5, i, yellow)
			   x_right_count = 3;    
		   elif x_right_count==3:
			   for i in range(8):
				   sense.set_pixel(4, i, white)
			   x_right_count = 4;     
		   elif x_right_count==4:
			   for i in range(8):
				   sense.set_pixel(3, i, black)
			   x_right_count = 5;    
		   elif x_right_count==5:
			   for i in range(8):
				   sense.set_pixel(2, i, green)
			   x_right_count = 6;  
		   elif x_right_count==6:
			   for i in range(8):
				   sense.set_pixel(1, i, blue)
			   x_right_count = 7;   
		   elif x_right_count==7:
			   for i in range(8):
				   sense.set_pixel(0, i, red)
			   x_right_count = 0; 			   
		 elif x>0:
			 x_right_count = 0
		   y_down_count = 0
		   y_up_count = 0
		   if x_left_count==0:
			   for i in range(8):
				   sense.set_pixel(0, i, orange)
			   x_left_count = 1
		   elif x_left_count==1:
			   for i in range(8):
				   sense.set_pixel(1, i, indigo)
			   x_left_count = 2
		   elif x_left_count==2:
			   for i in range(8):
				   sense.set_pixel(2, i, yellow)
			   x_left_count = 3
		   elif x_left_count==3:
			   for i in range(8):
				   sense.set_pixel(3, i, white)
			   x_left_count = 4
		   elif x_left_count==4:
			   for i in range(8):
				   sense.set_pixel(4, i, black)
			   x_left_count = 5    
		   elif x_left_count==5:
			   for i in range(8):
				   sense.set_pixel(5, i, green)
			   x_left_count = 6   
		   elif x_left_count==6:
			   for i in range(8):
				   sense.set_pixel(6, i, blue)
			   x_left_count = 7     
		   elif x_left_count==7:
			   for i in range(8):
				   sense.set_pixel(7, i, red)
			   x_left_count = 0
	 else:
		 if y<0:
		   x_right_count = 0
		   x_left_count = 0
		   y_up_count = 0
		   if y_down_count==0:
			   for i in range(8):
				   sense.set_pixel(i, 7, orange)
			   y_down_count = 1; 
		   elif y_down_count==1:
			   for i in range(8):
				   sense.set_pixel(i, 6, indigo)
			   y_down_count = 2; 
		   elif y_down_count==2:
			   for i in range(8):
				   sense.set_pixel(i, 5, yellow)
			   y_down_count = 3;   
		   elif y_down_count==3:
			   for i in range(8):
				   sense.set_pixel(i, 4, white)
			   y_down_count = 4;     
		   elif y_down_count==4:
			   for i in range(8):
				   sense.set_pixel(i, 3, black)
			   y_down_count = 5;    
		   elif y_down_count==5:
			   for i in range(8):
				   sense.set_pixel(i, 2, green)
			   y_down_count = 6;      
		   elif y_down_count==6:
			   for i in range(8):
				   sense.set_pixel(i, 1, blue)
			   y_down_count = 7;      
		   elif y_down_count==7:
			   for i in range(8):
				   sense.set_pixel(i, 0, red)
			   y_down_count = 0; 
		 if y>0:
		    x_right_count = 0
		   x_left_count = 0
		   y_down_count = 0
		   if y_up_count==0:
			   for i in range(8):
				   sense.set_pixel(i, 0, orange)
			   y_up_count = 1; 
		   elif y_up_count==1:
			   for i in range(8):
				   sense.set_pixel(i, 1, indigo)
			   y_up_count = 2; 
		   elif y_up_count==2:
			   for i in range(8):
				   sense.set_pixel(i, 2, yellow)
			   y_up_count = 3;   
		   elif y_up_count==3:
			   for i in range(8):
				   sense.set_pixel(i, 3, white)
			   y_up_count = 4;      
		   elif y_up_count==4:
			   for i in range(8):
				   sense.set_pixel(i, 4, black)
			   y_up_count = 5;     
		   elif y_up_count==5:
			   for i in range(8):
				   sense.set_pixel(i, 5, green)
			   y_up_count = 6;     
		   elif y_up_count==6:
			   for i in range(8):
				   sense.set_pixel(i, 6, blue)
			   y_up_count = 7;   
		   elif y_up_count==7:
			   for i in range(8):
				   sense.set_pixel(i, 7, red)
			   y_up_count = 0;  
	else: 
	 print("pi is down")
