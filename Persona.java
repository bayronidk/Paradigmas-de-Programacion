public class Persona {
    String Nombre;
    int edad;
    float estatura;
    int peso;
    String pais;
    String CURP;
    int sueldo;
    String sexo;

    public Persona(String nombrePersona, int edadPersona, float estaturaPersona, int pesoPersona, String paisPersona, String CURPPersona, int sueldoPersona, String sexoPersona) {
        Nombre = nombrePersona;
        edad = edadPersona;
        estatura = estaturaPersona;
        peso = pesoPersona;
        pais = paisPersona;
        CURP = CURPPersona;
        sueldo = sueldoPersona;
        sexo = sexoPersona;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String nombre) 
    {
        Nombre = nombre;
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Emilio", 19, 1.90f, 70, "Mexico", "ZAGE040806HDFRMMA1", 8000, "Masculino");
        System.out.println("Nombre de la persona:"+persona1.getNombre());
        persona1.setNombre("Juanito");
        System.out.println("Nuevo nombre después del set:"+persona1.getNombre());
    }
}
