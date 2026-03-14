# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class User(db.Model):

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)

    #__User_FIELDS__
    id_user = db.Column(db.Integer, nullable=True)
    username = db.Column(db.Text, nullable=True)
    hashed_password = db.Column(db.Text, nullable=True)

    #__User_FIELDS__END

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)


class Usuario(db.Model):

    __tablename__ = 'Usuario'

    id = db.Column(db.Integer, primary_key=True)

    #__Usuario_FIELDS__
    ape_usr = db.Column(db.Text, nullable=True)
    doc_usr = db.Column(db.Text, nullable=True)
    tel_usr = db.Column(db.Text, nullable=True)
    mov_usr = db.Column(db.Text, nullable=True)
    car_usr = db.Column(db.Text, nullable=True)
    fing_usr = db.Column(db.DateTime, default=db.func.current_timestamp())
    fret_usr = db.Column(db.DateTime, default=db.func.current_timestamp())
    nick_usr = db.Column(db.Text, nullable=True)
    clav_usr = db.Column(db.Text, nullable=True)
    fcla_usr = db.Column(db.DateTime, default=db.func.current_timestamp())
    dias_usr = db.Column(db.Integer, nullable=True)

    #__Usuario_FIELDS__END

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)


class Aseguradora(db.Model):

    __tablename__ = 'Aseguradora'

    id = db.Column(db.Integer, primary_key=True)

    #__Aseguradora_FIELDS__
    id_ase = db.Column(db.Integer, nullable=True)
    nom_ase = db.Column(db.Text, nullable=True)
    cod_ase = db.Column(db.Text, nullable=True)

    #__Aseguradora_FIELDS__END

    def __init__(self, **kwargs):
        super(Aseguradora, self).__init__(**kwargs)


class Auditoria_Sicov(db.Model):

    __tablename__ = 'Auditoria_Sicov'

    id = db.Column(db.Integer, primary_key=True)

    #__Auditoria_Sicov_FIELDS__
    id_revision = db.Column(db.Integer, nullable=True)
    serial_equipo_medicion = db.Column(db.Text, nullable=True)
    ip_equipo_medicion = db.Column(db.Text, nullable=True)
    fecha_registro_bd = db.Column(db.DateTime, default=db.func.current_timestamp())
    fecha_evento = db.Column(db.DateTime, default=db.func.current_timestamp())
    tipo_operacion = db.Column(db.Integer, nullable=True)
    tipo_evento = db.Column(db.Integer, nullable=True)
    codigo_proveedor = db.Column(db.Integer, nullable=True)
    id_runt_cda = db.Column(db.Integer, nullable=True)
    trama = db.Column(db.Text, nullable=True)
    identificacion_usuario = db.Column(db.Text, nullable=True)
    observacion = db.Column(db.Text, nullable=True)

    #__Auditoria_Sicov_FIELDS__END

    def __init__(self, **kwargs):
        super(Auditoria_Sicov, self).__init__(**kwargs)


class Carroceria(db.Model):

    __tablename__ = 'Carroceria'

    id = db.Column(db.Integer, primary_key=True)

    #__Carroceria_FIELDS__
    cod_car = db.Column(db.Text, nullable=True)
    nom_car = db.Column(db.Text, nullable=True)

    #__Carroceria_FIELDS__END

    def __init__(self, **kwargs):
        super(Carroceria, self).__init__(**kwargs)


class Cda(db.Model):

    __tablename__ = 'Cda'

    id = db.Column(db.Integer, primary_key=True)

    #__Cda_FIELDS__
    doc_cda = db.Column(db.Text, nullable=True)
    dir_cda = db.Column(db.Text, nullable=True)
    tel_cda = db.Column(db.Text, nullable=True)
    cer_cda = db.Column(db.Text, nullable=True)
    fexp_cda = db.Column(db.DateTime, default=db.func.current_timestamp())
    suc_cda = db.Column(db.String(255),  nullable=True)
    cla_cda = db.Column(db.String(255),  nullable=True)
    res_cda = db.Column(db.String(255),  nullable=True)
    rsa_cda = db.Column(db.String(255),  nullable=True)
    frs_cda = db.Column(db.DateTime, default=db.func.current_timestamp())
    eml_cda = db.Column(db.Text, nullable=True)
    cst_cda = db.Column(db.Text, nullable=True)

    #__Cda_FIELDS__END

    def __init__(self, **kwargs):
        super(Cda, self).__init__(**kwargs)


