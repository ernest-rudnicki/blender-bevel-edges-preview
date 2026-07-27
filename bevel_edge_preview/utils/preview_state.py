class PreviewState:
    _draw_handler = None
    _line_coordinates = []
    _is_active = False

    def __init__(
        self,
        draw_handler,
        line_coordinates,
    ):
        self._line_coordinates = line_coordinates
        self._draw_handler = draw_handler

    def set_draw_handler(self, draw_handler):
        self._draw_handler = draw_handler

    def set_line_coordinates(self, line_coordinates):
        self._line_coordinates = line_coordinates

    def get_draw_handler(self):
        return self._draw_handler

    def get_line_coordinates(self):
        return self._line_coordinates

    def set_is_active(self, is_active):
        self._is_active = is_active

    def get_is_active(self):
        return self._is_active

    def clear_state(self):
        self._draw_handler = None
        self._line_coordinates = []
        self._is_active = False


preview_state = PreviewState(None, [])
