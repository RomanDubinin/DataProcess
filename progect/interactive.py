import cv2
import sys
import numpy as np
import random

import Constants
import Helper

from Vector import Vector
from MovingProvider import MovingProvider
from Base import Base
from Enemy import Enemy

def move_enemy(enemy):
    random_vector = Helper.get_random_vector(0, 10)
    enemy_to_center_vector = base.position - enemy.position
    enemy_vector = enemy_to_center_vector / enemy_to_center_vector.length() * random_vector.length() + random_vector
    enemy.move_by(enemy_vector)

def close(enemy, moving_point):
    p = Vector(moving_point[0][0], moving_point[0][1]) - enemy.position
    return p.x < Constants.CONTOUR_EPS and p.y < Constants.CONTOUR_EPS


def get_not_killed_enemys(enemys, moving_points):
    return [enemy for enemy in enemys if all([not close(enemy, point) for point in moving_points])]

video_capture = cv2.VideoCapture(0)

ret, average_frame = video_capture.read()
average_frame = cv2.cvtColor(average_frame, cv2.COLOR_BGR2GRAY)
moving_provider = MovingProvider(average_frame)

HEIGTH, WIDTH = average_frame.shape
CENTER = Vector(WIDTH//2,HEIGTH//2)
base = Base(CENTER, CENTER, WIDTH//2, HEIGTH//2)

enemy_points = [Vector(0, 0), Vector(0, HEIGTH), Vector(WIDTH, 0), Vector(WIDTH, HEIGTH)]
enemys = []
for i in range(Constants.ENEMYS_NUM):
    enemys.append(Enemy(enemy_points[random.randint(0, len(enemy_points) - 1)]))


enemy = Enemy(Vector(0, 0))

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    contours = moving_provider.get_moved_contours(frame)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, Constants.CONTOUR_EPS,True)
        cv2.polylines(frame,approx,True,(0,255,255))
        enemys = get_not_killed_enemys(enemys, approx)


    base.move_by(Helper.get_random_vector(0, 10))
    cv2.circle(frame, (int(base.position.x), int(base.position.y)), 13, (255,0,0), thickness=-1)



    for enemy in enemys:
        move_enemy(enemy)
        cv2.circle(frame, (int(enemy.position.x), int(enemy.position.y)), 7, (0,0,255), thickness=-1)

    cv2.imshow('Video2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()