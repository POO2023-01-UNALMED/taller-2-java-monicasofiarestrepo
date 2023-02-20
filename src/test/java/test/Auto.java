package test;

import java.util.ArrayList;
import java.util.List;

public class Auto {
    String modelo;
    int precio;
    List<Asiento> asientos;
    String marca;
    Motor motor;
    int registro;
    static int cantidadCreados;


    public int cantidadAsientos() {
        int cantidad = 0;
        for (char i = 0; i < asientos.length; i++) {
            if (asiento instanceof Asiento) {
                cantidad++;
            }
        }
        return cantidad;
    }

    public String verificarIntegridad() {
        if (Motor.registro() != registro) {
            return "Las piezas no son originales";
        }
        for (Asiento asiento : asientos) {
            if (Asiento.registro() != registro) {
                return "Las piezas no son originales";
            }
        }
        return "Auto original";
    }
}