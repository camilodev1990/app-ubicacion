from django.db import models
import uuid

class Ubicacion(models.Model):
    
    DEPARTAMENTOS_COLOMBIA = [
        ('Amazonas', 'Amazonas'),
        ('Antioquia', 'Antioquia'),
        ('Arauca', 'Arauca'),
        ('Atlántico', 'Atlántico'),
        ('Bolívar', 'Bolívar'),
        ('Boyacá', 'Boyacá'),
        ('Caldas', 'Caldas'),
        ('Caquetá', 'Caquetá'),
        ('Casanare', 'Casanare'),
        ('Cauca', 'Cauca'),
        ('Cesar', 'Cesar'),
        ('Chocó', 'Chocó'),
        ('Córdoba', 'Córdoba'),
        ('Cundinamarca', 'Cundinamarca'),
        ('Guainía', 'Guainía'),
        ('Guaviare', 'Guaviare'),
        ('Huila', 'Huila'),
        ('La Guajira', 'La Guajira'),
        ('Magdalena', 'Magdalena'),
        ('Meta', 'Meta'),
        ('Nariño', 'Nariño'),
        ('Norte de Santander', 'Norte de Santander'),
        ('Putumayo', 'Putumayo'),
        ('Quindío', 'Quindío'),
        ('Risaralda', 'Risaralda'),
        ('San Andrés y Providencia', 'San Andrés y Providencia'),
        ('Santander', 'Santander'),
        ('Sucre', 'Sucre'),
        ('Tolima', 'Tolima'),
        ('Valle del Cauca', 'Valle del Cauca'),
        ('Vaupés', 'Vaupés'),
        ('Vichada', 'Vichada'),
    ]
    
    VIA = [
        ('Calle', 'Calle'),
        ('Carrera', 'Carrera'),
        ('Avenida', 'Avenida'),
        ('Transversal', 'Transversal'),
        ('Diagonal', 'Diagonal'),
        ('Glorieta', 'Glorieta'),
        ('Camino', 'Camino'),
    ]

    TIPO_UBICACION = [
        ('barrio', 'Barrio'),
        ('conjunto', 'Conjunto'),
        ('torre', 'Torre'),
        ('urbanizacion', 'Urbanización'),
        ('edificio', 'Edificio'),
        ('vereda', 'Vereda'),
        ('sector', 'Sector'),
        ('camino', 'Camino'),
        ('lote', 'Lote'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False, verbose_name="identificador")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")


    departamento = models.CharField(max_length=30, choices=DEPARTAMENTOS_COLOMBIA, default="Santander", verbose_name="Departamento")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    via = models.CharField(max_length=50, choices=VIA, default="calle", verbose_name="Vía")
    numero1 = models.CharField(max_length=100, verbose_name="Nombre o número de vía")
    numero2 = models.CharField(max_length=100, verbose_name="Nomenclatura")
    tipo_ubicacion = models.CharField(max_length=100, choices=TIPO_UBICACION, default="barrio", verbose_name="Tipo de ubicación")
    nombre_ubicacion = models.CharField(max_length=100, verbose_name="Nombre de ubicación")
    detalle_adicional = models.TextField(null=True, blank=True, verbose_name="Detalles adicionales")

    class Meta:
        db_table = "UBICACION"
        verbose_name = "Ubicacion"
        verbose_name_plural = "Ubicaciones"
        ordering = ["-fecha_creacion"]


    def __str__(self):
        partes = [
            f"{self.via} {self.numero1}",
            f"N° {self.numero2}" if self.numero2 else "",
            self.nombre_ubicacion,
            self.ciudad,
            self.departamento
        ]
        return ", ".join([p for p in partes if p])
    
    
    # ===========================================
    # METODOS DE UBICACION
    # ===========================================

    def mostrar_ubicacion(self):
        partes = [
            f"{self.via} {self.numero1}",
            f"N° {self.numero2}" if self.numero2 else "",
            self.nombre_ubicacion,
            self.ciudad,
            self.departamento
        ]
        return ", ".join([p for p in partes if p])



    def actualizar_direccion(self, departamento=None, ciudad=None, via=None, numero1=None,
                        numero2=None, tipo_ubicacion=None, nombre_ubicacion=None, detalle_adicional=None):
    
        campos_a_guardar = []

        if departamento:
            self.departamento = departamento
            campos_a_guardar.append('departamento')
        if ciudad:
            self.ciudad = ciudad
            campos_a_guardar.append('ciudad')
        if via:
            self.via = via
            campos_a_guardar.append('via')
        if numero1:
            self.numero1 = numero1
            campos_a_guardar.append('numero1')
        if numero2:
            self.numero2 = numero2
            campos_a_guardar.append('numero2')
        if tipo_ubicacion:
            self.tipo_ubicacion = tipo_ubicacion
            campos_a_guardar.append('tipo_ubicacion')
        if nombre_ubicacion:
            self.nombre_ubicacion = nombre_ubicacion
            campos_a_guardar.append('nombre_ubicacion')
        if detalle_adicional is not None:
            self.detalle_adicional = detalle_adicional
            campos_a_guardar.append('detalle_adicional')

        if campos_a_guardar:
            self.save(update_fields=campos_a_guardar)


