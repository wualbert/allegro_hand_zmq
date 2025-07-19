import json
import numpy as np
from typing import Optional, List, Tuple, Union
from dataclasses import dataclass, asdict

# Constants from BHand.h
NOF = 4  # number of fingers
NOJ = 4  # number of joints in each finger
TOTAL_JOINTS = NOF * NOJ  # 16 total joints

class AllegroMotionType:
    """Motion types for Allegro Hand as defined in BHand.h"""
    eMotionType_NONE = 0                # power off
    eMotionType_HOME = 1                # go to home position
    eMotionType_READY = 2               # finger position move motion (ready)
    eMotionType_GRAVITY_COMP = 3        # finger position move motion (gravity compensation)
    eMotionType_PRE_SHAPE = 4           # pre-shape motion
    eMotionType_GRASP_3 = 5             # grasping using 3 fingers
    eMotionType_GRASP_4 = 6             # grasping using 4 fingers
    eMotionType_PINCH_IT = 7            # pinching using index finger and thumb
    eMotionType_PINCH_MT = 8            # pinching using middle finger and thumb
    eMotionType_OBJECT_MOVING = 9       # object moving motion
    eMotionType_ENVELOP = 10            # enveloping grasp
    eMotionType_JOINT_PD = 11           # joint pd control
    eMotionType_MOVE_OBJ = 12           # object manipulation
    eMotionType_FINGERTIP_MOVING = 13   # fingertip moving control
    NUMBER_OF_MOTION_TYPE = 14          # total number of motion types

    # Motion type names for display
    MOTION_NAMES = {
        0: "NONE",
        1: "HOME",
        2: "READY",
        3: "GRAVITY_COMP",
        4: "PRE_SHAPE",
        5: "GRASP_3",
        6: "GRASP_4",
        7: "PINCH_IT",
        8: "PINCH_MT",
        9: "OBJECT_MOVING",
        10: "ENVELOP",
        11: "JOINT_PD",
        12: "MOVE_OBJ",
        13: "FINGERTIP_MOVING"
    }

    @classmethod
    def get_motion_name(cls, motion_type: int) -> str:
        """Get human-readable name for motion type"""
        return cls.MOTION_NAMES.get(motion_type, f"UNKNOWN_{motion_type}")

    @classmethod
    def is_valid_motion_type(cls, motion_type: int) -> bool:
        """Check if motion type is valid"""
        return 0 <= motion_type < cls.NUMBER_OF_MOTION_TYPE

class AllegroHandType:
    """Hand type enumeration"""
    LEFT = 0
    RIGHT = 1

@dataclass
class AllegroCommand:
    """Command structure for Allegro Hand"""
    def __init__(self, motion_type: int = AllegroMotionType.eMotionType_NONE, 
                 joint_positions: Optional[np.ndarray] = None,
                 desired_positions: Optional[np.ndarray] = None,
                 grasping_forces: Optional[np.ndarray] = None,
                 fingertip_positions: Optional[List[np.ndarray]] = None,
                 object_displacement: Optional[np.ndarray] = None,
                 time_interval: Optional[float] = None,
                 **kwargs):
        self.motion_type = motion_type
        self.joint_positions = joint_positions if joint_positions is not None else np.zeros(TOTAL_JOINTS)
        self.desired_positions = desired_positions if desired_positions is not None else np.zeros(TOTAL_JOINTS)
        self.grasping_forces = grasping_forces if grasping_forces is not None else np.zeros(NOF)
        self.fingertip_positions = fingertip_positions
        self.object_displacement = object_displacement
        self.time_interval = time_interval
        
        # Additional parameters
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, AllegroCommand):
            return False
        return (self.motion_type == other.motion_type and 
                np.array_equal(self.joint_positions, other.joint_positions))

    def validate(self) -> bool:
        """Validate command parameters"""
        if not AllegroMotionType.is_valid_motion_type(self.motion_type):
            return False
        
        if len(self.joint_positions) != TOTAL_JOINTS:
            return False
            
        if len(self.desired_positions) != TOTAL_JOINTS:
            return False
            
        if len(self.grasping_forces) != NOF:
            return False
            
        return True
