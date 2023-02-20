package test;

public class Auto {
	String modelo;
	int precio;
	Asiento[] asientos;
	String marca;
	Motor motor;
	int registro;
	int cantidadCreados;	
	
	public int cantidadAsientos() {
		int numAsientos = 0;
		for(int i=0; i < asientos.length ; i++) {
			if(asientos[i] instanceof Asiento) {
				numAsientos++;				
			}
		}
		return numAsientos;
	}
	
	public String verificarIntegridad() {
		if(registro!=motor.registro) {
			return "Las piezas no son originales";		
		}
		for(int a=0; a<asientos.length;a++) {
			if (asientos[a]!=null) {
				if(asientos[a].registro != registro) {
					return "Las piezas no son originales";				
				}
			}
			
		}
		return "Auto original";
		
	}

}