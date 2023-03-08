import string, random, base64
from datetime import datetime
import os, sys, platform, math, time
platform_uname = None
conda_flag = None
python_flag = None
cv2_flag = None
numpy_flag = None
matplotlib_flag = None
jupyter_flag = None
conda_env_name_flag = None
coppeliasim_remote_api_flag = None
settling_time = None
clientID = 0
left_motor_vel = 0
right_motor_vel = 0
file_name = 'task_2c_output.txt'

def random_string(length=10, char=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation):    return ''.join((random.choice(char) for x in range(length)))


def encode(str_input):
    str_output = base64.b64encode(str_input.encode('utf-8')).decode('utf-8')
    return str_output




output_file = open(file_name, 'w')
platform_uname = platform.uname().system
output_file.write(encode(random_string(6) + str(3746) + random_string(6)) + '\n')
output_file.write(encode(random_string(6) + "DB_3746" + random_string(6)) + '\n')
current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
output_file.write(encode(random_string(6) + current_time + random_string(6)) + '\n')
output_file.write(encode(random_string(6) + 'Recorded Total Mark is: ' + str(10) + random_string(6)))
output_file.close()