class Estado(db.Model):

    __tablename__ = 'Estado'

    id = db.Column(db.Integer, primary_key=True)

    #__Estado_FIELDS__
    nom_est = db.Column(db.String(255),  nullable=True)

    #__Estado_FIELDS__END

    def __init__(self, **kwargs):
        super(Estado, self).__init__(**kwargs)


class Nivel(db.Model):

    __tablename__ = 'Nivel'

    id = db.Column(db.Integer, primary_key=True)

    #__Nivel_FIELDS__
    id_niv = db.Column(db.Integer, nullable=True)
    nom_niv = db.Column(db.Text, nullable=True)

    #__Nivel_FIELDS__END

    def __init__(self, **kwargs):
        super(Nivel, self).__init__(**kwargs)


class Ciudad(db.Model):

    __tablename__ = 'Ciudad'

    id = db.Column(db.Integer, primary_key=True)

    #__Ciudad_FIELDS__
    id_ciu = db.Column(db.Integer, nullable=True)
    nom_ciu = db.Column(db.Text, nullable=True)
    cod_ciu = db.Column(db.String(255),  nullable=True)
    zon_ciu = db.Column(db.Text, nullable=True)

    #__Ciudad_FIELDS__END

    def __init__(self, **kwargs):
        super(Ciudad, self).__init__(**kwargs)


class Departamento(db.Model):

    __tablename__ = 'Departamento'

    id = db.Column(db.Integer, primary_key=True)

    #__Departamento_FIELDS__
    nom_dep = db.Column(db.Text, nullable=True)

    #__Departamento_FIELDS__END

    def __init__(self, **kwargs):
        super(Departamento, self).__init__(**kwargs)


class Pais(db.Model):

    __tablename__ = 'Pais'

    id = db.Column(db.Integer, primary_key=True)

    #__Pais_FIELDS__
    nom_pais = db.Column(db.Text, nullable=True)
    cod_pais = db.Column(db.String(255),  nullable=True)

    #__Pais_FIELDS__END

    def __init__(self, **kwargs):
        super(Pais, self).__init__(**kwargs)


class Clase(db.Model):

    __tablename__ = 'Clase'

    id = db.Column(db.Integer, primary_key=True)

    #__Clase_FIELDS__
    id_cla = db.Column(db.Integer, nullable=True)
    nom_cla = db.Column(db.Text, nullable=True)
    cod_cla = db.Column(db.Integer, nullable=True)

    #__Clase_FIELDS__END

    def __init__(self, **kwargs):
        super(Clase, self).__init__(**kwargs)


class Color(db.Model):

    __tablename__ = 'Color'

    id = db.Column(db.Integer, primary_key=True)

    #__Color_FIELDS__
    cod_col = db.Column(db.String(255),  nullable=True)

    #__Color_FIELDS__END

    def __init__(self, **kwargs):
        super(Color, self).__init__(**kwargs)


class Combustible(db.Model):

    __tablename__ = 'Combustible'

    id = db.Column(db.Integer, primary_key=True)

    #__Combustible_FIELDS__
    cod_com = db.Column(db.Integer, nullable=True)

    #__Combustible_FIELDS__END

    def __init__(self, **kwargs):
        super(Combustible, self).__init__(**kwargs)


class Condiciones(db.Model):

    __tablename__ = 'Condiciones'

    id = db.Column(db.Integer, primary_key=True)

    #__Condiciones_FIELDS__
    limpio = db.Column(db.Boolean, nullable=True)
    descargado = db.Column(db.Boolean, nullable=True)
    traccion = db.Column(db.Boolean, nullable=True)
    tapacubos = db.Column(db.Boolean, nullable=True)
    blindado = db.Column(db.Boolean, nullable=True)
    soporte = db.Column(db.Boolean, nullable=True)
    automatico = db.Column(db.Boolean, nullable=True)
    liquido_frenos = db.Column(db.Boolean, nullable=True)
    polarizado = db.Column(db.Boolean, nullable=True)
    tapa_combustible = db.Column(db.Boolean, nullable=True)
    alarma = db.Column(db.Boolean, nullable=True)
    id_condiciones = db.Column(db.Integer, nullable=True)

    #__Condiciones_FIELDS__END

    def __init__(self, **kwargs):
        super(Condiciones, self).__init__(**kwargs)


class Preinspeccion(db.Model):

    __tablename__ = 'Preinspeccion'

    id = db.Column(db.Integer, primary_key=True)

    #__Preinspeccion_FIELDS__
    id_ref = db.Column(db.Integer, nullable=True)
    observaciones = db.Column(db.Text, nullable=True)
    presion_ruedas = db.Column(db.Text, nullable=True)
    firma1 = db.Column(db.Text, nullable=True)
    firma2 = db.Column(db.Text, nullable=True)
    fecha_preinspeccion = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Preinspeccion_FIELDS__END

    def __init__(self, **kwargs):
        super(Preinspeccion, self).__init__(**kwargs)


