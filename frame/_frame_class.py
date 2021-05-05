class Frame:
    def __init__(self, time, size, pict_type, key_frame):
        self.time = time
        self.size = size
        self.pict_type = pict_type
        self.key_frame = key_frame

    @staticmethod
    def get_fields():
        return ['time', 'size', 'pict_type', 'key_frame']
