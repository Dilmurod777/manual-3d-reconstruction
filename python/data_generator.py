import cv2

cap = cv2.VideoCapture('./data/videos/bolt.mp4')

i, j = 0, 0
interval = 5

while True:
	if cap.grab():
		flag, frame = cap.retrieve()
		
		if not flag:
			continue
		else:
			if i % interval == 0:
				cv2.imwrite(f'./data/images/bolts/{j}.png', frame)
				j += 1
		i += 1
	else:
		break
	
	if cv2.waitKey(10) == 27:
		break
