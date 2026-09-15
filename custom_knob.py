import math
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtWidgets import QAbstractSlider

class CustomKnob(QAbstractSlider):


    color = "#929292"

    def _init_(self, parent=None):
        super()._init_(parent)
        print ("hola")
        #self.setMinimum(0)
        #self.setMaximum(100)
        #self.setValue(35)  # Valor inicial
        #self.setFixedSize(150, 150)  # Tamaño por defecto del Knob
        #self.setCursor(Qt.PointingHandCursor)
        #self.setColor("#3282f6")


    def setKnobColor(self, color):
            self.color = color
            self.update()  # Redibuja el widget con el nuevo color




    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        #color = "#3282f6"
        width = self.width()
        height = self.height()
        size = min(width, height)
        pad = 10
        radius = (size - pad * 2) / 2
        center = QPointF(width / 2, height / 2)

        # 1. Mapeo del valor a ángulos (Estilo Qt Dial, de 135° a -270°)
        start_angle = 225
        total_angle = -270
        
        # Calcular porcentaje actual
        range_val = self.maximum() - self.minimum()
        factor = (self.value() - self.minimum()) / range_val if range_val != 0 else 0
        active_angle = factor * total_angle

        # 2. Dibujar la pista de fondo (Arco Gris Oscuro)
        pen_bg = QPen(QColor("#3d3d3d"), 12)
        pen_bg.setCapStyle(Qt.RoundCap)
        painter.setPen(pen_bg)
        # Qt mide en 1/16 de grado
        painter.drawArc(pad, pad, size - pad*2, size - pad*2, start_angle * 16, total_angle * 16)

        # 3. Dibujar la pista activa (Arco Naranja)
        #pen_active = QPen(QColor("#cc841c"), 12)
        pen_active = QPen(QColor(self.color), 12)
        pen_active.setCapStyle(Qt.RoundCap)
        painter.setPen(pen_active)
        painter.drawArc(pad, pad, size - pad*2, size - pad*2, start_angle * 16, active_angle * 16)

        # 4. Dibujar el cuerpo del Knob (Círculo Central)
        painter.setPen(Qt.NoPen)
        # Sombra sutil exterior
        painter.setBrush(QBrush(QColor("#1f1f1f")))
        knob_radius = radius - 10
        #painter.drawEllipse(center, knob_radius, knob_radius)
        # Centro
        painter.setBrush(QBrush(QColor("#2d2d2d")))
        #painter.drawEllipse(center, knob_radius - 2, knob_radius - 2)

        # 5. Dibujar la Línea Indicadora (Aguja Naranja)
        current_angle_rad = math.radians(start_angle + active_angle)
        # Coordenadas de inicio y fin de la aguja interior
        inner_r = knob_radius * 0.2
        outer_r = knob_radius * 0.8
        
        x1 = center.x() + inner_r * math.cos(current_angle_rad)
        y1 = center.y() - inner_r * math.sin(current_angle_rad)
        x2 = center.x() + outer_r * math.cos(current_angle_rad)
        y2 = center.y() - outer_r * math.sin(current_angle_rad)

        #pen_needle = QPen(QColor("#d49424"), 6)
        pen_needle = QPen(QColor(self.color), 6)
        pen_needle.setCapStyle(Qt.RoundCap)
        painter.setPen(pen_needle)
        painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

    # Habilitar arrastre e interactividad con el mouse
    def mouseMoveEvent(self, event):
        self.update_value_from_mouse(event.position())

    def mousePressEvent(self, event):
        self.update_value_from_mouse(event.position())

    def update_value_from_mouse(self, pos):
        # Calcular el ángulo en base a la posición del mouse
        dx = pos.x() - self.width() / 2
        dy = self.height() / 2 - pos.y()
        angle = math.degrees(math.atan2(dy, dx))
        
        if angle < 0:
            angle += 360

        # Normalizar para que encaje de 135° a -225° (315° en sentido horario)
        relative_angle = 225 - angle
        if relative_angle < 0:
            relative_angle += 360
            
        if relative_angle > 315:
            return  # Zona muerta del potenciómetro
            
        factor = relative_angle / 270
        factor = max(0.0, min(1.0, factor)) # Limitar entre 0 y 1
        

        new_value = self.minimum() + factor * (self.maximum() - self.minimum())
        self.setValue(int(new_value))
        self.update()

