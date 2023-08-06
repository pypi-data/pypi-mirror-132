""" This module implement tasks functionality  """
from superwise.controller.base import BaseController


class SegmentController(BaseController):
    """Class SegmentController - responsible for segment functionality"""

    def __init__(self, client, sw):
        """
        Constructor of SegmentController class
        :param client:
        :poram sw: superwise object

        """
        super().__init__(client, sw)
        self.path = "admin/v1/segments"
        self.model_name = "Segment"
