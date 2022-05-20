## Prueba técnica Desarrollador Back-end [Solenium](https://solenium.co)

En este repositorio encontrarás una aplicación básica desarrollada en Django con una base de datos sqlite cuyo propósito es almacenar información de mediciones de variables eléctricas tomadas por unos medidores de energía, y permitir que la información sea procesada y consultada a través de API's.

Se requiere desarrollar:
* Una API que permita consultar las mediciones eléctricas de un medidor de energía en particular, entre dos fechas determinadas. Por ejemplo, al hacer un `GET` a un endpoint como `/api/measurements?meter=1&datetime_from=2022-05-11 14:00-05:00&datetime_to=2022-05-11 14:30-05:00` se debería debe devolver en formato JSON las mediciones de energía del medidor con id `1` que se hayan tomado el 11 de mayo de 2022 entre las 2:00 p.m. y las 2:30 p.m. Ejemplo de salida:
```
[
    {
        "date_time":"2022-05-12T14:01:04-05:00",
        "voltage":119.2,
        "current":1.73,
        "active_power":121.89,
        "reactive_power":160.04
    },
    {
        "date_time":"2022-05-12T14:01:44-05:00",
        "voltage":119.1,
        "current":1.73,
        "active_power":121.3,
        "reactive_power":160.04
    },
    {
        "date_time":"2022-05-12T14:02:04-05:00",
        "voltage":119.2,
        "current":1.73,
        "active_power":121.3,
        "reactive_power":160.04
    },
    {
        "date_time":"2022-05-12T14:02:44-05:00",
        "voltage":119.3,
        "current":1.73,
        "active_power":121.89,
        "reactive_power":160.64
    },
    {
        "date_time":"2022-05-12T14:03:04-05:00",
        "voltage":119.4,
        "current":1.73,
        "active_power":121.3,
        "reactive_power":161.23
    },
    {
        "date_time":"2022-05-12T14:03:46-05:00",
        "voltage":119.4,
        "current":1.73,
        "active_power":120.7,
        "reactive_power":160.64
    },
    {
        "date_time":"2022-05-12T14:04:04-05:00",
        "voltage":119.4,
        "current":1.73,
        "active_power":120.7,
        "reactive_power":160.64
    }
]
```


* (Opcional) Una API que permita conocer cuál fue la potencia máxima registrada por un medidor en particular en cada una de las horas del día, para una fecha determinada. El campo de la base de datos que corresponde a la potencia es `active_power`. Por ejemplo, al consultar `/api/max_power?meter=1&date=2022-05-11` devolver algo como:

```
[
    {
        "hour":"2022-05-11T00:00:00-05:00",
        "max_power":140.97
    },
    {
        "hour":"2022-05-11T01:00:00-05:00",
        "max_power":120.1
    },
    {
        "hour":"2022-05-11T02:00:00-05:00",
        "max_power":140.37
    },
    {
        "hour":"2022-05-11T03:00:00-05:00",
        "max_power":180.9
    },
    {
        "hour":"2022-05-11T04:00:00-05:00",
        "max_power":135.6
    },
    {
        "hour":"2022-05-11T05:00:00-05:00",
        "max_power":597.54
    },
    {
        "hour":"2022-05-11T06:00:00-05:00",
        "max_power":162.42
    },
    {
        "hour":"2022-05-11T07:00:00-05:00",
        "max_power":135.6
    },
    {
        "hour":"2022-05-11T08:00:00-05:00",
        "max_power":177.92
    },
    {
        "hour":"2022-05-11T09:00:00-05:00",
        "max_power":126.66
    },
    {
        "hour":"2022-05-11T10:00:00-05:00",
        "max_power":151.1
    },
    {
        "hour":"2022-05-11T11:00:00-05:00",
        "max_power":152.89
    },
    {
        "hour":"2022-05-11T12:00:00-05:00",
        "max_power":147.52
    },
    {
        "hour":"2022-05-11T13:00:00-05:00",
        "max_power":142.75
    },
    {
        "hour":"2022-05-11T14:00:00-05:00",
        "max_power":225.6
    },
    {
        "hour":"2022-05-11T15:00:00-05:00",
        "max_power":210.11
    },
    {
        "hour":"2022-05-11T16:00:00-05:00",
        "max_power":150.5
    },
    {
        "hour":"2022-05-11T17:00:00-05:00",
        "max_power":214.88
    },
    {
        "hour":"2022-05-11T18:00:00-05:00",
        "max_power":161.83
    },
    {
        "hour":"2022-05-11T19:00:00-05:00",
        "max_power":170.17
    },
    {
        "hour":"2022-05-11T20:00:00-05:00",
        "max_power":399.65
    },
    {
        "hour":"2022-05-11T21:00:00-05:00",
        "max_power":611.84
    },
    {
        "hour":"2022-05-11T22:00:00-05:00",
        "max_power":223.82
    },
    {
        "hour":"2022-05-11T23:00:00-05:00",
        "max_power":164.81
    }
]

```

**Los endpoints de los ejemplos y la estructura de salida (formato) son sólo sugerencias, y se pueden estructurar como se desee.**

### Información adicional:
* Se creó un super-usuario en la base de datos con usuario `admin` y contraseña `admin`.
* Los modelos de la aplicación se encuentran en el archivo `energy/models.py`. De este mismo archivo puede inferirse la estructura de la base de datos.
* Si lo crees necesario, puedes crear alguna aplicación, modelo, archivo, etc.. adicional dentro del repositorio.
* Puedes instalar y usar cualquier dependencia o librería adicional.
* Se utilizó Python v.3.9.6 para la configuración inicial del entorno, pero puede realizarse en cualquier otra versión de Python 3.
* Las dependencias se encuentran en el archivo `requirements.txt` y pueden instalarse con `pip install -r requirements.txt`.

