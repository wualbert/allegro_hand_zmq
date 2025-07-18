#
#   Allegro client in Python
#   Binds REP socket to tcp://*:5556
#
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from allegro_zmq.utils import zmq_utils

import numpy as np
import time
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

rock_q = np.array([	-0.1194, 1.2068, 1.0, 1.4042,
	-0.0093, 1.2481, 1.4073, 0.8163,
	0.1116, 1.2712, 1.3881, 1.0122,
	0.6017, 0.2976, 0.9034, 0.7929])
paper_q = np.array([
	-0.1220, 0.4, 0.6, -0.0769,
	0.0312, 0.4, 0.6, -0.0,
	0.1767, 0.4, 0.6, -0.0528,
	0.5284, 0.3693, 0.8977, 0.4863])
scissors_q = np.array([
	0.0885, 0.4, 0.6, -0.0704,
	0.0312, 0.4, 0.6, -0.0,
	0.1019, 1.2375, 1.1346,
	1.0244, 1.0, 0.6331, 1.3509, 1.0])


#  Do 10 requests, waiting each time for a response
for q in ([rock_q, paper_q, scissors_q]*3):
    q_str = zmq_utils.convert_allegro_q_to_zmq_str(q)
    print("Sending request %s " % q_str)
    socket.send_string(q_str)

    #  Get the reply.
    message = socket.recv_string()
    print("Received reply %s" % message)
    time.sleep(2)