class Vehiculo(db.Model):

    __tablename__ = 'Vehiculo'

    id = db.Column(db.Integer, primary_key=True)

    #__Vehiculo_FIELDS__
    id_veh = db.Column(db.Integer, nullable=True)
    placa = db.Column(db.Text, nullable=True)
    mod_veh = db.Column(db.Integer, nullable=True)
    cil_veh = db.Column(db.Integer, nullable=True)
    mot_veh = db.Column(db.Integer, nullable=True)
    vin_veh = db.Column(db.Text, nullable=True)
    eje_veh = db.Column(db.Integer, nullable=True)
    soa_veh = db.Column(db.Text, nullable=True)
    sexp_veh = db.Column(db.DateTime, default=db.func.current_timestamp())
    sven_veh = db.Column(db.DateTime, default=db.func.current_timestamp())
    lic_veh = db.Column(db.Text, nullable=True)
    pot_veh = db.Column(db.Integer, nullable=True)
    dia_veh = db.Column(db.Integer, nullable=True)
    lla_veh = db.Column(db.Text, nullable=True)
    kil_veh = db.Column(db.Integer, nullable=True)
    nsl_veh = db.Column(db.Integer, nullable=True)
    pol_veh = db.Column(db.Boolean, nullable=True)
    bli_veh = db.Column(db.Boolean, nullable=True)
    mat_veh = db.Column(db.DateTime, default=db.func.current_timestamp())
    cha_veh = db.Column(db.Text, nullable=True)
    gas_veh = db.Column(db.Text, nullable=True)
    vgs_veh = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Vehiculo_FIELDS__END

    def __init__(self, **kwargs):
        super(Vehiculo, self).__init__(**kwargs)


class Marca(db.Model):

    __tablename__ = 'Marca'

    id = db.Column(db.Integer, primary_key=True)

    #__Marca_FIELDS__
    id_mar = db.Column(db.Integer, nullable=True)
    nom_mar = db.Column(db.Text, nullable=True)
    cod_mar = db.Column(db.Text, nullable=True)

    #__Marca_FIELDS__END

    def __init__(self, **kwargs):
        super(Marca, self).__init__(**kwargs)


class Linea(db.Model):

    __tablename__ = 'Linea'

    id = db.Column(db.Integer, primary_key=True)

    #__Linea_FIELDS__
    id_lin = db.Column(db.Integer, nullable=True)
    nom_lin = db.Column(db.Text, nullable=True)
    cod_lin = db.Column(db.Text, nullable=True)

    #__Linea_FIELDS__END

    def __init__(self, **kwargs):
        super(Linea, self).__init__(**kwargs)


class Tp_Vehiculo(db.Model):

    __tablename__ = 'Tp_Vehiculo'

    id = db.Column(db.Integer, primary_key=True)

    #__Tp_Vehiculo_FIELDS__
    id_tveh = db.Column(db.Text, nullable=True)
    nom_tveh = db.Column(db.Text, nullable=True)

    #__Tp_Vehiculo_FIELDS__END

    def __init__(self, **kwargs):
        super(Tp_Vehiculo, self).__init__(**kwargs)


class Tp_Motor(db.Model):

    __tablename__ = 'Tp_Motor'

    id = db.Column(db.Integer, primary_key=True)

    #__Tp_Motor_FIELDS__
    nom_tpm = db.Column(db.Text, nullable=True)

    #__Tp_Motor_FIELDS__END

    def __init__(self, **kwargs):
        super(Tp_Motor, self).__init__(**kwargs)


class Servicio(db.Model):

    __tablename__ = 'Servicio'

    id = db.Column(db.Integer, primary_key=True)

    #__Servicio_FIELDS__
    inx_ser = db.Column(db.Integer, nullable=True)

    #__Servicio_FIELDS__END

    def __init__(self, **kwargs):
        super(Servicio, self).__init__(**kwargs)


class Referencia(db.Model):

    __tablename__ = 'Referencia'

    id = db.Column(db.Integer, primary_key=True)

    #__Referencia_FIELDS__
    val_ref = db.Column(db.Integer, nullable=True)

    #__Referencia_FIELDS__END

    def __init__(self, **kwargs):
        super(Referencia, self).__init__(**kwargs)



#__MODELS__END
